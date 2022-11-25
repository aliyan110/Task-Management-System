import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import Registration_UI
import Login_Screen


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.transition = FadeTransition()
        self.add_widget(Registration_UI(name='register'))
        self.add_widget(Login_Screen(name='login'))

    def screen_transition(self, *args):
        self.current = 'login'
