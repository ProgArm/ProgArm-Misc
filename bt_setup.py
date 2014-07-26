#!/usr/bin/env python
# This is a simple script to configure HC-05 and HM-10 modules
import serial


def chat(sio, str):
    sio.write(str)
    answer = sio.readall()
    print answer
    return answer

# use python -m serial.tools.list_ports to list ports
sio = serial.Serial("/dev/ttyUSB0", 9600, timeout=1) # TODO accept port and baud rate as an argument

if chat(sio, "AT") == 'OK': # Should receive OK from HM-10
    # HM-10
    chat(sio, "AT+RENEW")

    chat(sio, "AT+NAMEProgArm")
    chat(sio, "AT+PASS676869")

    chat(sio, "AT+BAUD2") # 0: 9600 1: 19200 2: 38400 3: 57600 4: 115200
    chat(sio, "AT+STOP0") # 0: one stop bit 1: two stop bits
    chat(sio, "AT+PARI1") # 0: none 1: even 2: odd
else:
    # HC-05
    sio.close()
    sio = serial.Serial("/dev/ttyUSB0", 38400, timeout=1) # TODO accept port and baud rate as an argument

    chat(sio, "AT+ORGL\r\n")
    chat(sio, "AT+VERSION?\r\n")

    chat(sio, "AT+NAME=ProgArm\r\n")
    chat(sio, "AT+PSWD=6869\r\n") # this does not work?

    chat(sio, "AT+UART=38400,0,2\r\n") # 0: one stop bit 1: two stop bits # 0: none 1: odd 2: even

sio.close()
