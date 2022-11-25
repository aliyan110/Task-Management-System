from file1 import MyScreen1
from file2 import MyScreen2


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen1())
        sm.add_widget(MyScreen2())
        return sm


from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class MyScreen1(Screen):
    pass

Builder.load_string('''
<MyScreen1>:
    Label:
        text: 'Hello World'
''')

