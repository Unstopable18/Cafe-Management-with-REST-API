from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schema import UserSchema, UserGetSchema,SuccessMessageSchema,UserOptionalQuerySchema,UserQuerySchema,UserOptionSchema
import hashlib
from flask_jwt_extended import create_access_token, get_jwt, jwt_required 
from blocklist import BLOCKLIST

blp=Blueprint("users",__name__,description="Operations GET, PUT, POST, DELETE")

@blp.route("/login")
class Userlogin(MethodView):

    def __init__(self):
        self.db=UserDatabase()

    @blp.arguments(UserSchema, location="query")
    def post(self,args):
        print(args)
        username= args.get("username")
        password= hashlib.sha256(args.get("password").encode('utf-8')).hexdigest()
        user_id=self.db.verify_user(username,password)
        if user_id:
            return {
                "access_token":create_access_token(identity=user_id)
            }
        abort(400, message="User not found")

@blp.route("/logout")
class Userlogout(MethodView):

    @jwt_required()
    def post(self):
        jti=get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Logged-out Successfully"}

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

    @blp.response(200,SuccessMessageSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def put(self,args):
        id= args.get("id")
        username= args.get("username")
        password= hashlib.sha256(args.get("password").encode('utf-8')).hexdigest()
        if self.db.put_user(id,username,password):
            return {"message":"User updated succesfully"},200
        else:
            abort(400, message="Id not found")


    @blp.arguments(UserSchema, location="query")
    @blp.response(201,SuccessMessageSchema)
    def post(self,args):
        username= args.get("username")
        password= hashlib.sha256(args.get("password").encode('utf-8')).hexdigest()
        if self.db.add_user(username,password):
            return {"message":"User added succesfully"},201
        else:
            abort(400,message="Username already exists") 
        

    @blp.arguments(UserOptionSchema, location="query")
    @blp.response(200,SuccessMessageSchema)
    def delete(self,args):
        id= args.get("id")
        if self.db.delete_user(id):
            return {"message":"User deleted succesfully"},200
        else:
            abort(400, message="Id not found") 
