import os
import time
import pyautogui
import logging
import clipboard
from datetime import datetime
from utils import logger, click_to, click_many, check_exist, waiting_for


if __name__ == '__main__':
    number_invited = 0
    while number_invited < 200:
        if check_exist("like.PNG", region=(900, 200, 70, 800)):
            click_to("like.PNG", region=(900, 200, 70, 800))

            waiting = 0
            while waiting <= 3:
                number_invited += click_many("invite.PNG", region=(900, 200, 600, 800))
                pyautogui.moveTo(x=1091, y=573, duration=0.5)
                pyautogui.scroll(-400)
                pyautogui.scroll(-400)
                time.sleep(1)
                if not check_exist("invite.PNG", region=(900, 200, 600, 800)):
                    waiting += 1
            if check_exist("close_invite.PNG", region=(900, 200, 600, 800)):
                click_to("close_invite.PNG", region=(900, 200, 600, 800))
        pyautogui.moveTo(x=1635, y=655, duration=0.5)
        pyautogui.click(x=1635, y=655)
        pyautogui.scroll(-1500)
        pyautogui.scroll(-1000)
        time.sleep(1)
