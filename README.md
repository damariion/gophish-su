# gophish-su (Streamline Utilities)

**gophish-su** is a collection of micro-utilities designed to streamline the phishing workflow in **Gophish** and related applications.
It’s built with **LBVD** usage in mind, focusing on speed, clarity, and easy integration into existing pipelines.

## 🛠 Tools

* **search.py**: fetch campaign information (e.g. name, clicks, submits) and filter using panda's query-syntax
* **mailer.py**: generate an e-mail for the begin, post-24h or end stage of a simulation (statistics are automatically inserted)
* **lander.py**: generate landing-pages through CLI-arguments instead of manual HTML-editing
* **filter.py**: filter e-mails on events (e.g. all e-mails that clicked)

## 📤 Output

* All tools write to **stdout** and **stderr**
* No files are created by default
* Pipe the output to a file if you need to save it:

```bash
gen-landing.py <args> > landing.html
```

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
