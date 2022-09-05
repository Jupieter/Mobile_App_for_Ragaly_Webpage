import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
cwd = os.getcwd()
# print(cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

import transform
from get_data import *



class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class RagalyApp(MDApp):
    def __init__(self, **kwargs):
        super(RagalyApp, self).__init__(**kwargs)
        self.posts = []
        self.max_post = 0
        self.post_pos = 0

    def four_news(self):
        print("direction: ")
        # pos_pos = self.post_pos + direction * 4
        # if pos_pos < 2: pos_pos = 1
        # elif pos_pos > self.max_post-3: pos_pos = self.max_post-3
        # print(pos_pos)

        pass    

    def on_start(self):
        # get_db = DB_questions()
        # posts, self.max_post = get_db.runner()                 # All last revisioned post
        # self.posts = transform.transform(posts) 
        # for post in self.posts:
        #     print(post)
        print("max_post: ", self.max_post)


    def build(self):
        print('Build 0')
        text1 = "[b]Ragályi Közös Önkormányzati Hivatal[/b] \n \n" 
        text2 = "(Ragály • Alsószuha • Imola • Szuhafő • Trizs • Zubogy) \n \n" 
        text3 = "[b]Cím:[/b] 3724 Ragály, Rákóczi Ferenc út 16.  \n \n"
        text4 = "[b]Telefon:[/b] (06–48) 354-001; (06-48) 504-201 \n \n"
        adress_text = text1 + text2 + text3 + text4
        print(adress_text)
        # print(self.ids)
        # self.ids.scr_adress.text = adress_text
        # self.icon = 'conf/icon/coffee-ante-porta-512.png'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        return Builder.load_file('kv/main.kv')

if __name__ == '__main__':
    print('START MAIN')
    RagalyApp().run()