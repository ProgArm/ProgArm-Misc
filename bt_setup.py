#!/usr/bin/env python
# This is a simple script to configure HM-10 modules
import serial


def chat(sio, str):
    sio.write(str)
    print sio.readall()

# use python -m serial.tools.list_ports to list ports
sio = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5) # TODO accept port and baud rate as an argument

chat(sio, "AT") # just a test. Should receive OK in response

chat(sio, "AT+RENEW")

chat(sio, "AT+NAMEProgArm")
chat(sio, "AT+PASS676869")

chat(sio, "AT+BAUD2") # 0: 9600 1: 19200 2: 38400 3: 57600 4: 115200
chat(sio, "AT+STOP0") # 0: one stop bit 1: two stop bits
chat(sio, "AT+PARI1") # 0: none 1: even 2: odd

sio.close()
