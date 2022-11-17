from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# class gl(App):
#     def build(self):
#         layout = GridLayout(rows = 2)
#         btn1 = Button(text="Zaryab")
#         btn2 = Button(text="Chal")
#         btn3 = Button(text="Rha ")
#         btn4 = Button(text="Hai")

#         layout.add_widget(btn1)
#         layout.add_widget(btn2)
#         layout.add_widget(btn3)
#         layout.add_widget(btn4)

#         return layout

# class gl(App):


# gl().run()

print("hellow world")

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)

class MyApp(App):
    def build(self):
        layout = GridLayout()
        l1 =  Label(text="User Name", size_hint = (None,None), width = 200, height = 900, font_size = 15, bold = True, italic = True, color = (0,0,0,1))
        l2 =  Label(text="Password", size_hint = (None,None), width = 200, height = 1000, font_size = 15,bold = True, italic = True, color = (0,0,0,1))
        layout.add_widget(l1)
        layout.add_widget(l2)
        return layout 
        
#if _name_ == '_main_':
MyApp().run()        

