# PDF to EPUB (EPUBTurn) for calibre

A calibre plugin that converts a book's PDF, including scanned books, into a reflowable EPUB with [EPUBTurn](https://epubturn.com), then adds the EPUB to the same book in your library.

- The free sample needs no account.
- Paying for the full book happens on the EPUBTurn website. The plugin never sees card details.
- Your PDF is uploaded to EPUBTurn for conversion. See the [privacy policy](https://epubturn.com/privacy.html).

This plugin is in early development. Conversion is not available yet.

## Install

1. Download `epubturn-calibre.zip` from the releases page.
2. In calibre, open **Preferences → Plugins → Load plugin from file** and choose the zip.
3. Restart calibre. Add the **Convert PDF to EPUB** button to a toolbar if calibre does not add it.

## Develop

```sh
./build.sh                                  # builds dist/epubturn-calibre.zip
calibre-customize -a dist/epubturn-calibre.zip
calibre-debug -g                            # start calibre with debug output
```

On macOS the calibre tools are in `/Applications/calibre.app/Contents/MacOS/`.

## Licence

GNU General Public License v3 or later. See `LICENSE`.
