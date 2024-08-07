from peewee import *
from db import DATABASE

class BaseModel(Model):
    def to_dict(self):
        return self.__dict__.get('__data__')
    class Meta:
        database = DATABASE.db
        
        
        