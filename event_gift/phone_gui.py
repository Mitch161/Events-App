# Mitchell Haride
# Date: 26/03/19
# Time: 21:00

#Phone Information
# Name = Samsung Galaxy J4+
# Resolution = 720x1480
# Aspect Ratio = 18.5:9

from kivy.app import  App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
#from kivy.uix.dropdown import DropDown
#from kivy.base import runTouchApp
import tkinter as tk
from tkinter import ttk
import datetime
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import sys
import time
import os
import filecmp

#Constants
LARGE_FONT = ("roboto", 16)
COUNTDOWN_FONT = ("roboto", 32)

class PhoneGui(App):
    def __init__(self, **kwargs):
        super(PhoneGui, self).__init__(**kwargs)
        self.display = Main_Grid
        self.image = ""
        self.txt = ""
        self.video = ""
        self.target_time = 0

    def build(self):
        Config.set('graphics', 'width', '720')
        Config.set('graphics', 'height', '1480')

        #self.display.bind(size=self._update_rect, pos=self._update_rect)
        #with self.display:
        #    Color(0,1,0,1)
        #    self.rect = Rectangle(size=self.display.size, pos=self.display.pos)

        msg = TextWindow(self.txt)
        img = ImageWindow(self.image)
        vid = VideoWindow(self.video)

        clock = SimpleClock()
        Clock.schedule_interval(clock.update, 1)
        countdown = CountdownClock()
        Clock.schedule_interval(countdown.update, 1)
        return self.display(clock,countdown,img,msg)
        #return Main_Grid(clock, countdown)

    def retrieve_files(self):
        files_list = []
        files = os.listdir('giftevent/data')
        for file in files:
            files_list.append(file)
        return files_list

    #def _update_rect(self):
    #    self.rect.pos

    def format_data(self):
        filepath = "giftevent/data/"
        files = self.retrieve_files()
        for file in files:
            if ".txt" in file:
                self.txt = self.read_textfile(file)
            elif ".jpg" or ".png" in file:
                #self.image = ("giftevent/data/"+file)
                self.image = ('/home/mitchell/Pictures/Wallpapers/mitch2.png')
            elif ".mp4" in file:
                self.video = ("giftevent/data/"+file)
            else:
                print("Invalid format")

    def read_textfile(self, file):
        open_file = open("giftevent/data/"+file, "r")
        data = open_file.read()
        return data



class Main_Grid(GridLayout):
    def __init__(self, clock, countdown, img, msg, **kwargs):
        super(Main_Grid, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 3
        float_colour1 = 255/255.0
        float_colour2 = 255/255.0
        float_colour3 = 255/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 1480), pos=(0,0))
        #self.target_time = 60

        self.add_widget(Topbanner_Display(clock))
        #current_date = datetime.today().date()
        #self.add_widget(Label(text="Current Date\n"+current_date.strftime("%A")+"\n"
        #                           +current_date.strftime("%y:%m:%d"),size_hint_y=None,height=100))
        #self.add_widget(Label(text="",size_hint_y=None,height=100))
        #self.add_widget(clock)

        #self.add_widget(Label(text="", size_hint_x=None,width=0))
        self.add_widget(Event_Display(countdown, img))
        #self.add_widget(countdown)
        #self.add_widget(Label(text="", size_hint_x=None,width=0))

        #self.add_widget(Label(text="", size_hint_x=None, width=0))
        self.add_widget(msg)
        #self.add_widget(Label(text="", size_hint_x=None, width=0))

class Topbanner_Display(GridLayout):
    def __init__(self, clock, **kwargs):
        super(Topbanner_Display, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 1
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))
        self.add_widget(QuitGrid())
        current_date = datetime.today().date()
        self.add_widget(Label(text="Current Date\n"+current_date.strftime("%A")+" "
                                   +current_date.strftime("%y:%m:%d"), font_size="24"))
        self.add_widget(clock)

class Event_Display(GridLayout, PhoneGui):
    def __init__(self,countdown,img, **kwargs):
        super(Event_Display, self).__init__(**kwargs)
        self.rows=1
        self.cols=3
        self.size_hint_x = None
        self.size_hint_y = None
        self.width=720
        self.height=800
        self.add_widget(ButtonGridLeft())
        if self.target_time <= 0:
            self.add_widget(img)
        elif self.target_time > 0:
            self.add_widget(countdown)
        self.add_widget(ButtonGridRight())

class QuitGrid(GridLayout):
    def __init__(self, **kwargs):
        super(QuitGrid, self).__init__(**kwargs)
        self.rows=1
        self.cols=3
        self.size_hint_y=None
        self.height = 75
        self.add_widget(Label(text=""))
        self.add_widget(QuitButt())
        self.add_widget(Label(text=""))

class QuitButt(Button):
    def __init__(self, **kwargs):
        super(QuitButt, self).__init__(**kwargs)
        self.text = "Exit"
        self.font_size = 34
        self.size_hint_x = None
        self.width = 150
        self.background_normal = ''
        self.background_color = [244/255.0,244/255.0,244/255.0,0.2]

class ImageWindow(Image):
    def __init__(self, img, **kwargs):
        super(ImageWindow, self).__init__(**kwargs)
        self.source = img
        #self.texture_size = (720,800)
        #self.size_hint_x=None
        self.allow_stretch = True
        self.keep_ratio = True
        self.width = 720
        self.height = 800

class TextWindow(Label):
    def __init__(self, txt, **kwargs):
        super(TextWindow, self).__init__(**kwargs)
        self.text = txt
        #self.size_hint_y=None
        #self.height=100

class VideoWindow(Video):
    def __init__(self, vid, **kwargs):
        super(VideoWindow, self).__init__(**kwargs)
        self.source = vid

class SimpleClock(Label):
    def update(self, *args):
        #self.size_hint_y=None
        #self.height=100
        self.text="Current Time\n"+time.strftime("%H:%M:%S")
        self.font_size = "24"

class CountdownClock(Label, PhoneGui):
    def __init__(self, **kwargs):
        super(CountdownClock, self).__init__(**kwargs)
        #self.target_time = target_time
        self.font_size = "24"
    def update(self, *args):
        if self.target_time == 0:
            print("Event is Starting...")
            Clock.unschedule(self.update)
        else:
            self.target_time -= 1
            time_string = str(self.target_time)
            self.text="Time Remaining\n" + time_string

class ButtonGridLeft(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonGridLeft, self).__init__(**kwargs)
        self.rows=3
        self.cols=1
        self.size_hint_x = None
        self.width = 75
        self.add_widget(Label(text=""))
        self.add_widget(LeftButton())
        self.add_widget(Label(text=""))

class ButtonGridRight(GridLayout):
    def __init__(self, **kwargs):
        super(ButtonGridRight, self).__init__(**kwargs)
        self.rows=3
        self.cols=1
        self.size_hint_x = None
        self.width = 75
        self.add_widget(Label(text=""))
        self.add_widget(RightButton())
        self.add_widget(Label(text=""))

class LeftButton(Button):
    def __init__(self, **kwargs):
        super(LeftButton, self).__init__(**kwargs)
        self.text = "<"
        self.font_size = 34
        self.size_hint_y = None
        #self.size_hint_x = None
        self.height = 150
        #self.width = 75
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]

class RightButton(Button):
    def __init__(self, **kwargs):
        super(RightButton, self).__init__(**kwargs)
        self.text = ">"
        self.font_size = 34
        self.size_hint_y = None
        #self.size_hint_x = None
        self.height = 150
        #self.width = 75
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]

#if __name__ == "__main__":
    #Config.set('graphics','width','720')
    #Config.set('graphics','height','1480')
    #PhoneGui().run()