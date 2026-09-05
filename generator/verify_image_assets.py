#!/usr/bin/env python3
"""Verify image-manifest integrity and generated image references."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = Path(__file__).with_name("image_manifest.json")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
IMAGE_TAG_RE = re.compile(r"<img\b[^>]*>")
ATTRIBUTE_RE = re.compile(r'\b([a-zA-Z-]+)="([^"]*)"')
PROPORTIONAL_IMAGE_SELECTORS = (
    ".book-cover--portrait",
    ".bio-profile-image img",
    ".meme-arcade-icon",
    ".meme-arcade-screen-card img",
    ".wwdc14-slide",
    ".featured-book-cover",
    ".citations-cover",
)


def dimensions(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "json", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    stream = json.loads(result.stdout)["streams"][0]
    return int(stream["width"]), int(stream["height"])


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    urls = set()
    entries_by_url = {}
    for name, entry in manifest.items():
        if not NAME_RE.fullmatch(name):
            fail(f"invalid manifest name: {name}")
        required = {"source", "preset", "max_width", "width", "height", "fingerprint", "url"}
        if required - entry.keys():
            fail(f"manifest entry is incomplete: {name}")
        expected_url = f"assets/{name}.{entry['fingerprint']}.webp"
        if entry["url"] != expected_url:
            fail(f"unexpected URL for {name}: {entry['url']}")
        path = ROOT / entry["url"]
        if not path.is_file():
            fail(f"missing asset for {name}: {path}")
        if hashlib.sha256(path.read_bytes()).hexdigest()[:12] != entry["fingerprint"]:
            fail(f"fingerprint mismatch for {name}")
        if dimensions(path) != (entry["width"], entry["height"]):
            fail(f"dimension mismatch for {name}")
        urls.add(entry["url"])
        entries_by_url[entry["url"]] = entry

    for page in ("index.html", "selected-work.html"):
        page_html = (ROOT / page).read_text(encoding="utf-8")
        image_tags = IMAGE_TAG_RE.findall(page_html)
        if not image_tags:
            fail(f"no image references found in {page}")
        for tag in image_tags:
            attributes = dict(ATTRIBUTE_RE.findall(tag))
            url = attributes.get("src")
            if not url:
                fail(f"image without a src in {page}: {tag}")
            if url not in urls:
                fail(f"unmanifested image in {page}: {url}")
            if not url.endswith(".webp"):
                fail(f"non-WebP image in {page}: {url}")
            entry = entries_by_url[url]
            if attributes.get("width") != str(entry["width"]) or attributes.get("height") != str(entry["height"]):
                fail(f"missing or incorrect intrinsic dimensions in {page}: {url}")
            if attributes.get("decoding") != "async":
                fail(f"missing async decoding in {page}: {url}")
        for selector in PROPORTIONAL_IMAGE_SELECTORS:
            rule = re.search(rf"{re.escape(selector)}\s*\{{([^}}]*)\}}", page_html)
            if not rule or "height: auto" not in rule.group(1):
                fail(f"missing proportional height rule in {page}: {selector}")
    print(f"Verified {len(manifest)} fingerprinted WebP assets and generated image references.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"Image asset verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
