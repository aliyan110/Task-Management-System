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

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg= Rectangle(pos=self.pos, size=self.size, source='Pic.png')

        # adding heading on the registration page
        self.add_widget(Label(text="REGISTRATION",
            font_size=26, 
            pos_hint={"center_x":0.5,"center_y":0.1},
            size_hint_x= None,
            height=70,
            size_hint_y= None,
            width = 300))
        # Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.top_grid.size_hint= (0.6,0.8)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0.5}
        


        # Add widget
        self.top_grid.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Date Of Birth"))
        self.date = TextInput(multiline=False)
        self.top_grid.add_widget(self.date)

        self.top_grid.add_widget(Label(text="Contact"))
        self.contact = TextInput(multiline=False)
        self.top_grid.add_widget(self.contact)

        self.top_grid.add_widget(Label(text="Email"))
        self.mail = TextInput(multiline=False)
        self.top_grid.add_widget(self.mail)

        self.top_grid.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)

        self.top_grid.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False)
        self.top_grid.add_widget(self.password)

        self.top_grid.add_widget(Label(text="Confirm Password"))
        self.cpass = TextInput(multiline=False)
        self.top_grid.add_widget(self.cpass)

        if self.cpass.text != self.password.text:
            print("Re-Enter same password")

        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)

        # Creating Image Upload Button
        self.upload = Button(text="Upload Image", font_size=22,
        pos_hint={"center_x":0.5,"center_y":0.6},
        size_hint_x= None,
        height=70,
        size_hint_y= None,
        width = 250)
        self.upload.bind(on_press = self.push)
        self.add_widget(self.upload)
        self.add_widget(Label(text="or drop a file",
            font_size=18, 
            pos_hint={"center_x":0.5,"center_y":0.7},
            size_hint_x= None,
            height=70,
            size_hint_y= None,
            width = 250))

        # Creating Submit Button
        self.submit = Button(text="Register", font_size=18,
        pos_hint={"center_x":0.7},
        size_hint_x= None,
        height=50,
        size_hint_y= None,
        width = 200)

        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
    def press(self, instance):
        name = self.name.text
        DOB = self.date.text
        contact = self.contact.text
        email = self.mail.text
        username = self.username.text
        password = self.password.text

        self.add_widget(Label(text=f'Thank you Mr {name}, your details has been updated, please enter your credentials and login'))

        # Clearing data after once entered
        self.name.text =''
        self.date.text =''
        self.contact.text =''
        self.mail.text =''
        self.username.text =''
        self.password.text =''
        self.cpass.text =''
    
    def on_size(self, *args):   
        self.bg.size = self.size
     
    def push(self, instance):
        pass
class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()