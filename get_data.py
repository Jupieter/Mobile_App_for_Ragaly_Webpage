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
    sql =  """
          SELECT id, post_title, post_parent, post_content 
          FROM wragalyp_posts 
          WHERE post_type='revision' OR post_type='post' 
          ORDER BY post_parent ASC
          """
    # sql = "SELECT post_title FROM wragalyp_posts WHERE id=42624 " , id DESC
    cur.execute(sql)
    myresult = cur.fetchall()
    myresult_out = list(myresult)
    return myresult_out
  
  def tuple_to_list(self, datas):
    post_list = []
    for data in datas:
      x = list(data)
      post_list.append(x)
    return post_list


  def zero_post_type(self, myresult_in):
    '''change post_parent zero value to own id value'''
    print(type(myresult_in))
    for post in myresult_in:
      if post[2] != 0:
        break
      elif post[2] == 0:
        post[2] = post[0]
        print("csere", post[0], post[2]) # type(post[2])
    print("----------------------------------------------------------")
    myresult_out = sorted(myresult_in, key=lambda x: x[0], reverse=True)
    for post in myresult_out:
      print("have zero? : ", post[0], post[2])
    return myresult_out


  def post_ids(self, myresult_in):
    '''select the last post revision id'''
    rev = ""
    rev_old = ""
    i = 0
    myresult = myresult_in
    for x in myresult:
      print(x[0],x[2])
    sortol = sorted(myresult, key=lambda x: x[0])
    for x in sortol:
      print("na ez: ", x[0],x[2])
    print("----------------------------------------------------------")
    # select the last revision posts
    posts = []
    for x in myresult:
      rev = x[2]
      if rev != rev_old  and x[3] != "": # and rev_old != x[0]
        rev_old = rev
        posts.append(x)
        i +=1
        print("appendált: ",x[0], x[1], x[2])
    print(i)
    return posts    

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


  def runner(self):
    myresult = self.post_rev()
    post_lst = self.tuple_to_list(myresult)
    post_zero = self.zero_post_type(post_lst)
    

    # posts = self.zero_post_type(myresult)
    # posts = self.post_ids(myresult)
    # for post in posts:
    #   print(post[0:3])
    # htmls = self. html_transform(posts)
    # for x in htmls:
    #   print(x)



if __name__ == '__main__':
    print('START MAIN')
    db = DB_questions()
    db.runner()

 


 
