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

import transform
from get_data import *
from madeby import MadeByBox
print("import II. Ragaly")



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
    
    def id_post(self, post_pk):
        print("The Post", post_pk)
        p_title = self.posts[post_pk][1]
        p_text = self.posts[post_pk][3]
        print("p_title", p_title)
        grid = self.root.ids["post_grid"]
        print(self.root.ids)
        print(grid)

        # post_t = PostTitleLabel
        # grid.add_widget()

        self.root.ids["scr2_post_title"].text = p_title
        self.root.ids["scr2_post"].text = p_text
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
        get_db = DB_questions()
        # print(get_db)
        posts, self.max_post = get_db.runner()                 # All last revisioned post
        self.posts = transform.transform(posts) 
        # self.four_news(0)
        self.post_news()
        # print(self.root.ids)
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