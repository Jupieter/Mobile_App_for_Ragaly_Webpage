# The posts are in HTML format in the Worldpress HomePage MySQL DB
from bs4 import BeautifulSoup
import requests
 


def text_find(html_post):
    soup = BeautifulSoup(html_post,  "html.parser")
    # Calculating result
    html_txt = soup.get_text()
    return html_txt 

def link_find(html_post):
    """ get all link"""
    soup = BeautifulSoup(html_post,  "html.parser")
    links = []
    for link in soup.find_all('a'):
        one_link = link.get('href')
        links.append(one_link)
    return links
    
def pretty_html(html_post):
    soup = BeautifulSoup(html_post, "html.parser")
    # print(soup.prettify())
    
def pict_link(links):
    """ get all link wich containes picture"""
    pict_list = []
    for link in links:
        ends = link[-4:-1]
        if ends == ".jp":           # or ends == ".pn"
            pict_list.append(link)
    return pict_list

def strong_murkup(html_in):
    ''' change the html <strong> to kivy [b] '''
    html_out1 = html_in.replace("</strong>", "[/b]")
    html_out = html_out1.replace("<strong>", "[b]")
    return html_out

def html_transform(posts_in):
    '''change al html post mark up to kivy mark up'''
    posts = posts_in
    for post in posts:
      html_act =post[3]
      html_tr = strong_murkup(html_act)
      post[3] = html_tr
    return posts
 