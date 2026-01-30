import requests
import re

# لیست کانال‌های هدف
CHANNELS = [
    "v2wray",
    "farah_vpn",
    "AR14N24B"
]

def scrape():
    all_configs = []
    # اضافه کردن ?: باعث می‌شود کل لینک استخراج شود نه فقط پیشوند
    pattern = r"(?:vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#]+"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                # حالا کل لینک را پیدا می‌کند
                matches = re.findall(pattern, response.text)
                all_configs.extend(matches)
                print(f"Fetched {len(matches)} configs from {channel}")
        except Exception as e:
            print(f"Error in {channel}: {e}")

    # حذف تکراری‌ها
    unique_configs = list(set(all_configs))
    
    with open("configs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_configs))
    print(f"Total Unique: {len(unique_configs)}")

if __name__ == "__main__":
    scrape()
