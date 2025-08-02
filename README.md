
# 🛰️ Pentrail

**Pentrail** — pentesterlər üçün yazılmış **modulyar və terminal əsaslı reconnaissance alətidir**. Bu alət ilkin kəşfiyyat mərhələlərini avtomatlaşdırır və genişlənə bilən arxitekturaya malikdir.





## ✨ Xüsusiyyətlər

- 🔎 Subdomain Enumeration
- 🌐 Port Scan
- 📜 JavaScript Link Finder
- 🧪 CORS Checker
- 📁 Directory Enumeration
- 👤 WHOIS Lookup

---

## 🛠️ Quraşdırma

```bash
git clone https://github.com/aydin-yasinov/pentrail.git
cd pentrail
chmod +x pentrail.py
```

> Python 3.7+ tələb olunur.

---

## 🚀 İstifadə

Hər modulu ayrıca işlədə bilərsən:

```bash
python3 pentrail.py subenum -d example.com
python3 pentrail.py portscan -d example.com
python3 pentrail.py jsfinder -d example.com
python3 pentrail.py cors -d example.com
python3 pentrail.py direnum -d example.com
python3 pentrail.py whois -d example.com
```

> `-d` parametrindən sonra target domeni qeyd etməyi unutma.

---

## 📂 Wordlist-lər

Bu layihə istifadəçilərin **öz wordlistlərini** istifadə etmələrini nəzərdə tutur. İstəyə uyğun olaraq `--wordlist` flag-i ilə əlavə oluna bilər.

```bash
python3 pentrail.py direnum -d example.com --wordlist /path/to/custom_wordlist.txt
```

---

## 📄 License

Bu layihə **Apache License 2.0** ilə lisenziyalanıb. Ətraflı məlumat üçün `LICENSE` faylına baxın.

---

## 👨‍💻 Müəllif

Bu layihə [Aydın Yasinov](https://github.com/aydin-yasinov) tərəfindən hazırlanıb.

---


## 🧠 Qeyd

Bu alət yalnız **təhlükəsizlik testləri üçün icazə verilmiş sistemlərdə** istifadə olunmalıdır. İcazəsiz istifadəyə görə məsuliyyət istifadəçiyə aiddir.
