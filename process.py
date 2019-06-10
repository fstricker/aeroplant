import settings
def dict_populate(text, target):
    '''
    DOCSTRING: Key-value assignments of cleaned string.
    Input: Consumes a string (return object of string_clean()).
    Output: Returns a dictionary with dict_keys and 0:n observations.
    '''
    split_output = [x.strip() for x in text.split(",")] 
    #create key-value list
    keys = []
    values = []
    key_value_pairs = []
    for i in range(0, len(split_output)):
        if i%2 != 0:
            values.append(split_output[i])
        else:
            keys.append(split_output[i])
    #pairing keys and values, !# excess elements will be ignored
    for item in zip(keys, values):
        key_value_pairs.append(item)
    #retain unique observations
    key_value_pairs = list(set(key_value_pairs))
    #populate dictionary from key_value_pairs
    if target == 0:
        for x,y in key_value_pairs:
            for z in settings.dict_in:
                #if keys match, values aren't NaN and positifs: append dictionary
                if x == z and y.lower() != 'nan':
                    if float(y) >= 0:
                        settings.dict_in[z].append(float(y))
    else:
        for x,y in key_value_pairs:
            for z in settings.dict_out:
                #if keys match, values aren't NaN and positifs: append dictionary
                if x == z and y.lower() != 'nan':
                    if float(y) >= 0:
                        settings.dict_out[z].append(float(y))
def string_clean(serial_bytes, target):
    '''
    DOCSTRING: Serial output cleaning.
    Input: Consumes a serial_read() and target info.
    Output: Returns a cleaned string.
    '''
    #stringify
    text = str(serial_bytes[0:len(serial_bytes)-2].decode("utf-8"))
    #F if !checksum: do xyz
    #replace commas at string-start/-end
    if text[0] == ',':
        text = text[1::]
    if text[-1] == ',':
        text = text[0:len(text)-1:]
    #replace colons, tabs, Celsius, % and double commas
    text = text.replace(":", "").replace("\t", "").replace('Celsius,', "").replace(", %,", ",").replace(",,", ",")
    #call dict_populate()
    if target == 0:
        dkey = 0
    else:
        dkey = 1
    dict_populate(text, dkey)