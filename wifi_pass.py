import subprocess as sb
import re,os
from tkinter import filedialog

path=filedialog.askdirectory()

print(path)
user_wifi=sb.run(['netsh','wlan','show','profiles'],capture_output=True).stdout.decode()
list_of_wifis=re.findall(r'User Profile     : (.*)\r',user_wifi)
infos=dict()
for i in list_of_wifis:
    m=sb.run(['netsh','wlan','show','profile',i,'key=clear'],capture_output=True).stdout.decode()
    ps=re.findall(r'Key Content            : (.*)\r',m)
    infos[i]=ps[0]
with open(path+'/password.txt','w') as file:
    for i in infos:
        x=i+" : "+infos[i]+'\n'
        file.writelines(x)
os.system('msg * Done!')
