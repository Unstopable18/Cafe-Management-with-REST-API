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
            item_dict['id']=row[0]
            item_dict['name']=row[1]
            item_dict['price']=row[2]
            return [item_dict]

    def add_item(self, id, body_object):
        pass

    def put_item(self, id, body_object):
        pass

    def delete_item(self, item_id):
        pass

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