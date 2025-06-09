#!/bin/bash
# wifi-password-viewer.sh
# View saved Wi-Fi passwords on Linux (NetworkManager)

echo -e "\n📶 Saved Wi-Fi Networks and Passwords:\n"
echo -e "SSID\t\t\tPassword"
echo "------------------------------------------"

# Path to NetworkManager profiles
config_dir="/etc/NetworkManager/system-connections/"

# Loop through each profile
for file in "$config_dir"*; do
    if grep -q "psk=" "$file"; then
        ssid=$(grep '^ssid=' "$file" | cut -d= -f2-)
        psk=$(grep '^psk=' "$file" | cut -d= -f2-)
        printf "%-24s %s\n" "$ssid" "$psk"
    fi
done

echo -e "\n✅ Done. Keep your credentials safe!"
