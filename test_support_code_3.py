import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label 

from kivy.graphics import Rectangle

class LandingScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(LandingScreen, self).__init__(**kwargs)

        self.score=0

        # put whatever pos_hint value you want.          
        self.add_widget(Label(text='SCORE: ' + str(self.score), size_hint=(0.5, 0.5)))
        self.btn1=Button(text='button1 ', size_hint=(0.5, 0.5), 
        on_press=self.click_b1)
        self.btn2=Button(text='button2', size_hint=(0.5, 0.5), 
        on_press=self.click_b2)


            
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
    
        with self.canvas.before:
            self.bg = Rectangle(pos=self.pos, size=self.size, source='Pic.png')
    
    def on_size(self, *args):
        self.bg.size = self.size

    def click_b1(self, instance):
        self.score +=10
    def click_b2(self, instance):
        self.score += 10
       
class SplashApp(App):
    def build(self):
        return LandingScreen()

if __name__ == '__main__':
    SplashApp().run()
    