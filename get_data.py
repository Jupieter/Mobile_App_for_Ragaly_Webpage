# from unicodedata import name
import pymysql
class DB_questions():

  def db_get(self):
    '''database connection'''
    try:
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
    except:
        con = None
    return con
        

  
  def post_parent(self):
    '''It query the id the parent of the post 'Hírek' & 'Hirdetmények' '''
    con = self.db_get() 
    if con:
      cur = con.cursor()
      sql = """
      SELECT object_id
      FROM wragalyp_term_relationships 
      WHERE term_taxonomy_id = 33 OR term_taxonomy_id = 34 OR term_taxonomy_id = 1
      ORDER BY object_id DESC
      """
      cur.execute(sql)
      parent_result = cur.fetchall()
      cur.close()
      return parent_result

  def post_inherit(self, parent_result): 
    ''' All inherit of posts'''
    con = self.db_get() 
    if con:
      cur = con.cursor()
      params = {'c_l': parent_result}
      sql =  """
            SELECT id, post_parent
            FROM wragalyp_posts 
            WHERE post_parent IN %(c_l)s
            ORDER BY id DESC
            """
      cur.execute(sql, params)
      inherits_result = cur.fetchall()
      cur.close()
      return inherits_result

  def post_last(self, inherits_result):
    ''' The highest id of inherited in posts'''
    if inherits_result:
      inh_res = list(inherits_result)
      last_post_list =[]
      post_title = None
      for inh in inh_res:
        # print(inh[0], inh[1])
        if post_title != inh[1]:
          post_title = inh[1]
          last_post_list.append(inh[0])
      return last_post_list

  def post_data(self, last_post_list): 
    '''get  post's data from database'''
    if last_post_list: 
      tuple_list = tuple(last_post_list)
      params = {'tuple_l': tuple_list}
      con = self.db_get() 
      if con:
        cur = con.cursor()
        sql =  """
              SELECT id, post_title, post_parent, post_content, post_date
              FROM wragalyp_posts 
              WHERE id IN %(tuple_l)s
              ORDER BY id DESC
              """
        myresult_out = ["Semmi", "Semmi"]
        cur.execute(sql, params)
        myresult = cur.fetchall()
        myresult_out = list(myresult)
        cur.close()
        return myresult_out

  def list_from_tuple(self, post_data):
    if post_data:
      post_list_data =[]
      for post_tuple in post_data:
        post_list = list(post_tuple)
        post_list_data.append(post_list)
      return post_list_data
  
  def get_post_title(self, post_id):
    ''' This must to request of service'''
    con = self.db_get() 
    if con:
      cur = con.cursor()
      sql =  """
            SELECT post_title
            FROM wragalyp_posts 
            WHERE id = (%s)
            """
      cur.execute(sql, str(post_id))
      post_title = cur.fetchone()
      title = list(post_title)[0]
      cur.close()
      return title



  def runner(self):
    ''' main query chain'''
    parent_result = self.post_parent()
    print(parent_result)
    inherit_result = self.post_inherit(parent_result)
    for inherit in inherit_result:
      print(inherit)
    last_post_list = self.post_last(inherit_result)
    post_data = self.post_data(last_post_list)
    post_list_data = self.list_from_tuple(post_data)
    # for postdt in post_list_data:
    #   print(postdt[0],postdt[1])
    if last_post_list:
      max_post = len(last_post_list)
      print("last_post_list =", max_post, "post")
    else:
      max_post = 0
      last_post_list = None
      print("No Data. Maybe not internet connection")   
    
    title = self.get_post_title(41243)
    print("Title=  ", title)

    return post_list_data, max_post

    # parent_result = self.post_parent()
    # for prnt in parent_result:
    #   print(prnt)
    # inherit_result = self.post_inherit(parent_result)
    # for inherit in inherit_result:
    #   print(inherit)
    # last_post_list = self.post_last(inherit_result)
    # for post_id in last_post_list:
    #   print(post_id)
    # max_post = len(last_post_list)
    # post_data = self.post_data(last_post_list)
    # for postdt in post_data:
    #   print(postdt, max_post)
    # return post_data, max_post
  

if __name__ == '__main__':
    print('START MAIN')
    db = DB_questions()
    db.runner()

 


 
