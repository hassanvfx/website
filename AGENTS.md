# Repository editing guidance

- Treat `generator/` as the source of truth for the website.
- Never edit generated HTML files such as `index.html` or `selected-work.html` directly.
- Make website changes in the generator or its data/templates, then run `python3 generator/generate.py` to regenerate the published files.
- Verify both the generator source and the regenerated output before considering a website change complete.

## Image asset workflow

- For every displayed image added or replaced, run `python3 generator/optimize_images.py --source <local-path-or-https-url> --name <kebab-case-name> --preset <photo|graphic> --max-width <px>`.
- The script is the only writer for `generator/image_manifest.json`; never hand-edit the manifest, add a direct image URL, or reference an untracked image file from generator data or templates.
- Reference displayed images by their manifest key, then run `python3 generator/generate.py` and `python3 generator/verify_image_assets.py` before completing the change.
