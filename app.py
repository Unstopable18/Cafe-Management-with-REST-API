from flask import Flask, request
import uuid
from db import items

app = Flask(__name__)

@app.get('/items')
def get_items():
    return {'items':items}
    #return {'items':list(items.values())}  #to remove id 

@app.post('/item')
def add_item():
    #request_data=request.get_json()
    #items.append(request_data)
    items[uuid.uuid4().hex]=request.get_json()
    return {"message":"Item added succesfully"},201

# @app.get('/get-item/<string:name>')
# def get_item(name):
#     for item in items:
#         if name == item['name']:
#             return item
#     return {"message":"Item not found"}

# @app.get('/item')
# def get_item():
#     name= request.args.get('name')
#     for item in items:
#         if name == item['name']:
#             return item
#     return {"message":"Item not found"}, 404

@app.get('/item')
def get_item():
    id= request.args.get('id')
    try:
        return items[id]
    except KeyError:
        return {"message":"Item not found"}, 404

@app.put('/item')
def update_item():
    # request_data=request.get_json()
    # for item in items:
    #     if item['name']==request_data['name']:
    #         item['price']=request_data['price']
    #         return {"message":"Item updated succesfully"},200
    id= request.args.get('id')
    if id in items.keys():
        items[id]=request.get_json()
        return {"message":"Item updated succesfully"},200
    else:
        return {"message":"Item not found"}, 404

@app.delete('/item')
def delete_item():
    # name= request.args.get('name')
    # for item in items:
    #     if name == item['name']:
    #         items.remove(item)
    #         return {"message":"Item deleted succesfully"}
    id= request.args.get('id')
    if id in items.keys():
        del items[id]
        return {"message":"Item deleted succesfully"},200
    else:
        return {"message":"Item not found"}, 404
