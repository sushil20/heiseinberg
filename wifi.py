import subprocess
#import wifi
devices=subprocess.check_output(['netsh','wlan','show','network'])
devices=devices.decode('ascii')
devices=devices.replace("\r"," ")
ssid=devices.split("\n")
#ssid is a network name or it is a seq of char
#it allows to connect desired network
ssid=ssid[4:] #ssid=service set identifier
ssids=[]
x=0
while x<len(ssid):
    if x%5==0:
        ssids.append(ssid[x])
        x+=1
        print(ssids)
