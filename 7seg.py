import sys
import RPi.GPIO as GPIO
import time,datetime
import tm1637
GPIO.setmode(GPIO.BOARD) //---------for board pins 
Display=tm1637.TM1637(16,18,tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightness(1)
while(True):
    now=datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    currenttime=[int(hour/time),hour%10,int(minute/10),minute%10]
    Display.Show(currenttime)
    Display.ShowDoublepoint(second%2)
time.sleep(1)

