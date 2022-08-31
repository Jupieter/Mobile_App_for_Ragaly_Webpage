from unicodedata import name
import pymysql


class DB_questions():

  def db_get(self):
    #database connection
    con = pymysql.connect(
      host="127.0.0.1",   
      port=3306,
      user="root",          
      passwd="",            
      database="ragaly")
    # mydb = pymysql.connect(
    #   host="ragaly.hu", # 212.92.23.152
    #   port=3306,
    #   user="appfejleszt", 
    #   passwd="nNe4rF#pH7gRQ", 
    #   database="ngwpragaly")
    print(con)
    return con

  def post_ids(self): 
    rev = ""
    rev_old = ""
    con = self.db_get() 
    cur = con.cursor()
    sql =  "SELECT id, post_title, post_parent FROM wragalyp_posts WHERE post_type='revision' OR post_type='post' ORDER BY id DESC"
    # sql = "SELECT post_title FROM wragalyp_posts WHERE id=42624 "
    cur.execute(sql)
    myresult = cur.fetchall()

    # select the last revision posts
    htmls = []
    for x in myresult:
      rev = x[2]
      if rev != rev_old and rev_old != x[0]:
        rev_old = rev
        htmls.append(x)
        print(x[0], x[1], x[2])
        
      #for y in htmls:
      #  print(y)


if __name__ == '__main__':
    print('START MAIN')
    db = DB_questions()
    db.post_ids()

 


 
