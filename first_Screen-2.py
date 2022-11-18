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
from kivy.core.window import Window


## Tip: always to the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.





class LogIn(FloatLayout):
    def __init__(self, **kwargs):
        super(LogIn, self).__init__(**kwargs)
        Window.clearcolor=(1,1,1,1)
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg = Image(pos=self.pos, size=self.size, source='Pic.png')
            self.bg.opacity=0.6
        # self.window.add_widget(Image(source = "Pic.png"))
        

        self.collector1=GridLayout(spacing=120,row_force_default = True, 
                 row_default_height=70)
        self.collector1.cols=2

        self.button_admin = Button(
                        text="Admin",
                        font_size = 20,
                        bold = True,
                        color=(1,1,1,1),
                        background_color = "#0323EE"
                        )
       # self.button_admin.bind(on_press = self.button_admin_pressed)
        #def botton_admin_pressed(self, instance):
         #   color = (1,1,1,0.1)
        
     
        self.button_employee = Button(
                      text = "Employee",
                      size_hint = (1,0.5),
                      bold = True,
                      font_size = 20,
                      background_color = '#FE1902'
                      )
        

        # label widget
        self.lable_user_name = Label(
                        text="User name",
                        size_hint = (None, None),
                        width = 90,
                        height = 30,
                        font_size = 18,
                        color='#00000',
                        bold = True
                        )
        # text input widget
        self.text_input_user_name = TextInput(multiline = False, padding_y = (20, 20), 
                                            size_hint = (1,0.3),
                                            width = 10,
                                            height=20)
        self.lable_password = Label(
                         text = "Password",
                         size_hint = (None, None),
                         width = 75,
                         height = 40,
                         font_size = 18,
                         color='#00000',
                         bold = True
                        )
        self.text_input_user_password = TextInput(
                    multiline = False,
                    padding_y = (20,20),
                    size_hint = (1,0.3)
                    )
        
        self.label_forget_password = Label(text="                                                                                                                                                                                             Forget Password",                                                                                                                               
                        size_hint = (None, None),
                        width = 155,
                        height = 20,
                        font_size = 12,
                        #padding_y = (200,20),
                        color='#564AE1',
                        pos_hint = {"center_x":0.8, "center_y":0.8},
                        bold=True
                        )
        

        self.label_dont_account = Label(
                         text="didn't have account",
                         size_hint = (None, None),
                         width = 105,
                         height = 20,
                         font_size = 12,
                         #padding_y = (200,20),
                         color='#434642',
                         bold = True
                        )

        self.collector=GridLayout(spacing =270 ,row_force_default = True, 
                 row_default_height=40, col_force_default = True, col_default_width = 70 
                  #col_force_default=True,
                  #col_default_width=100
                )
        self.collector.cols=2

        #self.sign_up = GridLayout()
        #self.sign_up.cols=1
        self.button_sign_up = Button(
                        text="Sign up",
                        size_hint = (1,0.7),
                        height=100,
                        width=100,
                        bold = True,
                     #   background_color = '#335BFF',
                      )
        


        #button widget
        #self.login = GridLayout()
        #self.login.cols=1
        self.button_login = Button(
                      text = "log in",
                      size_hint = (1,0.7),
                      height=40,
                      width=100,
                      bold = True,
                      background_color = '#187603'
                      )


        self.Gap = Label(text="  \n   ")
     #   self.button_login.bind(on_press = self.button_login_pressed)
        
        ## adding items to gridlayout that we've created above
        self.collector1.add_widget(self.button_admin)
        self.collector1.add_widget(self.button_employee)
        self.window.add_widget(self.collector1)
        self.window.add_widget(self.lable_user_name)
        self.window.add_widget(self.text_input_user_name)
        self.window.add_widget(self.lable_password)
        self.window.add_widget(self.text_input_user_password)
        self.window.add_widget(self.label_forget_password)
        self.window.add_widget(self.Gap)
        self.window.add_widget(self.label_dont_account)
        #self.window.add_widget(self.button_login)
        #self.sign_up.add_widget(self.button_sign_up)
        #self.login.add_widget(self.button_login)
        self.collector.add_widget(self.button_sign_up)
        self.collector.add_widget(self.button_login)
        self.window.add_widget(self.collector)
        
        
        
        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
        self.add_widget(self.window)
        #return self.window

    #def botton_login_pressed(self, instance):
        pass
        #self.greeting1.text = "Hello Mr. " + self.user.text + "...!"

    def on_size(self, *args):   
        self.bg.size = self.size
        
class SplashApp(App):
    def build(self):
        return LogIn()

if __name__ == "__main__":
    SplashApp().run()