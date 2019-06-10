#load dependencies
from csv import writer
from datetime import datetime
import settings
#
def write_data(inputs, outputs):
    '''
    DOCSTRING: Collation of sensor in- and outputs.
    Inputs: Lists of metric tuples.
    Output: List.
    '''
    payload = [str(datetime.now())]
    with open(settings.inandout_file,"a") as o:
        out_writer = writer(o,delimiter=",")
        out_writer.writerow(payload + inputs + outputs)
        o.close()
#
def return_stats(adict):
    '''
    DOCSTRING: Calculation of min, max, mean.
    Input: Dictionary.
    Output: List.
    '''
    #container list for metric tuples
    line_tuples = []
    #line
    line_input = []
    #F keys = adict.keys()
    #F means = [mean(adict[x]) if adict[x] != [] else None for x in adict]
    means = [sum(adict[x])/len(adict[x]) if adict[x] != [] else None for x in adict]
    minima = [min(adict[x]) if adict[x] != [] else None for x in adict]
    maxima = [max(adict[x]) if adict[x] != [] else None for x in adict]
    #zip() along keys
    for item in zip(means, minima, maxima):
        line_tuples.append(item)
    #concatenate
    for i in range(0, len(line_tuples)):
        line_input += list(line_tuples[i])
    return line_input