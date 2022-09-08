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
from kivymd.uix.boxlayout import MDBoxLayout
import transform
from get_data import *
from madeby import MadeByCard
print("import VII. Ragaly")


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
        print("on_start ragaly                START")
        get_db = DB_questions()
        print(get_db)
        posts, self.max_post = get_db.runner()                 # All last revisioned post
        self.posts = transform.transform(posts) 
        self.four_news(0)
        print(self.root.ids)
        self.root.ids.scr3_box.add_widget(MadeByCard())  
        print("on_start ragaly                END")


    def build(self):
        print('Build Ragaly')
        self.theme_cls.theme_style = "Light"
        print("light")
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        print("Blue")
        return Builder.load_file('kv/main.kv')

if __name__ == '__main__':
    print('START MAIN RAGALY')
    RagalyApp().run()