import time
import sys
import serial

"""initialise port"""
ser = serial.Serial(port='COM3',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=12)


while True:
    x = ser.readline()
    
    if x == "b'Start\r\n'":        
        print(x + "Timing Initiated")
        a = time.time()
    elif x == b'Stop\r\n':
       
        print("Timing Stoped")
        
        print("Elapsed time: " + str(a))
        sys.exit(0)
    
    
        
