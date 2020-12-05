from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from DuplicateRemover import DuplicateRemover
from kivy.properties import ObjectProperty

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
    """Initial window that users see that shows the logo and 
    allows the user to begin sweeping"""
    
    pb = ObjectProperty(None)
    beginsweep = ObjectProperty(None)
    def beginSweep(self):
        
        dirname = "Images"
        
        # Remove Duplicates
        dr = DuplicateRemover(dirname)
        dr.find_duplicates()    
"""
class LoadingWindow(Screen):
    pass
"""
    
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
    
   



# Find Similar Images
#dr.find_similar("image11.jpg",10)

"""
<LoadingWindow>:
    name: "loadingscreen"
    beginsweep: beginsweep
    pb: pb
    root.beginSweep()
    PhotoRoot:
        Border:
        GridLayout:
            cols: 1 
            rows: 4
            pos_hint: {"center_x":0.5,"center_y": 0.56}
            Label:
                color: (0,0,0,1)
                bold: True
                font_size: 30
                text: "IMITARI"
                size: self.texture_size
                text_size: root.width-30, None
                halign: "center"
                valign: "bottom"  
            BoxLayout:
                size_hint_y: 0.4
                Image:
                    source: 'logo.png'
                    size_hint_y: 2
                    pos_hint: {"center_x":1,"center_y":0.6}
                    
                    
            AnchorLayout:
                anchor_y: "bottom"
                anchor_x: "center"
                Label:
                    color: (0,0,0,1)
                    text: "Sweeping..."
                    size_hint_x: 0.6
                    size_hint_y: 0.5
                    size: self.texture_size
                    text_size: root.width-30, None
                    halign: "center"
                    valign: "top"
                ProgressLabel:
                    id: pblabel
                    text: str(pb.value) + "%"
            
            AnchorLayout:
                size_hint_y: 0.5  
                MyProgress:
                    id: pb
                    anchor_y: "top"
                    anchor_x: "center"

        # temporary button just to bypass loading screen DELETE BEFORE EXPORT
        MyButton:
            text: "next page"
            text_size: self.size
            size_hint: (0.1,0.1)
            pos_hint: {'center_x':0.9,'center_y':0.2}
            on_release: 
                app.root.current = "photodisplay"
                root.manager.transition.direction = 'left'
"""

    