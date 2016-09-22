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
    a = time.time()
    if x == "b'Start\r\n'":        
        print(x + "Timing Initiated")            
    elif x == b'Stop\r\n':
        b = time.time()
        print("RACE is OVER STOP")
        elapsed_time = a - b
        print("Elapsed time: " + str(elapsed_time))
        sys.exit(0)
    
    
        
