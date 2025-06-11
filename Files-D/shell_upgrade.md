### Shell Upgrade Commands (Line-by-Line)

```bash
# 1. Spawn a proper interactive shell using Python's PTY module
python3 -c 'import pty; pty.spawn("/bin/bash")'

# 2. Set the default shell to bash (better than /bin/sh)
export SHELL=/bin/bash

# 3. Enable 256-color support for terminal applications
export TERM=xterm-256color

# 4. Enable truecolor (24-bit RGB) support if available
export COLORTERM=truecolor

# 5. Put current terminal in raw mode and disable echo
stty raw -echo

# 6. Bring the backgrounded shell to foreground (after pressing Ctrl+Z)
fg

# 7. Reset terminal settings to sane defaults
reset

# 8. Set correct rows and columns based on your current terminal size
stty rows $(stty size | cut -d' ' -f1) columns $(stty size | cut -d' ' -f2)

# 9. Clear the screen for a clean workspace
clear
