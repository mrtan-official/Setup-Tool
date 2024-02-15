import os, platform, time, sys
print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m 64 Bit Found')
 print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;48m\n')
 time.sleep(3)
 os.system("clear") 
 import set
elif bit == '32bit':
 print('\033[1;31m[\x1b[38;5;48m●\033[1;31m]\x1b[38;5;48m 32 Bit Found')
 print('\033[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;48m\n')
 time.sleep(3)
 os.system("clear")
 import setup
