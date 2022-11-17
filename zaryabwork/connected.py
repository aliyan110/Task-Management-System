from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

from zaryabwork.main import Login

class Connected(Screen):
    def connected(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()