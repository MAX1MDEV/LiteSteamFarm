import os
import time
import schedule
import threading

def run_dollar_program():
    os.startfile("steam://rungameid/3069470")
    time.sleep(20)  # ждем 20 секунд
    os.system("taskkill /im Dollar.exe")

def run_idle_kitties_program():
    os.startfile(r"C:\Program Files (x86)\Steam\steamapps\common\Idle Kitties Online\IdleKittiesOnline.exe")
    time.sleep(600)  # ждем 10 минут
    os.system("taskkill /im IdleKittiesOnline-Win64-Shipping.exe")

def job_dollar():
    thread = threading.Thread(target=run_dollar_program)
    thread.start()

def job_idle_kitties():
    thread = threading.Thread(target=run_idle_kitties_program)
    thread.start()
    
# отправляем сигнал сразу при запуске скрипта
job_dollar()
job_idle_kitties()

schedule.every(30).minutes.do(job_dollar)  # запускаем игру каждые 30 минут
schedule.every(3).hours.do(job_idle_kitties)  # а эту запускаем каждые 3 часа
def run_schedule():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Программа завершена.")
            os._exit(0)

# запускаем все в одном потоке
run_schedule()
