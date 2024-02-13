# BrainHome - Philips Hue

BrainHome x phue 

phue: https://github.com/studioimaginaire/phue

In this project I used phue library for python to code it. 

Features:
-turn on and off all lights, 
-turn on and off chosen light
-set brightness of all lights (100%, 75%, 50%, 25%)
(in this week I plan to add more things)

This app will appear only in your taskbar. As a confirmation on every launch of this app, your light/s will blink to show that the app is active. Once you turn it off it will do the same thing

# How to set it up 

As of now you need to enter your ip on your first launch of the app. Here is a litte tutorial

1. Open ip_huebridge.txt, delete text and enter your Hue bridge IP there (in my case it was 192.168.0.103) REMEMBER IT IS A LOCAL IP NOT A PUBLIC ONE
2. When you open the app the first time you need to go to your Hue bridge and click the button on it to make connection, after that you will no longer have to do this and it will connect automatically
3. (EXTRA STEP) If you want to have it start at the boot of your computer do this. Click Windows key + R and write shell:startup. Then make a shortcut to my app and put it in there. After that you can try it by restarting the computer.

# Errors

1. Wrong IP! Check tutorial for help. - IP set in ip_huebridge.txt is wrong or you didn't change it.
