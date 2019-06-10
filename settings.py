#settings.py
#load dependecies
from csv import writer
from datetime import datetime, timedelta
import os.path
import logging
#
def time_increment(time_input):
    '''
    DOCSTRING: Function to set future timestamp
    Input: Minutes (Float or int)
    Ouput: datetime.datetime object
    '''
    return datetime.now() + timedelta(minutes = time_input)
def init():
    '''
    DOCSTRING: Definition of global and local variables. Use case build and change global variables from importing modules.
    Input: Global and local variables.
    Output: .csv and globally accessible variables using import.
    '''
    #F add % humidity and celsius temp
    cols = ['PM_1.0', 'PM_2.5', 'PM_10', 'Humidity', 'Temp', 'MICS_VOC_PPB', 'MICS_CO2_PPM']
    #define dictionary
    global dict_in
    global dict_out
    dict_in = {}
    dict_out = {}
    global dict_keys
    dict_keys = [x.replace("_", " ") for x in cols]
    for key in dict_keys:
        dict_in[key] = []
        dict_out[key] = []
    #metrics
    stats = ['_Mean', '_Min', '_Max']
    stat_cols = []
    for i in cols:
        for j in stats:
            stat_cols.append(i + j)
    in_cols = [x + '_In' for x in stat_cols]
    out_cols = [x + '_Out' for x in stat_cols]
    #define future timestamp
    global timestop
    timestop = time_increment(0.2)
    #target_file
    global inandout_file
    inandout_file = "/home/pi/aeroplant_1.0/aeroplant.csv"
    #check whether .csv to be created
    if not os.path.isfile(inandout_file):
        print(f"Creating {inandout_file}")
        with open(inandout_file,"w") as o:
            out_writer = writer(o,delimiter=",")
            out_writer.writerow(['Timestamp'] + in_cols + out_cols)
            o.close()
    else: 
        print(f"{inandout_file} already created")
    #create log
    #global protocol_file
    protocol_file = '/home/pi/aeroplant_1.0/protocol.log'
    if not os.path.isfile(protocol_file):
        logging.basicConfig(filename=protocol_file,level=logging.DEBUG)
        logging.info('This is a log of aeroplant performance')        
#populate log function
def logger(payload):
    '''
    DOCSTRING: Logs start and end of each aeroplant session.
    Input: None.
    Output: Log entry.
    '''
    logging.basicConfig(filename = '/home/pi/aeroplant_1.0/protocol.log', level = logging.DEBUG)
    logging.info(str(datetime.now()) +':' + payload)