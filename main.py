import os
import datetime
print("import I. Ragaly")
# from tkinter import Image
os.environ['KIVY_NO_CONSOLELOG'] = '0'
cwd = os.getcwd()
print("cwd, ",cwd)
os.environ['KIVY_HOME'] = cwd + '/conf'



from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import AsyncImage

import transform
from get_data import *
from madeby import MadeByBox
import urllib.request
import requests
print("import II. Ragaly")


def is_cnx_active(timeout=1):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

class PostCard(MDCard):
    def __init__(self, **kwargs):
        super(PostCard, self).__init__(**kwargs)
    

class ContentNavigationDrawer(MDBoxLayout):
    print("ContentNavigationDrawer")
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    print("ContentNavigationDrawer   END")


class RagalyApp(MDApp):
    def __init__(self, **kwargs):
        print("--init--")
        super(RagalyApp, self).__init__(**kwargs)
        self.posts = []
        self.max_post = 4
        self.post_pos = 0
        print("--init--   END")
    
    def go_home(self):
        sm = self.root.ids.screen_manager
        sm.current = "scr_1"

    def get_sql_data(self):
        """ If have internet get data with get_db.py and transform the post content to 
         kivy formatted text"""
        if is_cnx_active(1) :
            get_db = DB_questions()
            # print(get_db)
            posts, self.max_post = get_db.runner()                 # All last revisioned post
            self.posts = transform.transform(posts) 
            # self.four_news(0)
            self.post_news()
            # print(self.root.ids)


    def hun_to_eng(self, p_adr):
        """ make wordpress permalink from the post title"""
        magyar='íéáűőúöüó '
        angol='ieauououo-'
        p_adr = p_adr.lower()
        for i in range(0,10
        ):
            p_adr=p_adr.replace(magyar[i],angol[i])
            # p_adr=p_adr.replace(" ","-")
        unnecessary = ['"',"'","."]
        for j in unnecessary:
            p_adr=p_adr.replace(j,"")
            # p_adr=p_adr.replace("'","")
            # p_adr=p_adr.replace(".","")
        p_adr = "https://ragaly.hu/" + str(p_adr)
        print('Adress.......: ', p_adr)
        return p_adr
    
    def id_post(self, post_pk):
        print("The Post", post_pk)
        p_title = self.posts[post_pk][1]
        p_adr = self.hun_to_eng(p_title)
        p_tit_adr = "[ref=" + p_adr + "][b]" + p_title + "[/b][/ref]"
        print(p_tit_adr)
        p_text = self.posts[post_pk][3]
        print("p_title", p_title)
        grid = self.root.ids["post_grid"]
        # print(self.root.ids)
        # print(grid)
        self.root.ids["scr2_post_title"].text = p_tit_adr
        # self.root.ids["scr2_post_link"].text = p_tit_adr
        self.root.ids["scr2_post"].text = p_text
        p_pict = self.posts[post_pk][5]
        print(p_pict)
        if p_pict != []:
            print(p_pict[0])
            self.root.ids["post_img"].source = p_pict[0]
        else:
            self.root.ids["post_img"].source = "images/cimer.jpg"
        sm = self.root.ids.screen_manager
        sm.current = "scr_2"
    
    def post_news(self):
        """This add MDCards to main screen with post title anf date and picture if have"""
        print("max post: ", self.max_post)
        grid = self.root.ids["grid_banner"]
        for i in range(0,self.max_post,1):
            card_id = "post" + str(i)
            banner = PostCard()
            banner.id= card_id
            banner.value = i
            p_id = self.posts[i][0]
            p_title = self.posts[i][1]
            p_parent = self.posts[i][2]
            p_date = self.posts[i][4].date()
            banner.ids["post_title"].text = str(p_title)
            banner.ids["post_date"].text = str(i) + " : " + str(p_date)  + " : " + str(p_id)  + " : " + str(p_parent)
            p_pict = self.posts[i][5]
            if p_pict != []:
                print(p_pict[0])
                print(banner.ids["post_image"].source)
                banner.ids["post_image"].source = p_pict[0]
            else:
                banner.ids["post_image"].source = "images/cimer.jpg"
            grid.add_widget(banner)
             #print(banner.ids)
 

    def on_start(self):
        print("on_start ragaly                START")
        self.get_sql_data()
        self.root.ids.scr3_box.add_widget(MadeByBox()) 
        # self.root.ids.post_grid.add_widget(PostBox()) 
        print("on_start ragaly                END")


    def build(self):
        print('Build Ragaly')
        # self.theme_cls.theme_style = "Light"
        # print("light")
        # self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        # print("Blue")

        return Builder.load_file('kv/main.kv')

if __name__ == '__main__':
    print('START MAIN RAGALY')
    RagalyApp().run()