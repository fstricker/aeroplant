#aeroplant.py aka main.py
from datetime import datetime
from time import sleep
from stat_summary import *
from process import *
from read import *
import settings
import linecache
import sys
#define more telling exception function
def DetailedException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return f'EXCEPTION IN ({filename}, LINE {lineno} "{line.strip()}"): {exc_obj}'
#initialize variables
sleep(3)
settings.logger('Starting aeroplant session')
print('Starting in...')
for i in range(0,3):
     print(3-i)
     sleep(1)     
settings.init()
#starting data flow
try:
    inputs = serial_flush('/dev/ttyUSB0')
    outputs = serial_flush('/dev/ttyUSB1')
except:
    #write to log
    settings.logger("Aeroplant session couldn't start, error:" + str(DetailedException()))
#
while True:
    try:
        if settings.timestop > datetime.now():
            print('Running interval, collecting data')
            serial_read(inputs, 0)
            serial_read(outputs, 1)        
        else:
            settings.timestop = settings.time_increment(15)
            print('Finishing interval, writing data and starting anew')
            sensors_in = return_stats(settings.dict_in)
            sensors_out = return_stats(settings.dict_out)
            #print(sensors_in)
            #print(sensors_out)
            #
            write_data(sensors_in, sensors_out)
            #reset dictionaries
            for key in settings.dict_keys:
                settings.dict_in[key] = []
                settings.dict_out[key] = []
            continue
    except:
        print(DetailedException())
        #write to log
        settings.logger('Aeroplant session disrupted, error:' + str(DetailedException()))
        break
