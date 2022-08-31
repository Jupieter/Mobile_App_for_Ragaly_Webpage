import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
# print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout



class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class RagalyApp(MDApp):

    def build(self):
        print('Build 0')
        # self.icon = 'conf/icon/coffee-ante-porta-512.png'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        return Builder.load_file('kv/main.kv')

if __name__ == '__main__':
    print('START MAIN')
    RagalyApp().run()