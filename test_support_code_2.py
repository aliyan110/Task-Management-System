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
from kivy.uix.screenmanager import ScreenManager, Screen
from test_support_code_ import second_screen

## Tip: always to the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.

sm = ScreenManager()
screens = [Screen(name='Title {}'.format(i)) for i in range(4)]
for i in range(4):
    sm.add_widget(screens[i])


class SayHello(FloatLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='Pic.png')
        # self.window.add_widget(Image(source = "Pic.png"))
        
        # label widget
        self.lable_user_name = Label(
                        text="User name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 18,
                        color='#00FFCE'
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, padding_y = (20, 20), size_hint = (1,0.3))
        self.lable_password = Label(
                         text = "Password",
                         size_hint = (None, None),
                         width = 75,
                         height = 40,
                         font_size = 18,
                         color='#00FFCE'
                        )
        self.text_input_user_password = TextInput(
                    multiline = False,
                    padding_y = (20,20),
                    size_hint = (1,0.3)
                    )
        
        self.label_forget_password = Label(
                         text="forget_password",                                                                                                                               
                         size_hint = (100, 0.1),
                        # width = 75,
                         #height = 50,
                         font_size = 12,
                         #padding_y = (200,20),
                         color='#00FFCE',
                        pos_hint = {"center_x": 0.75, "center_y":1}
                        
                        )
        
        self.label_dont_account = Label(
                         text="didn't have account",
                         size_hint = (None, None),
                         width = 100,
                         height = 50,
                         font_size = 12,
                         #padding_y = (200,20),
                         color='#00FFCE'
                        )
        #button widget
        self.button_login = Button(
                      text = "login",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#00FFCE'
                      )
        self.button_login.bind(on_press = self.login_botton_pressed)
        
        ## adding items to gridlayout that we've created above
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        self.window.add_widget(self.lable_password)
        self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.label_forget_password)
        self.window.add_widget(self.label_dont_account)
        self.window.add_widget(self.button_login)

        screens[0] = self.window
        self.add_widget(screens[0])
        screens[1] = second_screen.build(self)
        print(sm.screen_names)
        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
        #self.add_widget(self.window)
        self.opacity = 0.50
        #return self.window

    def login_botton_pressed(self, instance):
        self.remove_widget(screens[0])
        self.add_widget(screens[1])
        #sm.switch_to(screens[1], direction='right')

    def on_size(self, *args):   
        self.bg.size = self.size
        
class SplashApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SplashApp().run()