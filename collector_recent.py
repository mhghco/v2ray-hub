import requests
from bs4 import BeautifulSoup
import re

CHANNELS = [
  "AR14N24b", "Airdorap_Free", "Alpha_V2ray_Group", "Alpha_V2ray_Iran", "AmyraxVPN", "AmyraxVPNGap", "AzadNet", "BlueShekan", "ChinaPortGFW",
  "ConfigX2ray", "DrovOne", "Echo_Center", "Farah_VPN", "Filtereshekan", "Fr33C0nfig", "Ln2Ray", "MaKVaslim", "MdVpnSec", "NETMelliAnti", "Oghab_VPN",
  "ProxyDotNet", "ProxyTelCo", "SaghiVpnX", "TEHRANARGO", "TweetPublic", "V2RAY_SPATIAL", "V2rayEnglish", "V2ray_Alpha", "VPNSupportGroup", "Vaslchi_VPN",
  "VpnMaan", "XpnTeam", "YamYamProxy", "anty_filter", "beshcan", "bored_vpn", "chat_nakone", "configraygan", "confing_proxi1", "cpy_teeL", "duckvp_n",
  "hormozvpn", "iHomeii", "internetmelil", "mehrosaboran", "meliproxyy", "mitivpn", "nufilter", "numb_frozen", "shankamil", "sogoandfuckyourlove", "tabiatvpn1",
  "v2FreeHub", "v2raygencon", "v2rayngvpn", "v2wray", "wallpaper_4k3d", "xsfilternet"
]

def get_recent():
    all_configs = []
    pattern = r"(?:vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#\/]+"

    print("Starting recent collection...")

    for channel in CHANNELS:
        try:
            response = requests.get(f"https://t.me/s/{channel}", timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            messages = soup.find_all('div', class_='tgme_widget_message_wrap')
            
            # بررسی 25 پیام آخر
            for msg in messages[-25:]:
                # جستجو در سورس HTML پیام برای پیدا کردن لینک‌های مخفی
                msg_content = str(msg)
                configs = re.findall(pattern, msg_content)
                all_configs.extend(configs)
        except Exception as e:
            continue

    unique_configs = list(set(all_configs))
    print(f"Found {len(unique_configs)} unique recent configs.")

    with open("configs_recent.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_configs))

if __name__ == "__main__":
    get_recent()
