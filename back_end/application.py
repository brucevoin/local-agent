from repository.model import Model
from repository.tool import Tool

class Application:
    def list_models():
        models = Model.select()
        return list(map(lambda i: i.to_dict(),models))
    
    def delete_model(id):
        pass
    
    def update_model(data):
        pass
    def udelete_model(data):
        pass
    
    
    def list_tools():
        pass
    
    def delete_tools(id):
        pass
    
    def create_tools(data):
        pass
    def update_tools(data):
        pass
    
    def run(message):
        pass
    
APPLICATION = Application()