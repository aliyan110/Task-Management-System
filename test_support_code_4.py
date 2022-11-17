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


class SayHello(BoxLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        self.lable_title_of_task = Label(
                                text="Title of Task",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                font_size=18,
                                color="#00FFCE"
                                ) 
        self.text_input_title_of_task= TextInput(multiline = True)
        self.lable_description = Label(
                                text="Decription",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                font_size=18,
                                color="#00FFCE"
                                )
        self.text_input_description= TextInput(multiline = True)

        self.lable_effort = Label(
                                text="Email+Push",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                font_size=18,
                                color="#00FFCE",
                                ) 
        self.text_effort = TextInput(multiline = False, size_hint = (0,0))
        self.lable_deadline = Label(
                                text="Profile Screen",
                                size_hint=(None,None),
                                width= 90,
                                height=30,
                                font_size=18
                                #color="#00FFCE"
                                )
        self.text_deadline = TextInput(multiline = False, size_hint = (0,0))
        
        
        self.button_accept = Button(
                      text = "Accept",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#00FFCE'
                      )
        self.button_accept.bind(on_press = self.accept_button_pressed)
    
        self.window.add_widget(self.lable_title_of_task)
        self.window.add_widget(self.text_input_title_of_task)
        self.window.add_widget(self.lable_description)
        self.window.add_widget(self.text_input_description)
        self.window.add_widget(self.lable_effort)
        self.window.add_widget(self.text_effort)
        self.window.add_widget(self.lable_deadline)
        self.window.add_widget(self.text_deadline)
        self.window.add_widget(self.button_accept)
        
        self.add_widget(self.window)
    def accept_button_pressed(self, instance):
        pass

class SpApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SpApp().run()