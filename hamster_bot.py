import pyautogui as pa
from time import sleep
import keyboard
import asyncio
import math

a = int(input('Введите лимит энергии: '))
b = int(input('Введите кол-во монет в тап: '))
print(math.floor(float(a) / float(b)))

sleep(3)
pa.moveTo(x=1007, y=565)



for i in range(math.floor(float(a) / float(b))):
    pa.click()
    sleep(0.01)



keyboard.wait()   