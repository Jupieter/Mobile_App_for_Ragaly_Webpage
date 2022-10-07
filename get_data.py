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
        

  
  def post_parent(self, post_page):
    '''It query the id the parent of the post 'Hírek' & 'Hirdetmények' '''
    if post_page == "post":
      con = self.db_get() 
      if con:
        cur = con.cursor()
        sql = """
          SELECT wragalyp_posts.ID
          FROM wragalyp_posts 
          INNER JOIN wragalyp_term_relationships
          ON wragalyp_posts.ID = wragalyp_term_relationships.object_id 
          WHERE wragalyp_posts.post_status = "publish" AND wragalyp_posts.ID
          IN (
           SELECT object_id
           FROM wragalyp_term_relationships 
           WHERE term_taxonomy_id IN %(categorie)s
           ORDER BY object_id DESC
          )
          ORDER BY wragalyp_posts.ID DESC
        """
        params = {'categorie': (1,33,34)}
        cur.execute(sql, params)
        parent_result = cur.fetchall()
        cur.close()
    else:
      # parent_result = tuple(306, 303)
      parent_result = ((10209,), (10205,), (10201,), (390,), (384,), (312,), (303,))
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
            ORDER BY post_parent DESC, id DESC
            """
      cur.execute(sql, params)
      inherits_result = cur.fetchall()
      cur.close()
      print(inherits_result)
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
      print(last_post_list)
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

  def get_post_name(self, post_id):
    ''' This must to request of service'''
    con = self.db_get() 
    if con:
      cur = con.cursor()
      sql =  """
            SELECT post_name
            FROM wragalyp_posts 
            WHERE id = (%s)
            """
      cur.execute(sql, str(post_id))
      post_name = cur.fetchone()
      name = list(post_name)[0]
      cur.close()
      return name



  def runner(self, post_page = "post"):
    ''' main query chain'''
    parent_result = self.post_parent(post_page)
    # print("parent_result:  ", parent_result)
    inherit_result = self.post_inherit(parent_result)
    last_post_list = self.post_last(inherit_result)
    post_data = self.post_data(last_post_list)
    post_list_data = self.list_from_tuple(post_data)
    if last_post_list:
      max_post = len(last_post_list)
    else:
      max_post = 0
      last_post_list = None
      # print("No Data. Maybe not internet connection")   
    return post_list_data, max_post


  

if __name__ == '__main__':
    print('START MAIN')
    db = DB_questions()
    db.runner()

 


 
