# Mitchell Haride
# Date: 26/03/19
# Time: 21:00

#Phone Information
# Name = Samsung Galaxy J4+
# Resolution = 720x1480
# Aspect Ratio = 18.5:9

import tkinter as tk
import time
import sys
from client import Client
from phone_gui import PhoneGui

LARGE_FONT = ("roboto", 16)

def main():
    global clock
    try:
        connection = Client()
        connection.download_data()
    except:
        print("Cannot connect")
    mainwindow = PhoneGui()
    mainwindow.format_data()
    mainwindow.run()

    #PhoneGui().run()

if __name__ == "__main__":
    main()