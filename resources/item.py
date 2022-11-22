from flask import request
import uuid
from db import items
from flask.views import MethodView
from flask_smorest import Blueprint
from schema import ItemSchema

blp=Blueprint("items",__name__,description="Operations GET, PUT, POST, DELETE")

@blp.route("/item")
class Item(MethodView):
    def get(self):
        id= request.args.get('id')
        if id is None:
            return items
        try:
            for item in items:
                if item['id']==id:
                    return item
        except KeyError:
            return {"message":"Item not found"}, 404

    @blp.arguments(ItemSchema)
    def put(self, request_data):
        # request_data=request.get_json()
        id= request.args.get('id')
        if id== None:
            return {"message":"Id not given"}, 404
        try:
            for item in items:
                if item['id']==id:
                    item['item']['name']=request_data['name']
                    item['item']['price']=request_data['price']
                    return {"message":"Item updated succesfully"},200
        except KeyError:
            return {"message":"Item not found"}, 404


    @blp.arguments(ItemSchema)
    def post(self,request_data):
        # request_data=request.get_json()
        # if 'name' not in request_data or 'price' not in request_data:
        #     return {"message":"'name' and 'price' must be in body"}, 400
        items[uuid.uuid4().hex]=request_data
        return {"message":"Item added succesfully"},201

    def delete(self):
        id= request.args.get('id')
        if id== None:
            return {"message":"Id not given"}, 404
        if id in items.keys():
            del items[id]
            return {"message":"Item deleted succesfully"},200
        return {"message":"Item not found"}, 404
