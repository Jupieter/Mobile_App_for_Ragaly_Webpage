# The posts are in HTML format in the Worldpress HomePage MySQL DB
from bs4 import BeautifulSoup
 

class HtmlTransformer():
    def __init__(self) -> None:
        # Initializing variable
        pass

    def text_find(html_data):
        soup = BeautifulSoup(html_data,  "html.parser")
        # Calculating result
        html_txt = soup.get_text()
        # Printing the result
        print('html_txt', html_txt)
        return html_txt 

    def link_find(html_data):
        # get all link from html
        soup = BeautifulSoup(html_data,  "html.parser")
        links = []
        for link in soup.find_all('a'):
            one_link = link.get('href')
            links.append(one_link)
            print('one_link', one_link)
        return links
    
    def pretty_html(html_data):
        soup = BeautifulSoup(html_data, "html.parser")
        print(soup.prettify())


 