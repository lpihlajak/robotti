import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial("COM21")

ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1:
    # get keyboard input
    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
	if input == 'w':
		ser.write("x0,y2%")
	if input == 's':
		ser.write("x0,y0%") 
	if input == 'a':
		ser.write("x-2,y0%")
	if input == 'd':
		ser.write("x0,y-2%")