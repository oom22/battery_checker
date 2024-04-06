import psutil
import tkinter 
import time
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()


while True:  # Infinite loop to continuously check the battery status
    indicator = psutil.sensors_battery()
    if indicator.power_plugged:  # Check if the battery is charging
        if indicator.percent >= 80:
            # Show the warning if the battery level is 80% or more
            messagebox.showwarning("Battery Warning", "The battery is at 80% or more. Please unplug the charger.")
        time.sleep(1200)  # Wait for 20 minutes (1200 seconds) before checking again
    else:
        time.sleep(300)  # If not charging, wait for 5 minutes (300 seconds) before checking again
        