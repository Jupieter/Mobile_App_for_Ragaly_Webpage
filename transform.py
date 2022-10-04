from get_data import *
import soap


def transform(posts):
    i = 0
    for post in posts:
        # if i > teszt_db: break
        html_data = post[3] 
        print(post[1])                # post contetnt in html formatted string
        links = soap.link_find(html_data)   # find all links in html formatted text and return in a list
        pics = soap.pict_link(links)        # from link list slect all jpg link
        # print(pics)
        post.append(pics)                   # pictures added to list item-5
        # print(i, "--------------------- pictures --------------------------")
        # print(post[0:2])
        # print("pic: ",  post[5])
        i += 1

    i = 0
    for post in posts:
        # if i > teszt_db: break
        html_data = post[3]                     # post contetnt in html formatted string
        bolded = soap.strong_murkup(html_data)  # change <strong> to [b]
        html_txt = soap.text_find(bolded)  
        post[3] = html_txt
        print(i, "-------------------- text find ---------------------------" , post[0], post[1], post[2], post[4])
        # print( post[5])
        # print("html_txt ", i,": ", html_txt)
        i += 1
    
    return posts

if __name__ == '__main__':
    print('START TRANSFORM')
    teszt_db = 40
    get_db = DB_questions()
    posts, max_post = get_db.runner()                 # All last revisioned post
    transform(posts) 

