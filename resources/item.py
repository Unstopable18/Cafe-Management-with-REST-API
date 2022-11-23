from flask import request
import uuid
from db import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schema import ItemSchema, ItemGetSchema,SuccessMessageSchema,ItemOptionalQuerySchema,ItemQuerySchema

blp=Blueprint("items",__name__,description="Operations GET, PUT, POST, DELETE")

@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db=ItemDatabase()

    @blp.response(200,ItemGetSchema(many=True)) 
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self,args):
        id= args.get("id")
        if id is None:
            return self.db.get_items()
        # for item in self.db.get_items():
        #     if item["id"]==id:
        #         return [item]
        # abort(400, message="Id not found")
        else:
            return self.db.get_item(id)

    @blp.arguments(ItemSchema)
    @blp.response(200,SuccessMessageSchema)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data,args):
        id= args.get("id")
        for item in self.db.get_items():
            if item["id"]==id:
                item["item"]["name"]=request_data["name"]
                item["item"]["price"]=request_data["price"]
                return {"message":"Item updated succesfully"},200
        abort(400, message="Id not found")


    @blp.arguments(ItemSchema)
    @blp.response(201,SuccessMessageSchema)
    def post(self,request_data):
        item={
            "id":uuid.uuid4().hex,
            "item":{
                "name":request_data["name"],
                "price":request_data["price"]
            }
        }
        items.append(item)
        return {"message":"Item added succesfully"},201

    @blp.arguments(ItemQuerySchema, location="query")
    @blp.response(200,SuccessMessageSchema)
    def delete(self,args):
        id= args.get("id")
        for item in self.db.get_items():
            if item["id"]==id:
                items.remove(item)
                return {"message":"Item deleted succesfully"},200
        abort(400, message="Id not found")
