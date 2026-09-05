# Repository editing guidance

- Treat `generator/` as the source of truth for the website.
- Never edit generated HTML files such as `index.html` or `selected-work.html` directly.
- Make website changes in the generator or its data/templates, then run `python3 generator/generate.py` to regenerate the published files.
- Verify both the generator source and the regenerated output before considering a website change complete.
