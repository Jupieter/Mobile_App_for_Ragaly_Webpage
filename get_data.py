# from unicodedata import name
import pymysql


class DB_questions():

  def db_get(self):
    '''database connection'''
    # con = pymysql.connect(
    #   host="127.0.0.1",   
    #   port=3306,
    #   user="root",          
    #   passwd="",            
    #   database="ragaly")
    con = pymysql.connect(
       host="ragaly.hu", # 212.92.23.152
       port=3306,
       user="appfejleszt", 
       passwd="nNe4rF#pH7gRQ", 
       database="ngwpragaly")
    print(con)
    return con

  def post_rev(self): 
    '''get all posts from database'''
    con = self.db_get() 
    cur = con.cursor()
    sql =  "SELECT id, post_title, post_parent, post_content FROM wragalyp_posts WHERE post_type='revision' OR post_type='post' ORDER BY id DESC"
    # sql = "SELECT post_title FROM wragalyp_posts WHERE id=42624 "
    cur.execute(sql)
    myresult = cur.fetchall()
    return myresult

  def post_ids(self, myresult_in):
    '''select the last post revision id'''
    rev = ""
    rev_old = ""
    i = 0
    # select the last revision posts
    posts = []
    myresult = myresult_in
    for x in myresult:
      rev = x[2]
      if rev != rev_old and rev_old != x[0]:
        rev_old = rev
        posts.append(x)
        i +=1
      #  print(x[0], x[1], x[2])
    print(i)
    return posts    

  def strong_murkup(self, html_in):
    ''' change the html <strong> to kivy [b] '''
    html_out1 = html_in.replace("</strong>", "[/b]")
    html_out = html_out1.replace("<strong>", "[b]")
    print(html_out)
    return html_out

  def html_transform(self, posts_in):
    '''change al html post mark up to kivy mark up'''
    posts = posts_in
    htmls = []
    for post in posts:
      html_act =post[3]
      print("első: ",html_act)
      html_tr = self.strong_murkup(html_act)
      # print("második: ", html_tr)
      post[3] = html_tr
      print(post[3])
      print(post)
      # htmls.append(html_act)
    return posts


  def runner(self):
    myresult = self.post_rev()
    posts = self.post_ids(myresult)
    # htmls = self. strong_murkup(posts)
    post1 = posts[0]
    print(post1)
    htmls = self. strong_murkup(posts)
    print(htmls)



if __name__ == '__main__':
    print('START MAIN')
    db = DB_questions()
    db.runner()

 


 
