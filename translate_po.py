#!/usr/bin/env python3
"""
Translate .po files using GoogleTranslator from deep_translator.

Usage:
    python translate_po.py

Dependencies:
    - polib
    - deep_translator

Author: Rafael Arraez
"""

import polib
from deep_translator import GoogleTranslator


def translate_po_file(input_path: str, output_path: str, source_lang: str = 'en', target_lang: str = 'es'):
    """
    Translate a .po file from source language to target language.

    :param input_path: Path to the input .po file
    :param output_path: Path to save the translated .po file
    :param source_lang: Source language code (default 'en')
    :param target_lang: Target language code (default 'es')
    """
    print(f"📂 Loading file: {input_path}")
    po = polib.pofile(input_path)
    translator = GoogleTranslator(source=source_lang, target=target_lang)

    count = 0
    for entry in po.untranslated_entries():
        try:
            translated = translator.translate(entry.msgid)
            entry.msgstr = translated or ""
            count += 1
            print(f"✅ {count}. '{entry.msgid}' ➜ '{entry.msgstr}'")
        except Exception as e:
            print(f"❌ Error translating '{entry.msgid}': {e}")

    po.save(output_path)
    print(f"\n💾 Translations saved to: {output_path}")


if __name__ == "__main__":
    INPUT_FILE = 'path/to/file.po'
    OUTPUT_FILE = 'path/to/file-translated.po'
    translate_po_file(INPUT_FILE, OUTPUT_FILE)
