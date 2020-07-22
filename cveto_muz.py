import serial #Serial imported for Serial communication
import time #Required to use delay functions
import traceback
ser = serial.Serial('COM12',9600) #подключение к ардуино
time.sleep(2)
#print ArduinoSerial.readline() чтение с ардуино
print ('Enter 1 to turn ON LED and 0 to turn OFF LED')
for i in range(20):
    ser.write(b'q')
    time.sleep(0.5)
    ser.write(b'w')
    time.sleep(0.5)
    ser.write(b'e')
    time.sleep(0.5)
    ser.write(b'w')
    time.sleep(0.5)
    ser.write(b'e')
    time.sleep(0.5)
    ser.write(b'q')
    time.sleep(0.5)
    ser.write(b'e')
    time.sleep(0.5)
    
