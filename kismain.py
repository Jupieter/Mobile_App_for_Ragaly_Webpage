from get_data import *
from soap import *

get_db = DB_questions()
posts = get_db.runner()                 # All last revisioned post
# print("get_db", get_db)

trafo = HtmlTransformer

# print(posts)
for post in posts:
    # print(post)
    html_data = post[3]                 # post contetnt in html formatted string
    # print("html_in", type(html_data))
    links = trafo.link_find(html_data)  # find all links in html formatted text and return in a list
    pics = trafo.pict_link(links)       # from link list slect all jpg link
    # print("kismain: ", post[0], post[1], post[2], links)
    # print("links: ",  links)
    post.append(pics)
    print(post[0:2], "pic: ",  post[4])
    