import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
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
    pattern = r"(?:vmess|vless|trojan|ss|ssr|hy2|tuic)://[a-zA-Z0-9\-_@.:?=&%#]+"
    now = datetime.now().astimezone() # زمان فعلی با منطقه زمانی

    for channel in CHANNELS:
        try:
            response = requests.get(f"https://t.me/s/{channel}", timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            # پیدا کردن تمام کادرهای پیام
            messages = soup.find_all('div', class_='tgme_widget_message_wrap')
            
            for msg in messages:
                time_tag = msg.find('time')
                if time_tag and time_tag.get('datetime'):
                    msg_time = parser.parse(time_tag.get('datetime'))
                    # اگر پیام مربوط به کمتر از ۱ ساعت پیش باشد
                    if now - msg_time <= timedelta(hours=1):
                        text = msg.find('div', class_='tgme_widget_message_text')
                        if text:
                            configs = re.findall(pattern, text.get_text())
                            all_configs.extend(configs)
        except: continue

    with open("configs_hourly.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(list(set(all_configs))))

if __name__ == "__main__":
    get_hourly()
