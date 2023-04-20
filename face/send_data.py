# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM10', baudrate=9600, timeout=1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    line = arduino.readline()   # read a byte
    if line:
        string = line.decode()
        # id = string.decode('ascii')
        print(string)
    num = input("Enter a number: ") # Taking input from user
    # time.sleep(1)
    value = write_read(num)
    print(value) # printing the value
    