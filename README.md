# Toblerone-Wifi-Tool
This is a GUI of AirCrack and some other tools that makes handshake capture a bit easier 

If you do not fully understand something using this program, then this tool is not  for you. Refer to the laws in your province/country before accessing, using, or in any other way utilizing this program.

These materials are for educational and research purposes only.

Do not attempt to violate the law with anything contained here. If this is your intention, CLOSE THE PROGRAM! Neither the author of this material, or anyone else affiliated in any way, is going to accept responsibility for your actions.

We do NOT promote Hacking! We are documenting the way hackers steal and performs activities. So it can be useful to Protect yourself.
------------------------------------------------------------------------------------

Dependacies
------------------
htop
xterm
aircrack-ng
cowpatty

htop
----
opens a xterm window that has htop task-manager

iwconfig
--------
shows you the names of interfaces
helps to find your wireless card to config
shows what mode the wireless adapter is in (moniter or managed)

iwconfig
--------
shows you the names of interfaces
helps to find your wireless card to config
shows what mode the wireless adapter is in (moniter or managed)

interface monitor
-----------------
sets the network card to moniter mode by the commands
$ ifconfig <interface> down
$ iwconfig <interface> mode moniter
$ ifconfig <interface> up
then uses airoplay-ng to check if interface is in moniter mode and injection


handshake
---------
Opens the scanning and packet capture menu

how to capture a handshake
--------------------------

1) click on scan all a window will pop up with connections let it run for 2 to 3 mins, then close the window(what it is doing is writing the data to the text file. the longer you have it open the more data that will be written)

2) click on select target. a window will popup and ask you to select a csv. this csv is what you scanned for in the prevous step. its name will be "groupCapture-01.csv" but if you have scanned more then once, then the file will increment the number(groupCapture-02.csv) the bigger number is the most recent scan. After you choose your file a second window will pop up with all the ssid's that you scanned for in the first button. CHOOSE the ssid that you want to target. click select target to save the target data. 	WHEN WINDOW CLOSES IT SAVED YOUR CHOICE

3) Once the target is selected, click on start scan. this calls a more refined search with only your target. KEEP THE WINDOW OPEN UNTILL YOU SEE A MAC ADDRESS UNDER STATION TAG OR NEXT STEP WONT WORK. If

4) click on select station. a window will popup and ask you to select a csv. this csv is what you were scanning for in the prevous step. its name will be "targetCapture-01.csv" but if you have scanned more than once, then the file will increment the number(targetCapture-02.csv). the bigger the number, the more recent the scan. After you choose your file a second window will pop up with all the stations that you were scanning for in the last step. IF IT IS BLANK THAT MEANS THERE IS NO STATION TO BE TARGETED IN A SCAN, OR THAT ROUTER DOES'NT HAVE ANY CONNECTED DEVICES. select a new target. WHEN THE WINDOW CLOSES, IT SAVED YOUR CHOICE.
if you have the station selected then move to deauth button

5) just click on deauth. if all previous steps worked as they should, you should see the target lose connection.
WAIT till you see "HANDSHAKE CAPTURED" on the top of the target scan window. if you closed that window start from step 3 and start again. When you have both the windows up, and you see "HANDSHAKE CAPTURED", you can close the target scan window. you have captured the handshake. GOOD JOB.

6) Once you have capture the handshake choose the check handshake option. It will have you pick a  .cap file to check if the handshake is complete. YOU NEED TO PICK THE TARGETCAPTURE.CAP, this is where the handshake is
When you choose the cap file that you want a program named cowpatty will check if you have all the necessary data for the handshake
When you choose the cap file that you want a program named cowpatty will check if you have all the necessary data for the handshake
After you have selected the cap file that u want. The program will open up a second file picker that lets you pick a wordlist to put aginst the cap file to crack.
Once you have picked both files aircrack will start up and try to crack the handshake. This process could take 5mins to days depending on the strength of the password and or if your wordlist has their password in it youj just have to keep trying.
