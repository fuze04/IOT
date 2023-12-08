import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD) //---------for board pins 
//GPIO.setmode(GPIO.BCM) //---------for BCM Pins
ledPin=15
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,False)

try:
    while True:
        GPIO.output(ledPin,True)
        print("LED ON")
        sleep(1)
        GPIO.output(ledPin,False)
        print("LED OFF")
        sleep(1)
finally:
    GPIO.output(ledPin,False)
    GPIO.cleanup()
