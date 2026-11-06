#!/bin/sh
# Build the installable plugin zip: dist/epubturn-calibre.zip
set -e
cd "$(dirname "$0")"
mkdir -p dist
rm -f dist/epubturn-calibre.zip
cp LICENSE plugin/LICENSE
(cd plugin && zip -qr ../dist/epubturn-calibre.zip . -x '*.pyc' -x '__pycache__/*')
rm plugin/LICENSE
echo dist/epubturn-calibre.zip
