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
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self). __init__(**kwargs)
        self.cols = 1
        self.orientation= 'vertical'
                  
        # Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout(row_force_default=True,
        row_default_height=50)
        self.top_grid.cols = 5
        self.top_grid.size_hint= (1,0.2)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0}   
        Window.clearcolor=(0,0,0,1)

        # Add widget

        # Adding logo on top left
        self.Group_Icon=Image(size_hint=(0.35,0.1), pos={0,0.1}, source='logo.png')
        self.top_grid.add_widget(self.Group_Icon)

        self.Assign_Task = Button(text='Assign Task')
        self.top_grid.add_widget(self.Assign_Task)

        self.My_Tasks = Button(text='My Tasks')
        self.top_grid.add_widget(self.My_Tasks)

        self.Profile = Button(text='Profile',size_hint_x=None, width=80, pos_hint={1,None})
        self.top_grid.add_widget(self.Profile)

        self.logout = Button(text='Logout',size_hint_x=None, width=80, pos_hint={1,None})
        self.top_grid.add_widget(self.logout)

       
        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)


class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()