from peewee import SqliteDatabase, Model

database = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = database         
    
    def to_dict(self):
        return self.__dict__.get('__data__')
 