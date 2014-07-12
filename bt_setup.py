#!/usr/bin/env python
import serial
from serial import SerialException

sio = serial.Serial("/dev/ttyUSB0", 9600)

#TODO would this even work?

def chat(sio, str):
    sio.write(str + "\r\n")
    print sio.readline()

chat(sio, "AT+RENEW")
chat(sio, "AT+VER?")

chat(sio, "AT+NAMEProgArm")
chat(sio, "AT+PIN1234")

chat(sio, "AT+BAUD2") # 0: 9600 1: 19200 2: 38400 3: 57600 4: 115200
chat(sio, "AT+STOP0") # 0: one stop bit 1: two stop bits
chat(sio, "AT+PARI1") # 0: none 1: even 2: odd
