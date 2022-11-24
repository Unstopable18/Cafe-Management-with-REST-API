import pyodbc

class ItemDatabase:
    def __init__(self):
        self.conn=pyodbc.connect("DRIVER={SQL Server};Server=DESKTOP-LKH0TNU;Database=cafe;Trusted_Connection=True;")
        self.cursor=self.conn.cursor()

    def get_items(self):
        result=[]
        query="select * from items"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict={}
            item_dict['id']=row[0]
            item_dict['name']=row[1]
            item_dict['price']=row[2]
            result.append(item_dict)

        return result

    def get_item(self, item_id):
        query=f"select * from items where id='{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict={}
            item_dict['id'],item_dict['name'],item_dict['price']=row
            return [item_dict]

    def add_item(self, id, body_object):
        query=f"insert into items(id,name,price) values('{id}','{body_object['name']}',{body_object['price']})"
        self.cursor.execute(query)
        self.conn.commit()

    def put_item(self, id, body_object):
        query=f"update items set name='{body_object['name']}',price={body_object['price']} where id='{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount==0:
            return False
        else:
            self.conn.commit()
            return True

    def delete_item(self, item_id):
        query=f"delete from items where id='{item_id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount==0:
            return False
        else:
            self.conn.commit()
            return True

# db=ItemDatabase()
# db.get_items()




# items=[
#         {
#             'id':'',
#             'item':{
#                 'name':'Mojito',
#                 'price':160
#             }
#         },
#         {
#             'id':'96e51ad69e6c4fc1a3943f2a7970fc39',
#             'item':{
#                 'name':'Momos',
#                 'price':60
#             }
#         }
# ]