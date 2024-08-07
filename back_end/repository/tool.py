from base_model import BaseModel
from peewee import *

class Tool(BaseModel):
    name = CharField(unique=True,primary_key=True)
    description = CharField()
    Code = CharField(max_length=255)