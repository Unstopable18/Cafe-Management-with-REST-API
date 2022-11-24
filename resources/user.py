import uuid
from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schema import UserSchema, UserGetSchema,SuccessMessageSchema,UserOptionalQuerySchema,UserQuerySchema

blp=Blueprint("users",__name__,description="Operations GET, PUT, POST, DELETE")

@blp.route("/user")
class user(MethodView):

    def __init__(self):
        self.db=UserDatabase()

    @blp.response(200,UserGetSchema(many=True)) 
    @blp.arguments(UserOptionalQuerySchema, location="query")
    def get(self,args):
        id=args.get("id")
        print('id===',type(id))
        if id is None:
            return self.db.get_users()
        else:
            result= self.db.get_user(id)
            if result is None:
                abort(400, message="Id not found")
            return result

    @blp.arguments(UserSchema)
    @blp.response(200,SuccessMessageSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def put(self,**args):
        print(args)
        id= args.get("id")
        username= args.get("username")
        password= args.get("password")
        if self.db.put_user(id,username,password):
            return {"message":"user updated succesfully"},200
        else:
            abort(400, message="Id not found")


    @blp.arguments(UserSchema)
    @blp.response(201,SuccessMessageSchema)
    def post(self,args):
        id = uuid.uuid4().hex
        username= args.get("username")
        password= args.get("password")
        self.db.add_user(id,username,password)
        return {"message":"user added succesfully"},201

    @blp.arguments(UserQuerySchema, location="query")
    @blp.response(200,SuccessMessageSchema)
    def delete(self,args):
        id= args.get("id")
        if self.db.delete_user(id):
            return {"message":"user deleted succesfully"},200
        else:
            abort(400, message="Id not found") 
