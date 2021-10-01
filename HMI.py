import RPi.GPIO as GPIO
from time import sleep
import os
import sys


outPin = 23

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(outPin, GPIO.OUT) # LED pin set as output
GPIO.output(outPin, 0) # set light to off

pin = '7319'
answers = [
    ['SWJOMDNCET', 'N'],
    ['VJBUPEOSTH', 'B'],
    ['QVJOHCGPUE', 'G'],
    ['AUVESCFWTJ', 'A'],
    ['ECFLTMKQJD', 'L'],
    ['OMUCQDJTHF', 'R'],
    ['CHKMJODSVX', 'X'],
    ['EJVMHOICUF', 'I'],
    ['PQHUZVKFEC', 'Z'],
    ['FKUDCPYEVW', 'Y'],
]
position = 0
user_input = ''

while user_input != pin:
    user_input = input('ENTER PIN TO BEGIN ABORT SEQUENCE: ')

while position < len(answers):
    user_input = input(f'{answers[position][0]}: ')
    if user_input.lower() == answers[position][1].lower():
        position += 1
    else:
        position = 0

print('SHUTDOWN SEQUENCE ACTIVATED')

GPIO.output(outPin, 1)
sleep(2)
os.execl(sys.executable, sys.executable, *sys.argv)



#def restart():
#    command = "/usr/bin/sudo /sbin/shutdown -r now"
#    import subprocess
#    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#    output = process.communicate()[0]
#    print (output)
#    
#restart()
    
    
