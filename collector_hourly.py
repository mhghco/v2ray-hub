import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta, timezone
from dateutil import parser

CHANNELS = [
  "AR14N24b", "Airdorap_Free", "Alpha_V2ray_Group", "Alpha_V2ray_Iran", "AmyraxVPN", "AmyraxVPNGap", "AzadNet", "BlueShekan", "ChinaPortGFW",
  "ConfigX2ray", "DrovOne", "Echo_Center", "Farah_VPN", "Filtereshekan", "Fr33C0nfig", "Ln2Ray", "MaKVaslim", "MdVpnSec", "NETMelliAnti", "Oghab_VPN",
  "ProxyDotNet", "ProxyTelCo", "SaghiVpnX", "TEHRANARGO", "TweetPublic", "V2RAY_SPATIAL", "V2rayEnglish", "V2ray_Alpha", "VPNSupportGroup", "Vaslchi_VPN",
  "VpnMaan", "XpnTeam", "YamYamProxy", "anty_filter", "beshcan", "bored_vpn", "chat_nakone", "configraygan", "confing_proxi1", "cpy_teeL", "duckvp_n",
  "hormozvpn", "iHomeii", "internetmelil", "mehrosaboran", "meliproxyy", "mitivpn", "nufilter", "numb_frozen", "shankamil", "sogoandfuckyourlove", 
  "tabiatvpn1", "v2FreeHub", "v2raygencon", "v2rayngvpn", "v2wray", "wallpaper_4k3d", "xsfilternet"
]

def get_hourly():
    all_configs = []
    # پترن بهبود یافته برای گرفتن لینک‌های ناقص یا انکود شده
    pattern = r"(?:vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#\/]+"
    
    # استفاده از زمان UTC دقیق برای مقایسه
    now = datetime.now(timezone.utc)

    print(f"Starting hourly collection at {now}")

    for channel in CHANNELS:
        try:
            # درخواست به نسخه موبایل یا وب تلگرام
            response = requests.get(f"https://t.me/s/{channel}", timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            messages = soup.find_all('div', class_='tgme_widget_message_wrap')
            
            for msg in messages:
                time_tag = msg.find('time')
                if time_tag and time_tag.get('datetime'):
                    # پارس کردن زمان پیام و تبدیل به UTC
                    msg_time = parser.parse(time_tag.get('datetime')).astimezone(timezone.utc)
                    
                    # بررسی شرط یک ساعت اخیر
                    if now - msg_time <= timedelta(hours=1):
                        # نکته مهم: جستجو در کل HTML پیام (نه فقط متن)
                        # این کار باعث میشه لینک‌های داخل تگ <a> هم پیدا بشن
                        msg_content = str(msg)
                        configs = re.findall(pattern, msg_content)
                        all_configs.extend(configs)
        except Exception as e:
            print(f"Error scraping {channel}: {e}")
            continue

    # حذف تکراری‌ها و ذخیره
    unique_configs = list(set(all_configs))
    print(f"Found {len(unique_configs)} unique configs in the last hour.")
    
    with open("configs_hourly.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_configs))

if __name__ == "__main__":
    get_hourly()
