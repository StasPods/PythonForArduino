import serial #Serial imported for Serial communication
import time #Required to use delay functions
import traceback
ser = serial.Serial('COM12',9600) #подключение к ардуино
time.sleep(2)
#print ArduinoSerial.readline() чтение с ардуино
print ('Enter 1 to turn ON LED and 0 to turn OFF LED')
received = []
var = input()
while var!="o": #Do this forever
    var = input()
    print ("you entered", var)
    if (var == 'q'):
        ser.write(b'q') #отправить в ардуино в виде байт кода
        print ("LED turned sel")
        time.sleep(1)
    if (var == 'w'):
        ser.write(b'w')
        print ("LED turned red")
        time.sleep(1)
    if (var == 'e'):
        ser.write(b'e')
        print ("LED turned OFF")
        time.sleep(1)
    if ser.inWaiting() > 0:
        line = ser.readline()
        if line:
            received.append(line.decode().strip())
print(received)
