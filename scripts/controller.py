import RPi.GPIO as GPIO
import time
import sys

pin_list = []

kette_1 = "7"
kette_2 = "11"
kette_3 = "12"

GPIO.setmode(GPIO.BOARD)


max_Farbe = int(21)

def trigger_farbe(farbe):
    file = open("farbe.txt","r")
    cache = str(file.read())
    aktuelle_Farbe_list = cache.split(",")
    for pin in pin_list:
        if str(pin) == str(kette_1):
            aktuelle_Farbe = int(aktuelle_Farbe_list[0])
        elif str(pin) == str(kette_2):
            aktuelle_Farbe = int(aktuelle_Farbe_list[1])
        elif str(pin) == str(kette_3):
            aktuelle_Farbe = int(aktuelle_Farbe_list[2])

        if(aktuelle_Farbe > farbe):
            for i in range(aktuelle_Farbe, max_Farbe):
                trigger_schalten(pin)
            aktuelle_Farbe = 0

        for i in range((farbe - aktuelle_Farbe)):
            trigger_schalten(pin)
            print("trig")
    file.close()
    if pin == int(kette_1):
        aktuelle_Farbe_list[0] = farbe
        print("change 1")
    elif pin == int(kette_2):
        aktuelle_Farbe_list[1] = farbe
        print("change 2")
    elif pin == int(kette_3):
        print("change 3")
        aktuelle_Farbe_list[2] = farbe
    file = open("farbe.txt","w")
    file.write(str(aktuelle_Farbe_list[0]) + "," + str(aktuelle_Farbe_list[1]) + "," + str(aktuelle_Farbe_list[2]))
    file.close()

def trigger_schalten(pin):
    GPIO.output(pin,True)
    time.sleep(0.025)
    GPIO.output(pin,False)
    time.sleep(0.025)


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
    print(farbe)
    if(farbe > max_Farbe):
        print("Die Farbe " + str(farbe) + " existiert nicht!")
    elif(farbe == -1):
        print("trigger Blink")
        trigger_blink()
    else:
        print("trigger_farbe")
        trigger_farbe(farbe)

GPIO.cleanup()
