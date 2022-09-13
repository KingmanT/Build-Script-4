# import subprocess
## need to convert HH:MM:SS AM/PM to HH:MM:SS (24)

time = "10:32:38 PM"
# print(time)
# command = "echo (time)"
# subprocess.call(command, shell=True)
# x = time.split()[0]
# print(x)
if time.split()[1] == "PM":
    hour = time.split()[0]
    # print(hour)
    hh = int(hour.split(':')[0])
    hhh = str(hh + 12) 
    # print(hhh)
    print(hhh + ":" + hour.split(':')[1] + ":" + hour.split(':')[2])
    


elif time.split()[1] == "AM":
    print(time.split[0])
