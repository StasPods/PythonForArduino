import serial #Serial imported for Serial communication
import time #Required to use delay functions
import traceback
ser = serial.Serial('COM9',9600) #подключение к ардуино
time.sleep(2)
#print ArduinoSerial.readline() чтение с ардуино
print ('Enter 1 to turn ON LED and 0 to turn OFF LED')
while 1: #Do this forever
    var = input() 
    print ("you entered", var) 
    if (var == 'e'): 
        ser.write(b'e') #отправить в ардуино в виде байт кода
        print ("LED turned ON")
        time.sleep(1)
    if (var == 'd'): 
        ser.write(b'd') 
        print ("LED turned OFF")
        time.sleep(1)
