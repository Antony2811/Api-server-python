import datetime

def get_time1():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")