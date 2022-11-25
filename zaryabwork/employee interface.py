import kivy
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
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.core.window import Window

from new_file import layout_Top_Grid
from new_file import layout_Right_Side
from new_file import layout_Middle_Side
from new_file import *


## Tip: always do the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.

class SayHello(RelativeLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)
        ## Creating a gridlayout for user, pwd and other items etc.
        self.layout_window = GridLayout()
        self.layout_window.cols = 1
        self.layout_window.size_hint = (1, 1)
        self.layout_window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        self.layout_window.clearcolor=(0,0,0,0)

        #image widget self.canvas.before will set image Pic.png as background
        Window.clearcolor=(0.9, 0.9, 0.9,1)
       
        # Add all layouts into main layout as a widget
        self.layout_window.add_widget(layout_Top_Grid().get_my_layout())
        self.layout_window.add_widget(layout_Middle_Side().get_my_layout())
        self.layout_window.add_widget(layout_Bottom_Side().get_my_layout())
        self.add_widget(self.layout_window)
        
    def assign_botton_pressed(self,instance):
        pass

    # def on_size(self, *args):   
    #     self.bg.size = self.size
        
class SplashApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SplashApp().run()