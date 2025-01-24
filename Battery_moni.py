# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:47:22 2024

@author: Ayobami Adeyemo
"""

import psutil
import time
import os

def battery_alert():
    while True:
        battery = psutil.sensors_battery()  # Update battery status inside the loop

        if battery.percent == 100 and battery.power_plugged:  # Check if battery is full and still plugged
            print("Battery is fully charged! Please unplug the charger.")
            
            # Optionally, play a sound when battery is 100% charged
            # For MacOS:
            # os.system('say "Battery is fully charged"')
            
            # For Linux:
            # os.system('spd-say "Battery is fully charged"')
            
            # For Windows:
            os.system('powershell [console]::beep(1000,500)')
            os.system('Kizz_Daniel_-_MarHaba.mp3')
            
            break
        
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    battery_alert()



    