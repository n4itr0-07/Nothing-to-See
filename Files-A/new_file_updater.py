import requests
from bs4 import BeautifulSoup

RESULT_URL = 'URL_TO SCRAP'
WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'
LAST_FILE = 'last_result.txt'

def send_discord_notification(message):
    data = {
        "content": f"📢 **New BGSBU Result Published!**\n{message}\n🔗 {RESULT_URL}"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("✅ Notification sent to Discord!")
    else:
        print("❌ Failed to send notification.")

def fetch_latest_result():
    try:
        res = requests.get(RESULT_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        link = soup.find_all('a')
        return link[0].text.strip() if link else None
    except Exception as e:
        print(f"Error fetching result: {e}")
        return None

def read_last_result():
    try:
        with open(LAST_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def write_last_result(result):
    with open(LAST_FILE, 'w') as f:
        f.write(result)

def main():
    latest = fetch_latest_result()
    previous = read_last_result()

    if latest and latest != previous:
        write_last_result(latest)
        send_discord_notification(latest)
    else:
        print("⏳ No new result.")

if __name__ == '__main__':
    main()
