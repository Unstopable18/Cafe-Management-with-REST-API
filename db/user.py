import pyodbc

class UserDatabase:
    def __init__(self):
        self.conn=pyodbc.connect("DRIVER={SQL Server};Server=DESKTOP-LKH0TNU;Database=cafe;Trusted_Connection=True;")
        self.cursor=self.conn.cursor()

    def get_users(self):
        result=[]
        query="select * from users"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            user_dict={}
            user_dict['id'],user_dict['username'],user_dict['password']=row
            result.append(user_dict)
        return result

    def get_user(self, user_id):
        query=f"select * from users where id='{user_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            user_dict={}
            user_dict['id'],user_dict['username'],user_dict['password']=row
            return [user_dict]
            

    def add_user(self, username,password):
        try:
            query=f"insert into users(username,password) values('{username}','{password}')"
            self.cursor.execute(query)
            if self.cursor.rowcount==0:
                return False
            else:
                self.conn.commit()
                return True
        except:
            return False

    def put_user(self, id, username,password):
        query=f"update users set username='{username}',password='{password}' where id='{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount==0:
            return False
        else:
            self.conn.commit()
            return True

    def delete_user(self, user_id):
        query=f"delete from users where id='{user_id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount==0:
            return False
        else:
            self.conn.commit()
            return True

# db=UserDatabase()
# db.get_user(1)




# users=[
#         {
#             'id':'',
#             'user':{
#                 'username':'Mojito',
#                 'password':160
#             }
#         },
#         {
#             'id':'96e51ad69e6c4fc1a3943f2a7970fc39',
#             'user':{
#                 'username':'Momos',
#                 'password':60
#             }
#         }
# ]