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


## Tip: always do the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.

class SayHello(FloatLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.35, "center_y":0.6}
        #add widgets to window

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='logo.jpeg')
        # self.window.add_widget(Image(source = "Pic.png"))
 
        # label widget
        self.lable_user_name = Label(
                        text="Project name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))
        self.lable_password = Label(
                         text = "Project Domain",
                         size_hint = (None, None),
                         width = 90,
                         height = 30,
                         font_size = 13,
                         color=(0,0,2,1)
                        )
        self.text_input_user_password = TextInput(
                    multiline = False,
                    padding_y = (20,20),
                    size_hint = (0.2,0.7)
                    )
         # label widget
        self.lable_description = Label(
                        text="Description",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_description = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,3))
        #button widget
        self.button_assign = Button(
                      text = "Assign",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = (0,0,2,1)
                      )
        self.collector=GridLayout()
        self.collector.cols=2

        self.assign_to= GridLayout()
        self.assign_to.cols=1
        self.lable_assign_to = Label(
                        text="Assign to",
                        # size_hint = (None, None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_assign_to = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))
        self.lable_start_date = Label(
                        text="Start Date",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_start_date = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))

        self.efforts= GridLayout()
        self.efforts.cols=1
        self.lable_efforts = Label(
                        text="Efforts",
                        # size_hint = (None, None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_efforts = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))

        self.lable_deadline = Label(
                        text="Deadline",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_deadline = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))

        self.button_assign.bind(on_press = self.assign_botton_pressed)

        # adding items to gridlayout that we've created above
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        self.window.add_widget(self.lable_password)
        self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.lable_description)
        self.window.add_widget(self.text_description)
        self.assign_to.add_widget(self.lable_assign_to)
        self.assign_to.add_widget(self.text_input_assign_to)
        self.assign_to.add_widget(self.lable_start_date)
        self.assign_to.add_widget(self.text_input_start_date)
        self.assign_to.add_widget(self.button_assign)
        self.efforts.add_widget(self.lable_efforts)
        self.efforts.add_widget(self.text_input_efforts)
        self.efforts.add_widget(self.lable_deadline)
        self.efforts.add_widget(self.text_input_deadline)
        self.collector.add_widget(self.assign_to)
        self.collector.add_widget(self.efforts)
        self.window.add_widget(self.collector)


        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
        self.add_widget(self.window)
        #return self.window

    def assign_botton_pressed(self,instance):
        pass

    def on_size(self, *args):   
        self.bg.size = self.size
        
class SplashApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SplashApp().run()