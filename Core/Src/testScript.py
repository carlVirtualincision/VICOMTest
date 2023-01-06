import serial
from serial import PARITY_MARK, PARITY_SPACE, PARITY_NONE, PARITY_EVEN, PARITY_ODD
import random
import time



ser = serial.Serial("COM7", 3000000)

def write(msg, parity):
    if parity == 0:
        ser.parity = PARITY_SPACE
    elif parity == 1:
        ser.parity = PARITY_MARK
    ser.flush()
    ser.write(bytes(msg))
    ser.flush()

crcPoly = 0xA001
crcTable = [None] * 256

def crcInit():
    value = 0
    temp = 0
    for i in range(256):
        value = 0
        temp = i
        for j in range(8):
            if(((value ^ temp) & 0x0001) != 0):
                value = (value >> 1) ^ crcPoly
            else:
                value >>= 1
            
            temp >>= 1

        crcTable[i] = value


def crcCompute(inputBytes):
    crc = 0
    for i in range(len(inputBytes)):
        index = (crc ^ inputBytes[i]) & 0xFF
        crc = (crc >> 8) ^ crcTable[index]

    return crc


# setpointList = [0, 60, 180, 360, 150, 80]
# oldSetpoint = 0
setpointChoice = 0
direction = 0

crcInit()

while True:

    # direction = 0 if setpointChoice < 720 else 1

    # if(direction == 0):
    #     state.joint1.setpoint = setpointChoice
    #     state.joint2.setpoint = setpointChoice
    #     setpointChoice += 10

    # else:
    #     state.joint1.setpoint = setpointChoice
    #     state.joint2.setpoint = setpointChoice
    #     setpointChoice -= 10


    # oldSetpoint = setpointChoice
    # setpointChoice = random.choice(setpointList)
    # if(setpointChoice != oldSetpoint):

    #     # motorSetpoint = input()

    #     try: 

    #         state.joint2.setpoint = int(setpointChoice)
    #         state.joint1.setpoint = int(setpointChoice)

    #         # time.sleep(5)

    #     except Exception as x:
    #         print(x)
            
    #         pass

    # payloadLen = len(state.SerializeToString())

    # # headerCRC = calculator.checksum(bytes([5, payloadLen]))
    # headerCRC = crcCompute(bytes([5, payloadLen]))

    # print(hex(headerCRC & 0xff))
    # print(hex((headerCRC >> 8) & 0xFF))

    # payloadCRC = calculator.checksum(bytes(state.SerializeToString()))
    # payloadCRC = crcCompute(bytes(state.SerializeToString()))

    x = 65
    write([x], 1)
    # write([len(state.SerializeToString())], 0)
    # write([headerCRC & 0xff], 0)
    # write([(headerCRC >> 8) & 0xFF], 0)

    
    # write(state.SerializeToString(), 0)
    # # ser.write(state.SerializeToString())
    # # ser.flush()

    # write([payloadCRC & 0xff], 0)
    # write([(payloadCRC >> 8) & 0xFF], 0)

    # print(hex(payloadCRC & 0xff))
    # print(hex((payloadCRC >> 8) & 0xFF))

    # print("Moving to setpoint : " , setpointChoice)
    # time.sleep(2)