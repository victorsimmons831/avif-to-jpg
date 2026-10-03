"""AVIF to JPG — Convert AVIF stills to JPEG so older Windows apps can open them."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='avif_to_jpg',
        description='Convert AVIF stills to JPEG so older Windows apps can open them.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('AVIF to JPG')
    print('Phone AVIF into a JPEG folder.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
