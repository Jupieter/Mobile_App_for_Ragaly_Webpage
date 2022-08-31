import pymysql


class DB_questions():

  def db_get():
    #database connection
    mydb = pymysql.connect(
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
    print(mydb)
    return mydb

  def post_titles(self): 
    mydb = self.db_get() 
    mycursor = mydb.cursor()
    # sql =  mycursor.execute("SELECT post_title FROM wragalyp_posts WHERE post_type='revision' OR post_type='post' ")
    sql = "SELECT post_content FROM wragalyp_posts WHERE id=42624 "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    htmls = []
    for x in myresult:
      htmls.append(str(x))
      # print(x)

# importing the library

 


 
