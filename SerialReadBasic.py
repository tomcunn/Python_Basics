import serial
import os


ser = serial.Serial('COM3', 115200, timeout=10)
ser.flushInput()
ser.flushOutput()


text_file = open("./position4.txt", 'a')

while True:
	dataString = ser.readline()
	print (dataString)
	text_file.write(str(dataString) + '\n')
	text_file.flush()