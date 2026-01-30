import requests
import re

# لیست کانال‌هایی که می‌خواهی از آن‌ها کد جمع کنی
CHANNELS = [
    "v2ray_outlinefree", 
    "v2ray_free_conf", 
    "biatun_v2ray",
    "v2ray_config_pool"
]

def scrape():
    all_configs = []
    # الگوی شناسایی کانفیگ‌های v2ray
    pattern = r"(vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#]+"
    
    for channel in CHANNELS:
        try:
            url = f"https://t.me/s/{channel}"
            response = requests.get(url, timeout=15)
            # استخراج تمام لینک‌های منطبق با الگو
            configs = re.findall(pattern, response.text)
            all_configs.extend(configs)
            print(f"Fetched {len(configs)} from {channel}")
        except Exception as e:
            print(f"Error scraping {channel}: {e}")
            
    # حذف تکراری‌ها
    unique_configs = list(set(all_configs))
    
    # ذخیره در فایل متنی
    with open("configs.txt", "w") as f:
        f.write("\n".join(unique_configs))

if __name__ == "__main__":
    scrape()
