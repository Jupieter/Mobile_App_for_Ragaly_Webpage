import os
import datetime


os.environ['KIVY_NO_CONSOLELOG'] = '0'
cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + '/conf'


from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
import datetime

import requests
import transform
from get_data import *
from madeby import MadeByBox
from kivy.core.window import Window
# print("import II. Ragaly")


def is_cnx_active(timeout=1):
    """ check the internet connection"""
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


class PostCard(MDCard):
    def __init__(self, **kwargs):
        super(PostCard, self).__init__(**kwargs)
    

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    # print("ContentNavigationDrawer   END")


class RagalyApp(MDApp):
    def __init__(self, **kwargs):
        super(RagalyApp, self).__init__(**kwargs)
        self.posts = []
        self.pagees = []
        self.max_post = 0
        self.max_page = 0
        self.post_pos = 0
        self.error = [[0,"Internet elérési probléma", 0, "Vagy nincs bekapcsolva a mobil WIFI \n vagy a weboldal nem elérhető",datetime.datetime(2017, 5, 20, 19, 0, 27),[],[]]]
    
    def re_fresh(self):
        """used   
            - to refresh button (if no internet when app started) and 
            - to Clock cikle
        """
        self.posts = []
        grids = ["grid_banner", "grid_banner_2"]
        for grd in grids:
            grid = self.root.ids[grd]
            ch = []
            for child in grid.children:
                ch.append(child)
            for dt in ch:
              grid.remove_widget(dt)
            ch = []
        self.post_news("post")
        self.root.ids["button_mn"].title = "Hírek, Hirdetmények"
        sm = self.root.ids.screen_manager
        sm.current = "scr_1"
        self.post_news("page")

    def ch_title(self, title):
        self.root.ids["button_mn"].title = title
    
    def go_home(self):
        self.root.ids["button_mn"].title = "Hírek, Hirdetmények"
        sm = self.root.ids.screen_manager
        sm.current = "scr_1"

    
    def id_post(self, post_pk):
        """ Displays the posts. The headline is a clickable link."""
        p_title = self.posts[post_pk][1]
        p_tit_adr = p_title
        if is_cnx_active(1) :
            p_parent = self.posts[post_pk][2]
            db = DB_questions()
            p_adr = db.get_post_name(p_parent)
            p_adr = "https://ragaly.hu/" + str(p_adr)
            p_tit_adr = "[ref=" + p_adr + "][b]" + p_title[0:25] + "[/b][/ref]"
        self.root.ids["scr2_post_title"].text = p_tit_adr
        self.root.ids["button_mn"].title = p_tit_adr

        p_text = self.posts[post_pk][3]
        self.root.ids["scr2_post"].text = p_text
        p_pict = self.posts[post_pk][6]
        if p_pict != []:
            self.root.ids["post_img"].source = p_pict[0]
        else:
            self.root.ids["post_img"].source = "images/no-available-picture.jpg"

        links = self.posts[post_pk][5]
        link_long = len(links)
        for j in range(3):
            link_id = "link" + str(j)
            self.root.ids[link_id].text = ""
        if link_long > 3:
            link_long = 3
        for i in range(0,link_long,1):
            link_id = "link" + str(i)
            link_tit_adr = "[ref=" + links[i] + "][u]" + links[i] + "[/u][/ref]"
            self.root.ids[link_id].text = link_tit_adr
        self.root.ids["post_scroll_2"].scroll_y = 1
        sm = self.root.ids.screen_manager
        sm.current = "scr_2"
    
    def post_news(self, post_page):
        """This add MDCards to main screen with post title and date and picture if have"""
        if is_cnx_active(1) :
            get_db = DB_questions()
            p, max_p = get_db.runner(post_page)                 # All last revisioned post/page
            tp = transform.transform(p) 
            if post_page == "post":
                p_min = 0
                self.max_post = max_p
                p_max = self.max_post
                grid = self.root.ids["grid_banner"]
                self.posts = tp
            elif post_page == "page":
                p_min = self.max_post + 1
                self.max_page = self.max_post + max_p
                p_max = self.max_page
                grid = self.root.ids["grid_banner_2"]
                self.posts.extend(tp)
        if self.posts == [] or self.posts == self.error:
            self.posts = self.error
            p_min = 0
            p_max = 1
            grid = self.root.ids["grid_banner"]
        for i in range(p_min, p_max, 1):
            card_id = "post" + str(i)
            banner = PostCard()
            banner.id= card_id
            banner.value = i
            p_title = str(self.posts[i][1])
            if len(p_title) >= 38:
                 p_title = p_title[0:38] + " ..."  # if the lenght of the title is too long
            p_id = self.posts[i][0]
            p_parent = self.posts[i][2]
            p_date = self.posts[i][4].date()
            banner.ids["post_title"].text = p_title 
            date_text = str(p_date)
            banner.ids["post_date"].text = date_text
            p_pict = self.posts[i][6]
            if p_pict != []:
                banner.ids["post_image"].source = p_pict[0]
            else:
                banner.ids["post_image"].source = "images/no-image.jpg"
            grid.add_widget(banner)


    def on_start(self):
        self.post_news("post")
        self.post_news("page")

            
        self.root.ids.scr4_box.add_widget(MadeByBox()) 
        scroll_heigt = int(((Window.height - 60) / Window.height)*100)/100
        print(Window.size)
        self.root.ids.post_scroll_1.size_hint_y = scroll_heigt
        self.root.ids.post_scroll_3.size_hint_y = scroll_heigt
        self.root.ids.post_scroll_2.size_hint_y = int(((Window.height - 140) / Window.height)*100)/100
        self.root.ids.scr2_post_title.pos_y = (Window.height - 140)
        self.root.ids.scr4_box.size_hint_y = int(((Window.height - 160) / Window.height)*100)/100
        from kivy import platform
        from service.main import start_service
        if platform == "android":
            print("Android service called")
            start_service()
        print("on_start ragaly                END")


    def build(self):
        return Builder.load_file('kv/main.kv')
    


if __name__ == '__main__':
    print('START MAIN RAGALY')
    RagalyApp().run()