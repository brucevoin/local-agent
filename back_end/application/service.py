from repository.model import Model
from repository.tool import Tool

from domain.model import Model as DomainModel
from domain.tool import Tool as DomainTool
from domain.agent_v1 import Agent_v1


class Service:
    def list_models(self):
        models = list(Model.select())
        return list(map(lambda i: i.to_dict(), models))

    def delete_model(self, id):
        Model.delete_by_id(id)

    def update_model(self, data):
        new_model = Model(
            model=data["model"],
            base_url=data["base_url"],
            api_key=data["api_key"],
            description=data["description"],
        )
        new_model.update()

    def create_model(self, data):
        Model.create(
            model=data["model"],
            base_url=data["base_url"],
            api_key=data["api_key"],
            description=data["description"],
        )

    def list_tools(self):
        tools = list(Tool.select())
        return list(map(lambda i: i.to_dict(), tools))

    def delete_tool(self, id):
        Tool.delete_by_id(id)

    def create_tools(self, data):
        tool = Tool(
            name=data["name"], description=data["description"], code=data["code"]
        )
        tool.create()

    def update_tools(self, data):
        tool = Tool(
            name=data["name"], description=data["description"], code=data["code"]
        )
        tool.update()

    def run(self, message, models, tools, tempreture, max_consecutive_replay):
        if models and isinstance(models, list) and len(models) > 0:
            domain_models = list(
                map(
                    lambda x: DomainModel(x["model"], x["base_url"], x["api_key"]),
                    models,
                )
            )
            domain_tools = list(
                map(
                    lambda tool: DomainTool(
                        tool["name"],
                        tool["description"],
                        tool["code"],
                        tool["dependences"],
                    )
                )
            )
            autogen = Agent_v1(domain_models, domain_tools)
            res = autogen.run(message=message)
            return {"chat_history": res.chat_history, "summary": res.summary}
        else:
            raise (Exception("You must select at least one model"))

    def init(self):
        Model.create_table(safe=True)
        Tool.create_table(safe=True)


APPLICATION = Service()
