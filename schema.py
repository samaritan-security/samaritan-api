# app/schema.py

from graphene import ObjectType, String, Schema


class Query(ObjectType):
    # this defines a Field 'hello' in our Schema with a single argument 'name'
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our resolver method takes the GraphQL context (root, info) as well as
    # argument (name) for the Field and returns data for the query response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'


schema = Schema(query=Query)