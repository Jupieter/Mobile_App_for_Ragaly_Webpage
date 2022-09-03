# The posts are in HTML format in the Worldpress HomePage MySQL DB
from bs4 import BeautifulSoup
import requests
 

class HtmlTransformer():
    def __init__(self) -> None:
        # Initializing variable
        pass

    def text_find(self, html_post):
        soup = BeautifulSoup(html_post,  "html.parser")
        # Calculating result
        html_txt = soup.get_text()
        # Printing the result
        print('html_txt', html_txt)
        return html_txt 

    def link_find(html_post, *args):
        # print(html_post)
        # get all link from html
        soup = BeautifulSoup(html_post,  "html.parser")
        links = []
        for link in soup.find_all('a'):
            one_link = link.get('href')
            links.append(one_link)
            # print('              one_link', one_link)
        return links
    
    def pretty_html(html_post):
        soup = BeautifulSoup(html_post, "html.parser")
        print(soup.prettify())
    
    def picture_find():
        html_page = requests.get('http://books.toscrape.com/')
        soup = BeautifulSoup(html_page.content, 'html.parser')
        warning = soup.find('div', class_="alert alert-warning")
        book_container = warning.nextSibling.nextSibling

        images = book_container.findAll('img')
        example = images[0]
        pict = example.attrs['src']
        print(pict)
        
        url_base = "http://books.toscrape.com/" #Original website
        url_ext = example.attrs['src'] #The extension you pulled earlier
        full_url = url_base + url_ext #Combining first 2 variables to create       a complete URL
        r = requests.get(full_url, stream=True) #Get request on full_url
        if r.status_code == 200:                     #200 status code = OK
           with open("images/book1.jpg", 'wb') as f: 
              r.raw.decode_content = True
              shutil.copyfileobj(r.raw, f)

    def pict_link(links):
        pict_list = []
        for link in links:
            ends = link[-4:-1]
            # print(ends)
            if ends == ".jp":           # or ends == ".pn"
                pict_list.append(link)
        return pict_list



    
    def strong_murkup(self, html_in):
        ''' change the html <strong> to kivy [b] '''
        html_out1 = html_in.replace("</strong>", "[/b]")
        html_out = html_out1.replace("<strong>", "[b]")
        print("strong_murkup", html_out)
        return html_out

    def html_transform(self, posts_in):
        '''change al html post mark up to kivy mark up'''
        posts = posts_in
        for post in posts:
          html_act =post[3]
          # print("első: ",html_act)
          html_tr = self.strong_murkup(html_act)
          print(post[1])
          # print("második: ", html_tr)
          post[3] = html_tr
          # print(post[3])
          print(post)
        return posts


 