from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase

# the arguments used here are R G B A (red,green,blue,alpha) 
# sets background colour
# each entry has to be between 0 and 1 so for example, 0.5 for green means 50% green

Window.clearcolor = (0.4,0.74,0.91,0.7)
Window.size = (375,667)



class PhotoRoot(FloatLayout):
    """Custom Class inheriting from floatlayout to provide no restriction
    on its child widgets"""
    
    pass

class Logo(Image):
    """Our Custom class pertaining to our logo which inherits from the Image
    widget"""
    
    pass 

class HomeWindow(Screen):
    pass 

class LoadingWindow(Screen):
    pb = ObjectProperty(None)
    
class PhotoDisplayWindow(Screen):
    pass

class PhotoZoomWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ImitariApp(App):
    def build(self):
        return

if __name__ == '__main__':
    LabelBase.register(name= 'LemonMilk', fn_regular = 'Fonts/LemonMilkMedium.ttf',
                   fn_bold = 'Fonts/LemonMilkBold.ttf')
    ImitariApp().run()