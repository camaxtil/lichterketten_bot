import RPi.GPIO as GPIO
import time
import sys

pin_list = []

GPIO.setmode(GPIO.BOARD)


max_Farbe = int(21)

def trigger_farbe(farbe):
    file = open("farbe.txt","r")
    aktuelle_Farbe = int(file.read())
    
    if(aktuelle_Farbe > farbe):
        for i in range(aktuelle_Farbe, max_Farbe):
            trigger_schalten()
        aktuelle_Farbe = 0

    for i in range((farbe - aktuelle_Farbe)):
        trigger_schalten()

    file.close()
    aktuelle_Farbe = farbe
    file = open("farbe.txt","w")
    file.write(str(aktuelle_Farbe))
    file.close()

def trigger_schalten():
    for pin in pin_list:
        GPIO.output(pin,True)
    time.sleep(0.025)
    for pin in pin_list:
        GPIO.output(pin,False)


def trigger_blink():
    for pin in pin_list: 
        GPIO.output(pin,True)
    time.sleep(2)
    for pin in pin_list:
        GPIO.output(pin,False)


if __name__ == "__main__":
    
    for i in range(2,len(sys.argv)):
        x = int(sys.argv[i])
        GPIO.setup(x,GPIO.OUT)
        pin_list.append(x)
    
    farbe = int(sys.argv[1])
    if(farbe > max_Farbe):
        print("Die Farbe " + str(farbe) + " existiert nicht!")
    elif(farbe == -1):
        print("trigger Blink")
        trigger_blink()
    else:
        print("trigger_farbe")
        trigger_farbe(farbe)


GPIO.cleanup()
