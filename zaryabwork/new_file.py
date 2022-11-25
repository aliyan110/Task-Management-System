import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import *
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput


## this class wil return the layout of upper section assign_task, ...
class layout_Top_Grid:
    def __init__(self):
        self.layout_top_grid = GridLayout()
        self.layout_top_grid.cols = 5
        self.layout_top_grid.size_hint= (1, 0.2)
        self.layout_top_grid.pos_hint= {"center_x":0.5, "center_y":0.5}      
        
        # Adding logo on top left
        self.Image_Group_Icon=Image(size_hint=(0.35,0.1), pos={0,0.1}, source='logo.png')
        self.Assign_Task = Button(text='Assign Task')
        self.My_Tasks = Button(text='My Tasks')
        self.Profile = Button(text='Profile'
            #,size_hint_x=None, width=80, pos_hint={1,None}
            )
        self.logout = Button(text='Logout'
            #,size_hint_x=None, width=80, pos_hint={1,None}
            )
        self.layout_top_grid.add_widget(self.Image_Group_Icon)
        self.layout_top_grid.add_widget(self.Assign_Task)
        self.layout_top_grid.add_widget(self.My_Tasks)
        self.layout_top_grid.add_widget(self.Profile)
        self.layout_top_grid.add_widget(self.logout)
        
    def get_my_layout(self):
        return self.layout_top_grid

class layout_Right_Side:
    def __init__(self):
    ## Creating a layout for inserting images.     
        self.logo=Image(
            #pos=self.pos, size=self.size, 
            source='logo.jpeg')
        self.mission=Label(text='Mission Statement', font_size=16, bold=True, color= '#000000')
        self.mission_statement=Label(text='Our mission is to be market\nleader developing simple applications \n creating a revolution in development\n market',font_size=12, halign="left", color= '#1C2833')

        self.logo2=Image(
            #pos=self.pos, size=self.size, 
            source='logo.jpeg')
        self.vision=Label(text="Achievements", font_size=16, halign="left", color='#000000', bold=True)
        self.vision_statement=Label(text='%%here will be the recent achievements\n of our company%%',font_size=12, halign="left",color='#000000')
        
        self.layout_mission_collector= GridLayout()
        self.layout_mission_collector.cols=1
        self.layout_mission_collector.add_widget(self.logo)
        self.layout_mission_collector.add_widget(self.mission)
        self.layout_mission_collector.add_widget(self.mission_statement)

        self.layout_vision_collector= GridLayout()
        self.layout_vision_collector.cols=1
        self.layout_vision_collector.add_widget(self.logo2)
        self.layout_vision_collector.add_widget(self.vision)
        self.layout_vision_collector.add_widget(self.vision_statement)

        self.layout_image_side = GridLayout()
        self.layout_image_side.cols = 1
        # self.layout_image_side.size_hint = (0.3, 0.7)
        # self.layout_image_side.pos_hint = {"center_x": 0.8, "center_y":0.5}
        self.layout_image_side.add_widget(self.layout_mission_collector)
        self.layout_image_side.add_widget(self.layout_vision_collector)
        #self.layout_image_side.
    def get_my_layout(self):
        return self.layout_image_side

class layout_Left_Side:
    def __init__(self):
        self.layout_left_side=GridLayout()
        self.layout_left_side.cols=1
        
        self.lable_project_name = Label(
                        text="Project name",
                        # size_hint = (None, None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        self.text_input_project_name = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,0.7))
        
        self.lable_description = Label(
                        text="Description",
                        # size_hint = (None, None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        self.text_description = TextInput(multiline = False, padding_y = (20, 20), size_hint = (0.2,3))
        
        self.layout_for_efforts = GridLayout()
        self.layout_for_efforts.cols = 1
        
        self.lable_for_efforts = Label(
                        text="Efforts",
                        # size_hint = (None,None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_for_efforts = TextInput(multiline = False, padding_y = 20)
        
        self.layout_for_efforts.add_widget(self.lable_for_efforts)
        self.layout_for_efforts.add_widget(self.text_input_for_efforts)
        
        self.layout_for_deadline = GridLayout()
        self.layout_for_deadline.cols = 1

        self.lable_for_deadline = Label(
                        text="Deadline",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_for_deadline = TextInput(multiline = False, padding_y =20)
        self.layout_for_deadline.add_widget(self.lable_for_deadline)
        self.layout_for_deadline.add_widget(self.text_input_for_deadline)

        self.layout_for_efforts_and_deadline = GridLayout()
        self.layout_for_efforts_and_deadline.cols = 2
        self.layout_for_efforts_and_deadline.add_widget(self.layout_for_efforts)
        self.layout_for_efforts_and_deadline.add_widget(self.layout_for_deadline)
        
        self.button_accept = Button(
                      text = "Accept",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )
        self.button_decline = Button(
                      text = "Decline",
                      bold = True,
                      background_color = (0.7,0,0,1),
                    #   spacing=10
                      )
        
        self.layout_for_buttons = GridLayout()
        self.layout_for_buttons.cols = 2
        self.layout_for_buttons.add_widget(self.button_accept)
        self.layout_for_buttons.add_widget(self.button_decline)

        # finally adding things to main layout
        self.layout_left_side.add_widget(self.lable_project_name)
        self.layout_left_side.add_widget(self.text_input_project_name)
        self.layout_left_side.add_widget(self.lable_description)
        self.layout_left_side.add_widget(self.text_description)
        self.layout_left_side.add_widget(self.layout_for_efforts_and_deadline)
        self.layout_left_side.add_widget(self.layout_for_buttons)       

    def get_my_layout(self):
        return self.layout_left_side


class layout_Middle_Side:
    def __init__(self):
        self.layout_middle_side=GridLayout()
        self.layout_middle_side.cols=2
        
        self.layout_middle_side.add_widget(layout_Left_Side().get_my_layout())
        self.layout_middle_side.add_widget(layout_Right_Side().get_my_layout())
    def get_my_layout(self):
        return self.layout_middle_side

class layout_Bottom_Side:
    def __init__(self):
        self.layout_bottom_side=GridLayout()
        self.layout_bottom_side.cols=1
        
        self.button_nigotiate = Button(
                      text = "button_nigotiate",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )
        
        self.lable_reason = Label(
                        text="Reason",
                        # size_hint = (None,None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        self.text_input_reason = TextInput(multiline = True)
        
        self.lable_propose_efforts = Label(
                        text="Propose your efforts",
                        # size_hint = (0.5,3),
                        #width = 90,
                        #height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        self.text_input_propose_efforts = TextInput(multiline = False, size_hint=(0.6,0.2))

        self.button_submit = Button(
                      text = "Submit",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   size_hint = (None,None),
                    #   width = 2 ,
                    #   height = 1 ,
                    #   pos_hint = (2,1)
                    #   spacing=10
                      )
        self.layout_bottom_side.add_widget(self.button_nigotiate)
        self.layout_bottom_side.add_widget(self.lable_reason)
        self.layout_bottom_side.add_widget(self.text_input_reason)
        self.layout_bottom_side.add_widget(self.lable_propose_efforts)
        self.layout_bottom_side.add_widget(self.text_input_propose_efforts)
        self.layout_bottom_side.add_widget(self.button_submit)

    def get_my_layout(self):
        return self.layout_bottom_side



