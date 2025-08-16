# 🛰️ Pentrail

**Pentrail** is a **modular, terminal-based reconnaissance tool** built for penetration testers. It automates early-stage recon tasks and is designed with extensibility and simplicity in mind.

---

## ✨ Features

- 🔎 Subdomain Enumeration
- 🌐 Port Scanning
- 📜 JavaScript Link Finder
- 🧪 CORS Checker
- 📁 Directory Enumeration
- 👤 WHOIS Lookup

---

## 🛠️ Installation

```bash
git clone https://github.com/Aydin457/pentrail.git
cd pentrail
chmod +x pentrail.py
```

> Requires Python 3.7 or higher.

---

## 🚀 Usage

Each module can be run independently:

```bash
python3 pentrail.py -m subenum -t example.com
python3 pentrail.py -m portscan -t example.com
python3 pentrail.py -m jsfinder -t example.com
python3 pentrail.py -m cors -t example.com
python3 pentrail.py -m direnum -t example.com
python3 pentrail.py -m whois -t example.com
```

> Don’t forget to specify the target domain with the `-t` flag.

---

## 📂 Wordlists

Pentrail **does not include wordlists** by default. You are expected to supply your own using the `--wordlist` flag:

```bash
python3 pentrail.py direnum -t example.com --wordlist /path/to/custom_wordlist.txt
```

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

---

## 👨‍💻 Author

Developed by [Aydın Yasinov](https://github.com/Aydin457)

---

## ⚠️ Disclaimer

This tool is intended **only for use on systems you own or have explicit permission to test**. Unauthorized use is strictly prohibited and is the sole responsibility of the user.

---

## 📬 Contact

- 📧 Email: yasinovaydin@gmail.com  
- 🔗 Linkedin: [linkedin.com/in/aydın-yasinov](https://www.linkedin.com/in/aydın-yasinov/)
