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
    pattern = r"(?:vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#]+"

    for channel in CHANNELS:
        try:
            response = requests.get(f"https://t.me/s/{channel}", timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            messages = soup.find_all('div', class_='tgme_widget_message_wrap')
            
            # فقط ۲۰ پیام آخر هر کانال را بررسی کن
            for msg in messages[-20:]:
                text = msg.find('div', class_='tgme_widget_message_text')
                if text:
                    configs = re.findall(pattern, text.get_text())
                    all_configs.extend(configs)
        except: continue

    with open("configs_recent.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(list(set(all_configs))))

if __name__ == "__main__":
    get_recent()
