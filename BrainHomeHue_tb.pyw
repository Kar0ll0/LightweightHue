from phue import Bridge
import time
import os
import random
import pystray
import PIL.Image
#checking system for clear cmd
if os.name in ('nt', 'dos'):
    command = 'cls'
else:
    command = 'clear'
#===
def clearcmd():
    os.system(command)

image = PIL.Image.open('Assets/hueon.ico') #error with opening add whole dict


def turn_on_all_back(icon, item):
    for l in lights:
        l.on = True
    image = PIL.Image.open('hueon.ico')
def turn_off_all_back(icon, item):
    for l in lights:
        l.on = False
    image = PIL.Image.open('hueoff.ico')
def party_mode_back(icon, item):
    print('PARTY MODEE!')
    i=0
    for light in lights_list:
        while i != 15:
            light.hue = random.randint(0, 20000)
            time.sleep(0.5)
            i = i + 1
def blink_mode(icon, item):
    for l in lights:
        l.on = True
        time.sleep(1)
        l.brightness = 20
        time.sleep(0.5)
        l.brightness = 254

    
def exit_background(icon, item):
    icon.stop()

def on_clicked(icon, item):
    print('button works')

icon = pystray.Icon('LightweightHue', image, menu=pystray.Menu(
    pystray.MenuItem('Turn on ALL', turn_on_all_back),
    pystray.MenuItem('Turn off ALL', turn_off_all_back),
    pystray.MenuItem('Blink', blink_mode),
    pystray.MenuItem('Exit', exit_background)
))


#getting the ip from text
f= open("ip_huebridge.txt", "r+")
ip_bridge = str(f.read())
b = Bridge(ip_bridge)
##########################

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()


# Prints if light 1 is on or not

# Get a dictionary with the light id as the key

lights_list = b.get_light_objects('list')
light_names = b.get_light_objects('name')
lights = b.lights

light_names['Led'].on = True
time.sleep(1)
#startup seq
def startup():
    for l in lights:
        l.brightness = 20
        time.sleep(0.5)
        l.brightness = 254


def turn_on_all():
    for l in lights:
        l.on = True
def turn_off_all():
    for l in lights:
        l.on = False
def party_mode():
    print('PARTY MODEE!')
    i=0
    for light in lights_list:
        while i != 15:
            light.hue = random.randint(0, 20000)
            time.sleep(0.5)
            i = i + 1

startup()
icon.run()
startup()
clearcmd()