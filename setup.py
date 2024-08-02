import os, platform, time, sys
print('\n\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
print('\x1b[38;5;208mNote \033[1;31m:\x1b[38;5;48m When setup is done, You see SetUp done msg')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m You are 64 Bit user')
 time.sleep(3)
 os.system("clear") 
 import set
elif bit == '32bit':
 print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m You are 32 Bit user')
 time.sleep(3)
 os.system("clear")
 import setup
