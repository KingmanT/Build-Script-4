#!/usr/bin/python3

sunsetutc = "10:33:36 AM"

# if sunsetutc.split()[1] == "PM":
#     hour = sunsetutc.split()[0]
#     # print(hour)
#     hh = int(hour.split(':')[0])
#     if hh == 12:
#         hh24 = str(12)
#     else:
#         hh24 = str(hh + 12) 
#         # print(hh24)
#     sunset24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
#     print(sunset24)

if sunsetutc.split()[1] == "AM":
    hour = sunsetutc.split()[0]
    hh = int(hour.split(":")[0])
    if hh == 12:
        hh24 = "00"
        sunset24 = hh24 + ":" + hour.split(':')[1] + ":" + hour.split(':')[2]
    else:
        sunset24 = sunsetutc.split()[0]
    print(sunset24)