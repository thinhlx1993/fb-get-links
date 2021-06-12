import os
import time
import pyautogui
import logging
from datetime import datetime
import clipboard


os.makedirs('uploaded', exist_ok=True)
# create logger with 'spam_application'
logger = logging.getLogger('application')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('app.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def click_to(btn, region=None):
    logger.info(f"Click to {btn}")
    while True:
        ret = pyautogui.locateOnScreen(f"btn/{btn}", confidence=.8, region=region)
        if ret:
            pyautogui.click(ret)
            break


def click_many(btn, region=None):
    logger.info(f"Click many {btn}")
    results = pyautogui.locateAllOnScreen(f"btn/{btn}", confidence=.8, region=region)
    for ret in results:
        pyautogui.click(ret)


def check_exist(btn, region=None):
    exist = pyautogui.locateOnScreen(f"btn/{btn}", confidence=.8, region=region)
    logger.info(f"Check exist {btn} result {exist}")
    return exist


def waiting_for(btn, region=None):
    logger.info(f"Watiing for {btn}")
    while True:
        ret = pyautogui.locateCenterOnScreen(f"btn/{btn}", confidence=.8, region=region)
        if ret:
            x, y = ret
            return x, y


if __name__ == '__main__':
    dir_path = r"C:\code\auto_schedule\upload"
    while True:
        try:
            start_date = pyautogui.prompt('Nhập thời gian bắt đầu lên lịch. \nChú ý định dạng kiểu: 13/6/2021 12:00')
            date_time_obj = datetime.strptime(start_date, '%d/%m/%Y %H:%M')
            date_time_obj_ts = date_time_obj.timestamp()
            break
        except Exception as ex:
            pyautogui.alert('Lỗi, Kiểm tra lại định dạng của thời gian bắt đầu')

    for filename in os.listdir(dir_path):
        clipboard.copy(f"{dir_path}\\{filename}")
        x, y = waiting_for("create_new.png")
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(x, y + 120)
        time.sleep(3)
        pyautogui.hotkey("ctrl", "v")
        click_to("open.PNG")
        click_to("upload_done.png")
        click_many("close_step.png")
        title = waiting_for("title.png")
        title_x, title_y = title
        pyautogui.click(title_x + 50, title_y)

        filename_without_ext = os.path.splitext(filename)[0]
        # fix title
        if '-' in filename_without_ext:
            filename_without_ext = filename_without_ext.split('-')[1]
        pyautogui.typewrite(filename_without_ext)
        click_to("next.png")
        click_to("schedule.PNG")
        schedule_x, schedule_y = waiting_for("auto_schedule.png")

        date_obj = datetime.fromtimestamp(date_time_obj_ts)
        # change date
        pyautogui.click(schedule_x + 30, schedule_y)
        time.sleep(1)
        date = date_obj.strftime("%d/%m/%Y")
        pyautogui.typewrite(date, interval=1)

        # change hour
        pyautogui.click(schedule_x + 120, schedule_y)
        time.sleep(1)
        hour = date_obj.strftime("%H")
        pyautogui.typewrite(hour, interval=1)

        # change time
        pyautogui.click(schedule_x + 130, schedule_y)
        time.sleep(1)
        minute = date_obj.strftime("%M")
        pyautogui.typewrite(minute, interval=1)
        click_to("finish.png")
        waiting_for("done.png")
        click_to("close_success.PNG", region=(1000,200, 300, 400))
        date_time_obj_ts += 3600
        os.rename(f"{dir_path}\\{filename}", f"C:\\code\\auto_schedule\\uploaded\\{filename}")
