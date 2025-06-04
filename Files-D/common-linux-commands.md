# 🐧 Common Linux Commands for Cybersecurity & CTFs

This is a cheat sheet of essential Linux commands often used in CTFs, penetration testing, and general system use. Updated daily for GitHub streak 🌟

---

## 🗂️ File & Directory

| Command | Description |
|--------|-------------|
| `ls -la` | List all files including hidden |
| `cd /path/to/dir` | Change directory |
| `pwd` | Show current directory |
| `cp file1 file2` | Copy file |
| `mv file1 dir/` | Move file |
| `rm -rf folder` | Delete folder forcefully (be careful!) |

---

## 🔐 Permissions

| Command | Description |
|---------|-------------|
| `chmod +x script.sh` | Make script executable |
| `chown user:group file` | Change file ownership |

---

## 🔍 Search & Find

| Command | Description |
|---------|-------------|
| `find / -name "flag*.txt" 2>/dev/null` | Find file named `flag*.txt` |
| `grep "password" *.txt` | Search for word in text files |
| `strings binary_file` | Extract printable strings (good for reverse engineering) |

---

## 🧠 System Info

| Command | Description |
|---------|-------------|
| `uname -a` | Full system info |
| `whoami` | Current user |
| `id` | UID, GID info |
| `ifconfig` or `ip a` | Network interfaces |
| `netstat -tulpn` | Show open ports |

---

## ⚙️ Package Management (Debian/Ubuntu)

| Command | Description |
|---------|-------------|
| `sudo apt update && sudo apt upgrade` | Update packages |
| `sudo apt install nmap` | Install `nmap` |
| `dpkg -l` | List installed packages |

---

> ✅ Updated: June 4, 2025  
> 🔁 Use this as a personal cheat sheet or expand it as you learn more!

