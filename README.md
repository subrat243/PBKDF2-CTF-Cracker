# 🔐 PBKDF2 CTF Password Cracker

A high-performance Python tool designed for cracking **PBKDF2-HMAC-SHA512 hashes** in Capture The Flag (CTF) challenges using intelligent wordlist mutations and multiprocessing.

---

## 🚀 Features

* ⚡ Multi-core processing (uses all CPU cores)
* 🧠 Smart mutation engine (CTF-focused patterns)
* 🔍 Optimized for PBKDF2 (high iteration counts)
* 📊 Real-time progress tracking
* 🎯 Custom wordlist support

---

## 🛠️ Tech Stack

* Python 3
* hashlib
* multiprocessing

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/pbkdf2-ctf-cracker.git
cd pbkdf2-ctf-cracker
```

---

## ▶️ Usage

Edit configuration inside `cracker.py`:

```python
salt = b"your_salt_here"
target = "your_hash_here"
iterations = 2000000
wordlist_file = "wordlists/custom.txt"
```

Run:

```bash
python3 cracker.py
```

---

## 🧠 Strategy

This tool avoids naive brute force by:

* Using targeted mutations (e.g., `backup → backup123`)
* Leveraging contextual hints (e.g., salt-based patterns)
* Reducing search space for faster cracking

---

## ⚠️ Disclaimer

This tool is intended **only for educational purposes and authorized CTF challenges**. Do not use it on systems without permission.

---

## 🏆 Author

**Subrat Samantaray**
Cybersecurity Enthusiast | Offensive Security | CTF Player

---

## ⭐ Contribute

Feel free to fork, improve mutation rules, or optimize performance!
