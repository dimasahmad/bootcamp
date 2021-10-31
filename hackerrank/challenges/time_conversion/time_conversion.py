# time conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

def time_conversion(time: str) -> str:
    # 12:05:45PM
    # hh:mm:sspp
    hh: str = time[:2]
    mm: str = time[3:5]
    ss: str = time[6:8]
    pp: str = time[-2:]

    # 12:00:00AM => 00:00:00
    if(pp == "AM" and hh == "12"):
        hh = "00"

    # 12:00:00PM => 12:00:00
    # 01:00:00PM => 13:00:00
    elif(pp == "PM" and hh != "12"):
        hh = str(int(hh) + 12)

    return f"{hh}:{mm}:{ss}"
