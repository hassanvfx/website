# Image asset workflow

For every displayed image added or replaced, run `python3 generator/optimize_images.py --source <local-path-or-https-url> --name <kebab-case-name> --preset <photo|graphic> --max-width <px>`.

The script is the only writer for `generator/image_manifest.json`. Never hand-edit the manifest, add a direct image URL, or reference an untracked image file from generator data or templates. Reference displayed images by manifest key, then run `python3 generator/generate.py` and `python3 generator/verify_image_assets.py`. Never edit generated HTML directly.
