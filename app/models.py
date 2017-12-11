from mongoengine import Document, StringField, ReferenceField

class User(Document):
    firstname = StringField(max_length=50)
    lastname  = StringField(max_length=50)
    username = StringField(max_length=50)
    password = StringField(max_length=50)
    email =  StringField(max_length=50, required=True)

class Todo(Document):
    description = StringField(max_length=50)
    owner = ReferenceField(User)
