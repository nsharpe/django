from django.http import HttpResponse
import json
import sqlite3

con = sqlite3.connect("attributes.sqlite3")

class AttributeDefinition:
    def __init__(self,
                 id,
                 description,
                 type):
        self.id = id
        self.description = description
        self.type = type

def reset():
    con.execute("delete from sqlite_master where type in ('table', 'index', 'trigger');")

def attributes(request):
    return HttpResponse(json.dumps(listAttributes()))

def listAttributes():
    return ["a",
            "b",
            "c",
            "d"]