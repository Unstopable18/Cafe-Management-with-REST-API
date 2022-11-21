from flask import Flask 

app = Flask(__name__)

items=[
    {
        'name':'Green Apple mojito',
        'price':160
    },
    {
        'name':'Momos',
        'price':60
    }
]

@app.get('/get-items')
def get_items():
    return {'items':items}