# 🌍 .po Translator

A Python script to translate `.po` localization files using Google Translate via the `deep_translator` library.

---

## 🚀 Features

- ✅ Automatically translates only untranslated entries (`msgstr == ""`)
- 🌐 Uses the public Google Translate API (no API key required)
- 📄 Saves translations in a new `.po` file
- 💡 Simple and easy to use — great for localization workflows
- 🛠️ Optional CLI support for custom file paths and language configuration

---

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/po-translator.git
cd po-translator
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate it

```bash
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 4. Intall dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Basic Usage

### 1. Place your .po file in the same directory and make sure it's named:

```bash
trx_addons-es_VE.po
```

### 1. Place your .po file in the same directory and make sure it's named:

```bash
trx_addons-es_VE.po
```

### 2. A translated file will be saved as:

```bash
trx_addons-es_VE.po
```

### 3. Run the script:

```bash
python translate_po.py
```

## 🙌 Contributing
Feel free to open an issue or submit a pull request to suggest improvements or fixes.