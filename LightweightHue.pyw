from phue import Bridge
import time
import os
import random
import pystray
import PIL.Image
import ctypes
#import easygui as e
#from easygui import *
#import tkMessageBox
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
def turn_off_all_back(icon, item):
    for l in lights:
        l.on = False
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
def half_brightness(icon, item):
    for l in lights:
        l.brightness = 127
    icon.notify("Brightness is set to 50%", title="LightweightHue")
def max_brightness(icon, item):
    for l in lights:
        l.brightness = 254 
    icon.notify("Brightness is set to 100% ", title="LightweightHue")
def quarterbrightness(icon, item):
    for l in lights:
        l.brightness = 63
    icon.notify("Brightness is set to 25%", title="LightweightHue")
def seven_brightness(icon, item):
    for l in lights:
        l.brightness = 190
    icon.notify("Brightness is set to 75%", title="LightweightHue")


def exit_background(icon, item):
    icon.stop()

def on_clicked(icon, item):
    print('button works')

icon = pystray.Icon('LightweightHue', image, menu=pystray.Menu(
    pystray.MenuItem('Turn on ALL', turn_on_all_back),
    pystray.MenuItem('Turn off ALL', turn_off_all_back),
    pystray.MenuItem('Blink', blink_mode),
    pystray.MenuItem("100% Brightness", max_brightness),
    pystray.MenuItem("75% Brightness", seven_brightness),
    pystray.MenuItem("50% Brightness", half_brightness),
    pystray.MenuItem("25% Brightness", quarterbrightness),
    pystray.MenuItem('Exit', exit_background)
))


#getting the ip from text
f= open("ip_huebridge.txt", "r+")
ip_bridge = str(f.read())
if ip_bridge == "delete this and write your Hue bridge local ip here (you can find it in the Hue app on smartphone)":
    print("works")
#    e.msgbox("Wrong IP! Check tutorial for help", "Error")
    ctypes.windll.user32.MessageBoxW(None, "Wrong IP! Check tutorial for help", "Error", 0)
    quit()
else:
    pass


b = Bridge(ip_bridge)
##########################

# Connecting the Bridge for the first time
b.connect()

# Check Bridge status
b.get_api()

# Get a dictionary with the light id as the key

lights_list = b.get_light_objects('list')
light_names = b.get_light_objects('name')
lights = b.lights

light_names['Led'].on = True
time.sleep(1)
# startup seq
def startup():
    for l in lights:
        l.brightness = 20
        time.sleep(0.5)
        l.brightness = 254
#################


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


#app
startup()
icon.run()
startup()
clearcmd()