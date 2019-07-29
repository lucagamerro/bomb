import os 
from time import sleep

print("[*] Run this program as root.")
print("[*] Installing dependece...")
try:
    os.system('sudo pip3 install pyinstaller | grep "Successfully installed"')
except:
    print("[!] Error installing pyinstaller, try again.")
    exit()

try:
    os.system("sudo apt-get install npm")
    os.system("sudo npm install --global surge")
except:
    print("[!] Error installing surge, try again.")
    exit()

try:
    print("\n [*] Now login into your surge accoun and leave the lines below white.")
    os.system("surge")
except:
    print("[!] Login falied, try again.")
    exit()

try:
    bash = open("/home/luke/.bash_aliases", "a")
    bash.write("\n \n alias bomb='cd bomb && python3.7 bomb.py'")
    bash.close()
except:
    print("[!] Somtings don't work, try again.")
    exit()

print("[*] All done.")
print('[*] Now type "bomb" and enjoy the programm!')
sleep(1)
exit()