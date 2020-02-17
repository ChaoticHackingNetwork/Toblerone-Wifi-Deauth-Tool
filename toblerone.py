#all button width = 19
from tkinter import *
import tobleroneMethods as tm

root = Tk()
instructionList =[]

def instructions():
    top2 = Toplevel()

    #TODO
    #make a text and read it into list that has all the instructions
    #read it into memory
    #display it on the screen
    
    top2.title("Instructions")
    instruction1 = Label(top2, text='OPTIONS').grid(row=0, column=0)

#second window 
def HandshakeOpen():
    top = Toplevel()

    top.title("TOBLERONE HANDSHAKE")

    lblTitle1 = Label(top, text='OPTIONS', fg='light green', background='black').grid(row=0, column=0)
    lblTitle1 = Label(top, text='Details', fg='light green', background='black').grid(row=0, column=1)

    scanGroup = Button(top, text='Scan All', command=tm.groupDumpStart, width=19).grid(row=1, column=0)  
    lbl7 = Label(top, text="Scan Nearby Routers").grid(sticky="w", row=1, column=1)

    selectTarget = Button(top, text='Select Target', command=tm.targetedAiroDumpStart, width=19).grid(row=2, column=0)
    lbl8 = Label(top, text="Select target(group.csv)").grid(sticky="w", row=2, column=1)

    startScan = Button(top, text='Start Scan', command=tm.targetedAiroDumpStart1, width=19).grid(row=3, column=0)
    lbl9 = Label(top, text="Scan target").grid(sticky="w", row=3, column=1)

    station = Button(top, text='Select Station', command=tm.stationSelect, width=19).grid(row=4, column=0)
    lbl10 = Label(top, text="select station(target.csv)").grid(sticky="w", row=4, column=1)

    deauth = Button(top, text='Deauth', command=tm.deauth, width=19).grid(row=5, column=0)
    lbl11 = Label(top, text="Deauth").grid(sticky="w", row=5, column=1)

    checkHand = Button(top, text='Check Hanshake', command=tm.checkForHandshake, width=19).grid(row=6, column=0)
    lbl12 = Label(top, text="Check if complete handshake").grid(sticky="w", row=6, column=1)

    crack = Button(top, text='crack', command=openCracker, width=19).grid(row=7, column=0)
    lbl13 = Label(top, text="Open Crack Menu").grid(sticky="w", row=7, column=1)



def openCracker():
    top1 = Toplevel()

    top1.title("TOBLERONE Cracking")

    lblTitle3 = Label(top1, text='OPTIONS', fg='light green', background='black').grid(row=0, column=0)
    lblTitle4 = Label(top1, text='Details', fg='light green', background='black').grid(row=0, column=1)

    useAir = Button(top1, text='use Aircrack', command=tm.useAireC, width=19).grid(row=1, column=0)
    lbl13 = Label(top1, text="Crack CAP").grid(sticky="w", row=1, column=1)


#main application

root.title("TOBLERONE")

lblTitle = Label(root, text='OPTIONS', fg='light green', background='black').grid(row=0, column=0)
lblTitle = Label(root, text='Details', fg='light green', background='black').grid(row=0, column=1)

btnHtop = Button(root, text='htop', command=tm.htop, width=19).grid(row=2, column=0)
lbl = Label(root, text="Open Task-Manager").grid(sticky="w", row=2, column=1)

checkIf = Button(root, text='iwconfig', command=tm.ifConfig, width=19).grid(row=3, column=0)
lbl1 = Label(root, text="Veiw Interfaces").grid(sticky="w", row=3, column=1)

btnEditConfig = Button(root, text='Edit Config', command=tm.editConfig, width=19).grid(row=4, column=0)
lbl2 = Label(root, text="Configure Interface").grid(sticky="w", row=4, column=1)

interfaceMoniter = Button(root, text='Interface Moniter', command=tm.toMoniter, width=19).grid(row=5, column=0)
lbl3 = Label(root, text="set interface to default").grid(sticky="w", row=5, column=1)

interfaceManaged = Button(root, text='Interface Managed', command=tm.toManaged, width=19).grid(row=6, column=0)
lbl4 = Label(root, text="set interface to moniter mode").grid(sticky="w", row=6, column=1)

handShake = Button(root, text='Handshake', command=HandshakeOpen, width=19).grid(row=7, column=0)
lbl5 = Label(root, text="WPA2 Capture").grid(sticky="w", row=7, column=1)

mainloop()


