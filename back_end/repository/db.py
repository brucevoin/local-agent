
class Database:
    db = None
    def __init__(self):
        db = SqliteDatabase("data.db")
        
        
DATABASE = Database()   

