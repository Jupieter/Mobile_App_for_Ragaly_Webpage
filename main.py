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
        text1 = "[b]Ragályi Közös Önkormányzati Hivatal[/b] \n \n" 
        text2 = "(Ragály • Alsószuha • Imola • Szuhafő • Trizs • Zubogy) \n \n" 
        text3 = "[b]Cím:[/b] 3724 Ragály, Rákóczi Ferenc út 16.  \n \n"
        text4 = "[b]Telefon:[/b] (06–48) 354-001; (06-48) 504-201 \n \n"
        adress_text = text1 + text2 + text3 + text4
        print(adress_text)
        print(self.ids)
        # self.ids.scr_adress.text = adress_text
        # self.icon = 'conf/icon/coffee-ante-porta-512.png'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        return Builder.load_file('kv/main.kv')

if __name__ == '__main__':
    print('START MAIN')
    RagalyApp().run()