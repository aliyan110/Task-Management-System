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
from kivy.core.window import Window
import mysql.connector as connector


## Tip: always do the settings first then add data to layouts
## Tip2: always name the variables meaningful and with the type as well in-order to make code more readable.

class SayHello(FloatLayout):
    def __init__(self, **kwargs):
        super(SayHello, self).__init__(**kwargs)

    # Add Task bar
# Add Another Grid for text to be entered and one main grid for submit button and result
        self.top_grid = GridLayout(row_force_default=True,
        row_default_height=50)
        self.top_grid.cols = 5
        self.top_grid.size_hint= (1,0.2)
        self.top_grid.pos_hint= {"center_x":0.5, "center_y":0.9}      
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
        
        #add widgets to windowy
  
        ## Creating a gridlayout for user, pwd and other items etc.
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.35, "center_y":0.55}
        self.window.clearcolor=(0,0,0,1)

        ## Creating a layout for inserting images.
        self.imageside = GridLayout()
        self.imageside.cols = 1
        self.imageside.size_hint = (0.3, 0.7)
        self.imageside.pos_hint = {"center_x": 0.8, "center_y":0.5}

        self.vision_collector= GridLayout()
        self.vision_collector.cols=1

        self.mission_collector= GridLayout()
        self.mission_collector.cols=1

        self.logo=Image(pos=self.pos, size=self.size, source='logo.jpeg')
        self.logo2=Image(pos=self.pos, size=self.size, source='logo.jpeg')
        self.mission=Label(text='Mission Statement', font_size=16, bold=True, color= '#000000')
        self.mission_statement=Label(text='Our mission is to be market\nleader developing simple applications \n creating a revolution in development\n market',font_size=12, halign="left", color= '#1C2833')

        self.vision= Label(text="Achievements", font_size=16, halign="left", color='#000000', bold=True)
        self.vision_statement= Label(text='%%here will be the recent achievements\n of our company%%',font_size=12, halign="left",color='#000000')
        
        self.mission_collector.add_widget(self.logo)
        self.mission_collector.add_widget(self.mission)
        self.mission_collector.add_widget(self.mission_statement)

        self.vision_collector.add_widget(self.logo2)
        self.vision_collector.add_widget(self.vision)
        self.vision_collector.add_widget(self.vision_statement)

        self.imageside.add_widget(self.mission_collector)
        self.imageside.add_widget(self.vision_collector)

        self.add_widget(self.imageside)


        #image widget self.canvas.before will set image Pic.png as background
        Window.clearcolor=(0.9, 0.9, 0.9,1)
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
        self.text_input_user_name = TextInput(multiline = False, padding = 10, size_hint = (0.2,0.7))
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
                    padding = 10,
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
        self.text_description = TextInput(multiline = True, padding = 10, size_hint = (0.2,3))
        #button widget
        self.button_assign = Button(
                      text = "Assign",
                      bold = True,
                      background_color = (0,0,2,1),
                    #   spacing=10
                      )
        self.button_assign.bind(on_press = self.press)

        #button widget
        self.button_cancel = Button(
                      text = "Cancel",
                      bold = True,
                      background_color = (0.7,0,0,1),
                    #   spacing=10
                      )
        self.lable_gap = Label(text="\n")
        self.lable_gap2 = Label(text="\n")
        
        
        self.button_assign.pos_hint= (0,0.9)
        self.collector=GridLayout(padding=6)
        self.collector.cols=2
        # self.collector.pos_hint=(0,0.8),


        self.assign_to= GridLayout(row_force_default=True,
        row_default_height= 30,
        col_force_default=True,
        col_default_width=225)
        self.assign_to.cols=1
        self.lable_assign_to = Label(
                        text="Assign to",
                        # size_hint = (None,None),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_assign_to = TextInput(multiline = False, padding_y = 5)
        self.lable_start_date = Label(
                        text="Start Date",
                        # size_hint = (0.5,3),
                        #width = 90,
                        #height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_start_date = TextInput(multiline = False, padding_y = 5)

        self.efforts= GridLayout(row_force_default=True,
        row_default_height=30,
        col_force_default=True,
        col_default_width=225)
        self.efforts.cols=1
        self.lable_efforts = Label(
                        text="Efforts",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_efforts = TextInput(multiline = False, padding_y = 5)

        self.lable_deadline = Label(
                        text="Deadline",
                        # size_hint = (0.5,3),
                        # width = 90,
                        # height = 30,
                        font_size = 13,
                        color=(0,0,2,1)
                        )
        # text input widget
        self.text_input_deadline = TextInput(multiline = False, padding_y = 5)

        #self.button_assign.bind(on_press = self.assign_botton_pressed)

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
        #self.assign_to.add_widget(self.button_assign)
        self.efforts.add_widget(self.lable_efforts)
        self.efforts.add_widget(self.text_input_efforts)
        self.efforts.add_widget(self.lable_deadline)
        self.efforts.add_widget(self.text_input_deadline)
        self.collector.add_widget(self.assign_to)
        self.collector.add_widget(self.efforts)
        self.assign_to.add_widget(self.lable_gap)
        self.assign_to.add_widget(self.button_cancel)
        self.efforts.add_widget(self.lable_gap2)
        self.efforts.add_widget(self.button_assign)
        self.window.add_widget(self.collector)


        ## self itself is a FloatLayout, so add the gridlayout(self.window) to it.
        self.add_widget(self.window)
        #return self.window

        self.con = connector.connect(host='localhost',
                port = '3306',
                user = 'samad',
                password = 'pass123',
                database = 'pythontest',
                auth_plugin = 'mysql_native_password')


        query = 'create table if not exists admin_table(name varchar(100) primary key,domain varchar(50),description varchar(2000),assign_to varchar(50) ,effort varchar(50),start_date varchar(20), deadline varchar(20))'#, cpassword varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("admin table created")


    def insert_user(self,name,domain,description,assign_to,effort,start_date,deadline):
        query = "insert into admin_table(name,domain,description,assign_to,effort,start_date,deadline) values('{}','{}','{}','{}','{}','{}','{}')".format(name,domain,description,assign_to,effort,start_date,deadline)

        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("details saved to db")


    def fetch_all(self):
        query = "select * from admin_table"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Project Name: ", row [0])
            print("Project domain: ", row[1])
            print("Description:", row[2])
            print("Assign to:", row [3])
            print("Effort: ", row[4])
            print("Start date:", row[5])
            print("dead line", row[6])
        #    print("Confirm Password: "row[6])
            print()
            print()


    def press(self, instance):
        
        name = self.text_input_user_name.text
        domain = self.text_input_user_password.text
        description = self.text_description.text
        assign_to = self.text_input_assign_to.text
        effort = self.text_input_efforts.text
        start_date = self.text_input_start_date.text
        deadline = self.text_input_deadline.text
        SayHello.insert_user(self,name,domain,description,assign_to,effort, start_date, deadline)
        SayHello.fetch_all(self)
        # self.add_widget(Label(text=f'Thank you Mr {name}, your details has been updated, please enter your credentials and login'))

        # Clearing data after once entered
        self.text_input_user_name.text =''
        self.text_input_user_password.text=''
        self.text_description.text=''
        self.text_input_assign_to.text=''
        self.text_input_efforts.text=''
        self.text_input_start_date.text=''
        self.text_input_deadline.text=''
        
   # def on_size(self, *args):   
    #    self.bg.size = self.size
     
    def push(self, instance):
        pass
            
#class MyApp(App):
 #   def build(self):
  #      return MyLayout()

#if __name__ == '__main__':
#MyApp().run()


class SplashApp(App):
    def build(self):
        return SayHello()

if __name__ == "__main__":
    SplashApp().run()