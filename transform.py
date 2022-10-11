from get_data import *
import soap


def transform(posts):
    i = 0
    for post in posts:
        html_data = post[3] 
        # print(post[3])                # post contetnt in html formatted string
        links = soap.link_find(html_data)   # find all links in html formatted text and return in a list
        post.append(links)                   # pictures added to list item-5
        pics = soap.pict_link(links)        # from link list slect all jpg link
        post.append(pics)                   # pictures added to list item-5
        i += 1

    i = 0
    for post in posts:
        html_data = post[3]                     # post contetnt in html formatted string
        bolded = soap.strong_murkup(html_data)  # change <strong> to [b]
        html_txt = soap.text_find(bolded)  
        post[3] = html_txt
        # print(i, "-------------------- text find ---------------------------" , post[0], post[1], post[2])
        i += 1
    
    return posts

if __name__ == '__main__':
    print('START TRANSFORM')
    teszt_db = 40
    get_db = DB_questions()
    posts, max_post = get_db.runner("page")                 # All last revisioned post
    transform(posts) 

