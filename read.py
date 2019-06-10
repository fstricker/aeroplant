import serial
from process import string_clean

def serial_flush(port, baud_rate = 9600):
    '''
    DOCSTRING: Arduino data preparation for serial ports.
    Inputs: Mandatory [port] is USB serial port which is either /dev/ttyUSB0 or /devttyUSB1. Optional [baud_rate] which is the symbol rate and depends on Arduino side. Therefore defaulted to standard 9600.
    Output: Flushes the USB port and target info.
    '''
    #select and flush port
    serial_port = serial.Serial(port)
    serial_port.flushInput()
    return serial_port
    
def serial_read(port, destination):
    '''
    DOCSTRING: Data collection from serial ports.
    Inputs: Flushed serial port and destination info.
    Output: Calls string_clean().
    '''
    #read line-by-line
    serial_bytes = port.readline()
    #call string_clean()
    target = destination
    #print(serial_bytes)
    string_clean(serial_bytes, target)