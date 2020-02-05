# app/schema.py

from graphene import ObjectType, Schema, Field
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
from graphene.relay import Node

from models import User as UserModel


class User(MongoengineObjectType):

    class Meta:
        model = UserModel
        interfaces = (Node,)


class Query(ObjectType):
    node = Node.Field()
    all_users = MongoengineConnectionField(User)
    user = Field(User)


schema = Schema(query=Query, types=[User])
