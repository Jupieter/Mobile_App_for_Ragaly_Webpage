import os
import datetime
from tkinter import Image
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
        self.max_post = 4
        self.post_pos = 0
    
    def id_post(self, s_value):
        print("The Post", s_value)

    def four_news(self, direction):
        print("direction: ", direction)
        self.post_pos += direction * 4
        if self.post_pos >= (self.max_post-3): 
            self.post_pos = self.max_post-4
        if self.post_pos <= 0: 
            self.post_pos = 0
        if direction == 0:
            self.post_pos = 0
        print(self.post_pos)
        # print(self.root.ids)
        for pos in range(0,4,1):
            card_id = "post" + str(pos+1)
            post_id  = self.post_pos + pos
            # rint(self.root.ids[card_id].ids["post_title"])
            # self.root.ids[card_id].ids["post_title"].text = str(self.post_pos + pos)
            self.root.ids[card_id].value = post_id
            p_title = self.posts[post_id][1]
            self.root.ids[card_id].ids["post_title"].text = str(p_title)
            p_date = self.posts[post_id][4].date()
            print(p_date)
            self.root.ids[card_id].ids["post_date"].text = str(p_date)
            p_pict = self.posts[post_id][5]
            if p_pict != []:
                print(p_pict[0])
                print(self.root.ids[card_id].ids["post_image"].source)
                self.root.ids[card_id].ids["post_image"].source = p_pict[0]
            else:
                self.root.ids[card_id].ids["post_image"].source = "images/cimer.jpg"


        pass    

    def on_start(self):
        get_db = DB_questions()
        posts, self.max_post = get_db.runner()                 # All last revisioned post
        self.posts = transform.transform(posts) 
        # for post in self.posts:
        #     print(post)
        # print("max_post: ", self.max_post)
        self.four_news(0)


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