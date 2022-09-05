from get_data import *
# from soap import *
import soap

teszt_db = 40
get_db = DB_questions()
posts = get_db.runner()                 # All last revisioned post
# print("get_db", get_db)

# trafo = HtmlTransformer

# print(posts)
i = 0
for post in posts:
    if i > teszt_db: break
    
    # print(post)
    html_data = post[3]                 # post contetnt in html formatted string
    # print("html_in", type(html_data))
    links = soap.link_find(html_data)  # find all links in html formatted text and return in a list
    pics = soap.pict_link(links)       # from link list slect all jpg link
    # print("kismain: ", post[0], post[1], post[2], links)
    # print("links: ",  links)
    post.append(pics)
    print(i, "--------------------- pictures --------------------------")
    print(post[0:2])
    print("pic: ",  post[4])
    i += 1

i = 0
for post in posts:
    if i > teszt_db: break
    html_data = post[3]                 # post contetnt in html formatted string
    bolded = soap.strong_murkup(html_data)
    html_txt = soap.text_find(html_data)
    print(i, "-------------------- text find ---------------------------" , post[0], post[1], post[2], post[4], post[5])
    print(html_txt)
    i += 1


    