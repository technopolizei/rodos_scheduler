import requests
import schedule
import time
from datetime import datetime

# Список URL-адресов для запросов
URLS = [
    "http://192.168.60.11/protect/rb0n.cgi",
    "http://192.168.60.11/protect/rb1n.cgi",
    "http://192.168.60.11/protect/rb2n.cgi",
    "http://192.168.60.11/protect/rb3n.cgi",
    "http://192.168.60.11/protect/rb4n.cgi",
    "http://192.168.60.11/protect/rb5n.cgi",
    "http://192.168.60.11/protect/rb6n.cgi",
    "http://192.168.60.11/protect/rb7n.cgi"
]

def send_get_requests():
    today = datetime.today().weekday()
    if today >= 5:  # Выходные (5=Сб, 6=Вс)
        print(f"[{datetime.now()}] Выходной день — запросы не отправлены")
        return

    print(f"[{datetime.now()}] Начало отправки 8 запросов...")
    
    for idx, url in enumerate(URLS, 1):
        try:
            response = requests.get(url)
            print(f"[{datetime.now()}] Запрос {idx}/8: {url} — код {response.status_code}")
        except Exception as e:
            print(f"[{datetime.now()}] Запрос {idx}/8: Ошибка — {str(e)}")
        time.sleep(1)  # Пауза между запросами 

    print(f"[{datetime.now()}] Все запросы выполнены\n")

# Настройка расписания
schedule.every().day.at("08:00").do(send_get_requests)

print("Скрипт запущен. Ожидание запросов по расписанию...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Проверка расписания каждую минуту 