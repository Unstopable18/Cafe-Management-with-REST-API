import uuid
from flask_jwt_extended import jwt_required
from db.item import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schema import ItemSchema, ItemGetSchema,SuccessMessageSchema,ItemOptionalQuerySchema,ItemQuerySchema

blp=Blueprint("items",__name__,description="Operations GET, PUT, POST, DELETE")

@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db=ItemDatabase()

    @jwt_required()
    @blp.response(200,ItemGetSchema(many=True)) 
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self,args):
        id= args.get("id")
        if id is None:
            return self.db.get_items()
        else:
            result=self.db.get_item(id)
            if result is None:
                abort(400, message="Id not found")
            return result

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(200,SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data,args):
        id= args.get("id")
        if self.db.put_item(id,request_data):
            return {"message":"Item updated succesfully"},200
        else:
            abort(400, message="Id not found")

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201,SuccessMessageSchema)
    def post(self,request_data):
        id = uuid.uuid4().hex
        self.db.add_item(id,request_data)
        return {"message":"Item added succesfully"},201

    @jwt_required()
    @blp.arguments(ItemQuerySchema, location="query")
    @blp.response(200,SuccessMessageSchema)
    def delete(self,args):
        id= args.get("id")
        if self.db.delete_item(id):
            return {"message":"Item deleted succesfully"},200
        else:
            abort(400, message="Id not found")
