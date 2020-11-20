from kivy.app import App
from kivy.core.window import Window

# the arguments used here are R G B A (red,green,blue,alpha) 
# sets background colour
# each entry has to be between 0 and 1 so for example, 0.5 for green means 50% green

Window.clearcolor = (0.4,0.74,0.91,0.7)

class PhotoApp(App):
    
    def build(self):
        return 

if __name__ == '__main__':
    PhotoApp().run()