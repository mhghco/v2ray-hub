import requests
import re

# لیست کانال‌های هدف
CHANNELS = [
    "AR14N24b", "Airdorap_Free", "Alpha_V2ray_Group", "Alpha_V2ray_Iran", "AmyraxVPN", "AmyraxVPNGap", "AzadNet", "BlueShekan", "ChinaPortGFW",
    "ConfigX2ray", "DrovOne", "Echo_Center", "Farah_VPN", "Filtereshekan", "Fr33C0nfig", "Ln2Ray", "MaKVaslim", "MdVpnSec", "NETMelliAnti", "Oghab_VPN",
    "ProxyDotNet", "ProxyTelCo", "SaghiVpnX", "TEHRANARGO", "TweetPublic", "V2RAY_SPATIAL", "V2rayEnglish", "V2ray_Alpha", "VPNSupportGroup", "Vaslchi_VPN",
    "VpnMaan", "XpnTeam", "YamYamProxy", "anty_filter", "beshcan", "bored_vpn", "chat_nakone", "configraygan", "confing_proxi1", "cpy_teeL", "duckvp_n",
    "hormozvpn", "iHomeii", "internetmelil", "mehrosaboran", "meliproxyy", "mitivpn", "nufilter", "numb_frozen", "shankamil", "sogoandfuckyourlove",
    "tabiatvpn1", "v2FreeHub", "v2raygencon", "v2rayngvpn", "v2wray", "wallpaper_4k3d", "xsfilternet"
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
