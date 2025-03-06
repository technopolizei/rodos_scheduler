import requests
import schedule
import time
from datetime import datetime

# Списки URL для разных запросов
MORNING_URLS = [
    "http://admin:admin@192.168.60.11/protect/rb0n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb1n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb2n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb3n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb4n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb5n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb6n.cgi",
    "http://admin:admin@192.168.60.11/protect/rb7n.cgi"
]

EVENING_URLS = [
    "http://admin:admin@192.168.60.11/protect/rb0f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb1f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb2f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb3f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb4f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb5f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb6f.cgi",
    "http://admin:admin@192.168.60.11/protect/rb7f.cgi"
]

def send_requests(url_list, time_label):
    today = datetime.today().weekday()
    if today >= 5:
        print(f"[{datetime.now()}] Weekend! — {time_label} requests dismissed")
        return

    print(f"[{datetime.now()}] Starting {time_label} requests...")
    
    for idx, url in enumerate(url_list, 1):
        try:
            response = requests.get(url, timeout=5)
            status_msg = f"Code: {response.status_code}"
        except Exception as e:
            status_msg = f"Response: {type(e).__name__}"
        
        print(f"[{datetime.now()}] {time_label.capitalize()} request {idx}/8: {url} — {status_msg}")
        time.sleep(0.3)

    print(f"[{datetime.now()}] All {time_label} requests is done\n")

# Функции-обертки для расписания
def send_morning_requests():
    send_requests(MORNING_URLS, "mornings")

def send_evening_requests():
    send_requests(EVENING_URLS, "evenings")

# Настройка расписания
schedule.every().day.at("08:00").do(send_morning_requests)
schedule.every().day.at("23:59").do(send_evening_requests)

print("Script is working. Wait to special time...")
while True:
    schedule.run_pending()
    time.sleep(60)