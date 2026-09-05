#!/usr/bin/env python3
"""Convert declared website images to cache-busted WebP assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = Path(__file__).with_name("image_manifest.json")
ASSETS_DIR = ROOT / "assets"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PRESETS = {"photo": 82, "graphic": 90}


def load_manifest() -> dict[str, dict]:
    with MANIFEST_PATH.open(encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


def write_manifest(manifest: dict[str, dict]) -> None:
    with MANIFEST_PATH.open("w", encoding="utf-8") as manifest_file:
        json.dump(manifest, manifest_file, indent=2, sort_keys=True)
        manifest_file.write("\n")


def image_dimensions(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "json", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    stream = json.loads(result.stdout)["streams"][0]
    return int(stream["width"]), int(stream["height"])


def source_file(source: str, temporary_dir: Path) -> Path:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        destination = temporary_dir / "downloaded-image"
        command = ["curl", "--fail", "--location", "--silent", "--show-error", "--output", str(destination), source]
        for attempt in range(3):
            result = subprocess.run(command, check=False)
            if result.returncode == 0:
                return destination
            if attempt < 2:
                time.sleep(attempt + 1)
        raise subprocess.CalledProcessError(result.returncode, command)
    if parsed.scheme:
        raise ValueError("--source must be an https URL or a workspace-relative file path")
    path = (ROOT / source).resolve()
    if ROOT not in path.parents or not path.is_file():
        raise ValueError("local --source must name an existing file inside this workspace")
    return path


def convert(name: str, entry: dict) -> dict:
    source = entry["source"]
    recorded_source = entry.get("record_source", source)
    preset = entry["preset"]
    max_width = int(entry["max_width"])
    if preset not in PRESETS:
        raise ValueError(f"Unsupported preset for {name}: {preset}")
    if max_width < 1:
        raise ValueError(f"max_width for {name} must be positive")

    with tempfile.TemporaryDirectory(prefix="website-image-") as temp_name:
        temporary_dir = Path(temp_name)
        input_path = source_file(source, temporary_dir)
        original_width, original_height = image_dimensions(input_path)
        output_width = min(original_width, max_width)
        temporary_output = temporary_dir / "optimized.webp"
        subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(input_path),
                "-frames:v", "1", "-vf", f"scale={output_width}:-2",
                "-c:v", "libwebp", "-preset", "picture", "-quality", str(PRESETS[preset]),
                "-compression_level", "6", str(temporary_output),
            ],
            check=True,
        )
        width, height = image_dimensions(temporary_output)
        fingerprint = hashlib.sha256(temporary_output.read_bytes()).hexdigest()[:12]
        output_name = f"{name}.{fingerprint}.webp"
        output_path = ASSETS_DIR / output_name
        shutil.move(str(temporary_output), output_path)

    return {
        "source": recorded_source,
        "preset": preset,
        "max_width": max_width,
        "original_width": original_width,
        "original_height": original_height,
        "width": width,
        "height": height,
        "fingerprint": fingerprint,
        "url": f"assets/{output_name}",
    }


def update_entry(manifest: dict[str, dict], name: str, source: str, preset: str | None, max_width: int | None, record_source: str | None) -> None:
    if not NAME_RE.fullmatch(name):
        raise ValueError("--name must be a kebab-case semantic name")
    existing = manifest.get(name, {})
    entry = {
        "source": source,
        "preset": preset or existing.get("preset", "photo"),
        "max_width": max_width if max_width is not None else existing.get("max_width"),
    }
    if entry["max_width"] is None:
        raise ValueError("a new image requires --max-width")
    if record_source:
        entry["record_source"] = record_source
    manifest[name] = convert(name, entry)
    write_manifest(manifest)
    print(manifest[name]["url"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="workspace-relative image path or HTTPS URL")
    parser.add_argument("--name", required=True, help="kebab-case manifest key and output filename stem")
    parser.add_argument("--preset", choices=sorted(PRESETS), help="encoding preset")
    parser.add_argument("--max-width", type=int, help="maximum intrinsic output width")
    parser.add_argument("--record-source", help="provenance to retain when optimizing from a local derivative")
    args = parser.parse_args()

    manifest = load_manifest()
    try:
        update_entry(manifest, args.name, args.source, args.preset, args.max_width, args.record_source)
    except (OSError, subprocess.CalledProcessError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Image optimization failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
