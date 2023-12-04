from microbit import *
import radio

radio.config(channel=18) #remember to change this channel number
radio.config(length=250)
radio.on()

print('## pyRC - Python Relay Chat ##')
print('Microbit Edition')
print('Press (A) to transmit')

while True:
    rx = radio.receive()
    if rx:
        print(rx)
    if button_a.was_pressed():
        print('Enter message to transmit')
        tx = input()
        radio.send(tx)
        print('Sent!')
        print('Press (A) to transmit')
        


