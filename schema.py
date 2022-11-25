from marshmallow import Schema, fields

class UserSchema(Schema):
    username=fields.Str(required=True)
    password=fields.Str(required=True)

class UserOptionSchema(Schema):
    id=fields.Int(required=True)

class UserGetSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True, load_only=True)

class SuccessMessageSchema(Schema):
    message=fields.Str(dump_only=True)

class UserQuerySchema(Schema):
    id=fields.Int(required=True)
    username=fields.Str(required=True)
    password=fields.Str(required=True)

class UserOptionalQuerySchema(Schema):
    id=fields.Int(required=False)

class ItemSchema(Schema):
    name=fields.Str(required=True)
    price=fields.Int(required=True)

class ItemGetSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(dump_only=True)
    price=fields.Int(dump_only=True)

class ItemQuerySchema(Schema):
    id=fields.Int(required=True)

class ItemOptionalQuerySchema(Schema):
    id=fields.Int(required=False)

