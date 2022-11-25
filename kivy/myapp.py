from kivy.app import App
from kivy.graphics import *
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder


class Main_Screen(Screen):
    pass

class Second_Screen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv= Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return(kv)

if __name__== '__main__':
    MyApp().run()