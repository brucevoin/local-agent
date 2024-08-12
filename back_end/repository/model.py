from repository.base_model import BaseModel
from peewee import *

class Model(BaseModel):
    model = CharField(unique=True,primary_key=True)
    base_url = CharField()
    api_key = CharField()
    description = CharField()