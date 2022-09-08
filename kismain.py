import os
print("import I. Ragaly")
os.environ['KIVY_NO_CONSOLELOG'] = '0'
cwd = os.getcwd()
print("cwd, ",cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from madeby import MadeByBox

kv = """
MDScreen:
    id: "main_scr"
    MDBoxLayout:
        id: scr3_box
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: 0.95, 0.95
    
"""


class MadeByApp(MDApp):
    # def __init__(self, **kwargs):
    #     print("--init-- MadeByApp")
    
    def build(self):
        print('Build Ragaly')
        self.theme_cls.theme_style = "Light"
        print("light")
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        print("Blue")
        return Builder.load_string(kv)

    def on_start(self):
        print('on_start')
        print(self.root.ids)
        self.root.ids.scr3_box.add_widget(MadeByBox())    



if __name__ == '__main__':
    print('START MAIN MadeBy')
    MadeByApp().run()
