import requests
import re
from urllib.parse import unquote

# لیست کانال‌های هدف
CHANNELS = [
    "farah_vpn"
]

def scrape():
    all_configs = []
    # الگوی دقیق برای شناسایی تمام پروتکل‌ها
    pattern = r"(vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#]+"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for channel in CHANNELS:
        try:
            print(f"Scraping {channel}...")
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                # استخراج تمام لینک‌ها از کل صفحه (مشابه منطق اپلیکیشن شما)
                matches = re.findall(pattern, response.text)
                
                for match in matches:
                    # تمیز کردن لینک (در صورت وجود کاراکترهای اضافی HTML)
                    config = match.split('<')[0].split('"')[0].split(' ')[0]
                    all_configs.append(config)
                    
                print(f"Found {len(matches)} configs in {channel}")
        except Exception as e:
            print(f"Error in {channel}: {e}")

    # حذف موارد تکراری
    unique_configs = list(set(all_configs))
    
    # ذخیره نهایی
    with open("configs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_configs))
    print(f"Done! Total unique configs: {len(unique_configs)}")

if __name__ == "__main__":
    scrape()
