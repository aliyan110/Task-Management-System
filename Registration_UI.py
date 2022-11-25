import json
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

# LoginScreen
class LogIn_Screen(Screen):
    def __init__(self, **kwargs):
        super(LogIn_Screen, self).__init__(**kwargs)
        self.name='login'
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
        self.text_input_user_name = TextInput(multiline = False, #padding_y = (20, 20), 
                                            size_hint = (1,0.3))
                                            # width = 10,
                                            # height=20
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
                    #padding_y = (20,20),
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
        self.button_sign_up.bind(on_release=self.button_Signup_pressed)
        


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

        self.button_login.bind(on_press= self.button_login_pressed)


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


        #self.greeting1.text = "Hello Mr. " + self.user.text + "...!"

    def on_size(self, *args):   
        self.bg.size = self.size

    def button_login_pressed(self, instance):
        self.text_input_user_name.text=''
        self.text_input_user_password.text=''
        
    def button_Signup_pressed(self, instance):
        self.app.root.current="register"
        # .manager.transition.direction="left" 




# RegisterScreen
class Registration_UI(Screen):
    def __init__(self, **kwargs):
        super(Registration_UI, self). __init__(**kwargs)
        self.name='register'
        self.cols = 1
        self.orientation= 'vertical'
        Window.clearcolor=(1,1,1,1)

        #image widget self.canvas.before will set image Pic.png as background
        with self.canvas.before:
            self.bg= Image(pos=self.pos, size=self.size, source='Pic.png')
            self.bg.opacity=0.4

        # adding heading on the registration page
        self.add_widget(Label(text="REGISTRATION",
            font_size=26, 
            pos_hint={"center_x":0.5,"center_y":0.1},
            size_hint_x= None,
            height=70,
            size_hint_y= None,
            width = 300,
            bold=True,
            color='#000000'))
            
        # Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout(row_force_default=True,
        row_default_height=50,
        spacing=10)
        self.top_grid.cols = 2
        self.top_grid.size_hint= (0.5,0.7)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0.5}

        
        


        # Add widget
        self.top_grid.add_widget(Label(text="Name", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)

        self.top_grid.add_widget(Label(text="Date Of Birth", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.date = TextInput(multiline=False)
        self.top_grid.add_widget(self.date)

        self.top_grid.add_widget(Label(text="Contact", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.contact = TextInput(multiline=False)
        self.top_grid.add_widget(self.contact)

        self.top_grid.add_widget(Label(text="Email", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.mail = TextInput(multiline=False)
        self.top_grid.add_widget(self.mail)

        self.top_grid.add_widget(Label(text="User Name", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)

        self.top_grid.add_widget(Label(text="Password", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.password = TextInput(multiline=False)
        self.top_grid.add_widget(self.password)

        self.top_grid.add_widget(Label(text="Confirm Password", font_size=20,size_hint_x=None, width=200,
        color='#000000'))
        self.cpass = TextInput(multiline=False)
        self.top_grid.add_widget(self.cpass)

        if self.cpass.text != self.password.text:
            print("Re-Enter same password")

        # Add top_grid into main grid as a widget
        self.add_widget(self.top_grid)

        # Creating Image Upload Button
        self.upload = Button(text="Upload Image", font_size=22,
        pos_hint={"center_x":0.5,"center_y":0.7},
        size_hint_x= None,
        height=70,
        size_hint_y= None,
        width = 250,
        background_color='#0000FF')
        self.upload.bind(on_press = self.push)
        self.add_widget(self.upload)
        self.add_widget(Label(text="or drop a file",
            font_size=16, 
            pos_hint={"center_x":0.5,"center_y":0.7},
            size_hint_x= None,
            height=30,
            size_hint_y= None,
            width = 250,
            color='#000000'))

        # Creating Submit Button
        self.submit = Button(text="Register", font_size=18,
        pos_hint={"center_x":0.7},
        size_hint_x= None,
        height=50,
        size_hint_y= None,
        width = 200,
        background_color='#008000')

        self.submit.bind(on_release = self.released)
        self.add_widget(self.submit)

    def released(self, instance):
        app.root.current='login'
        # import ScreenManager
        # import Login_Screen
        # ScreenManager().screen_transition()
        nam = self.name.text
        DOB = self.date.text
        contact = self.contact.text
        email = self.mail.text
        username = self.username.text
        password = self.password.text

# here the data needs to be sent to server before being erased


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


# class ParentScreen2(Screen):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#         super_box=BoxLayout(orientation ='vertical')
#         csm=ScreenManager()
#         cs1=LogIn_Screen(name="login")
#         cs2=Registration_UI(name="register")
#         csm.add_widget(cs1)
#         csm.add_widget(cs2)
#         csm.current="child_screen1"
#         self.csm=csm



class MyApp(App):
    def build(self):
        sm=ScreenManager()
        self.sm=sm
        sm.add_widget(LogIn_Screen(name='login'))
        sm.add_widget(Registration_UI(name='register'))
        sm.current="login"
        return sm

if __name__ == '__main__':
    MyApp().run()