# app/schema.py

from graphene import ObjectType, String, Schema, List
from pymongo import MongoClient
from graphene_mongo import MongoengineObjectType

from models import User as UserModel

client: MongoClient = MongoClient("localhost:27017")
db = client.user


class User(MongoengineObjectType):
    class Meta:
        model = UserModel


class Query(ObjectType):
    # this defines a Field 'hello' in our Schema with a single argument 'name'
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    users = List(User)

    # our resolver method takes the GraphQL context (root, info) as well as
    # argument (name) for the Field and returns data for the query response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

    def resolve_users(self, info):
        return list(UserModel.objects.all())


schema = Schema(query=Query)
