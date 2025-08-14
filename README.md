# gophish-su (Streamline Utilities)

**gophish-su** is a collection of micro-utilities designed to streamline the phishing workflow in **Gophish** and related applications.
It’s built with **LBVD** usage in mind, focusing on speed, clarity, and easy integration into existing pipelines.

---

## 🔧 Installation

From the `setup` directory, run one of the installers:

```bash
# On Linux/macOS
cd setup
./install.sh

# On Windows (PowerShell)
cd setup
.\install.ps1
```

⚠️ You must be inside the `setup` directory for installation to work correctly.

---

## 🛠 Tool Categories

* **`gen-*`** → Generative tools (e.g. content generators)
* **`view-*`** → Viewing tools (e.g. campaign information, CLI data exploration)
* **`to-*`** → Conversion tools (format converters for interoperability, e.g. Gophish ↔ Lucy)

---

## 📤 Output

* All tools write to **stdout** and **stderr**
* No files are created by default
* Pipe the output to a file if you need to save it:

```bash
gen-landing.py <args> > landing.html
```