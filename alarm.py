import time, datetime
from selenium import webdriver
import sys, getopt
import sound

AlarmTime = int(input('Alarm time int:'))

#https://www.youtube.com/watch?v=ZZ5LpwO-An4
URL = str(input('Alarm url:') or 'https://www.youtube.com/watch?v=ZZ5LpwO-An4')

print(AlarmTime,URL)

while True:

    if AlarmTime == datetime.datetime.now().hour:
        chromedriver = r'C:\\Users\dylan\Desktop\Windows-Sound-Manager-master\\chromedriver.exe'
        driver = webdriver.Chrome(chromedriver)
        driver.get(URL)
        player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        print(player_status)
        sound.Sound.volume_max()



        break