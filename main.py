import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
# print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivymd.app import MDApp
from kivy.lang import Builder

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