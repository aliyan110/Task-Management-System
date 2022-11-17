from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager

class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class Manager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
         pass

MyApp().run()
