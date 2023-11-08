import re
import datetime
import numpy as np

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_times = [line.split()[0] for line in races if "Jennifer Rhines" in line]
    return rhines_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    # Convert times to milliseconds
    minutes = [(int(time.split(':')[0])*3600000) for time in racetimes]
    seconds_periods = [(time.split(':')[1]) for time in racetimes]
    seconds = [(int(time.split('.')[0])*60000) for time in seconds_periods]
    sub_total = [a+b for a,b in zip(minutes, seconds)]
    milliseconds = []
    for milli in racetimes:
        if ('.' in milli):
            milliseconds.append(int(milli.split('.')[1]))
        else:
            milliseconds.append(0)
    total = [a+b for a,b in zip(sub_total, milliseconds)]
    # Calculate average
    average = np.average(total)
    # Convert back to mm:ss:M format
    minutes, remainder = divmod(average, 3600000)
    seconds, milli_remainder = divmod(remainder, 60000)
    milliseconds = divmod(milli_remainder, 1000)[0] 
    return f"{int(minutes)}:{int(seconds)}:{int(milliseconds)}"

print(get_average())
get_average()