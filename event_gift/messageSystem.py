from kivy.app import  App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

class messageSys(App):
    def __init__(self, **kwargs):
        super(messageSys, self).__init__(**kwargs)
        self.display = Window

    def build(self):
        Config.set('graphics', 'width', '720')
        Config.set('graphics', 'height', '1480')
        return self.display

class Window(GridLayout):
    def __init__(self, clock, countdown, img, msg, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 6
        float_colour1 = 255 / 255.0
        float_colour2 = 255 / 255.0
        float_colour3 = 255 / 255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1, float_colour2, float_colour3, float_colour4)
            Rectangle(size=(720, 1480), pos=(0, 0))