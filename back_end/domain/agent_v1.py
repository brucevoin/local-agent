import autogen
from autogen.coding import LocalCommandLineCodeExecutor
from autogen import register_function
import importlib
import os

from domain.model import Model as DomainModel
from domain.tool import Tool as DomainTool


class Agent_v1:

    _userproxy = None
    _assistant = None

    _models = None
    _tools = None

    _workdir = "workdir"

    _llm_config = None

    def __init__(self, models: [DomainModel], tools: [DomainTool]):

        os.makedirs(self._workdir, exist_ok=True)
        self._models = models
        self._tools = tools

        self._config_llm()

        self._userproxy = autogen.UserProxyAgent(
            name="Userproxy",
            is_termination_msg=lambda msg: msg.get("content") is not None
            and "TERMINATE" in msg["content"],
            llm_config=self._llm_config,
            code_execution_config={
                "executor": LocalCommandLineCodeExecutor(work_dir=self._workdir),
            },
        )
        self._assistant = autogen.AssistantAgent(
            name="Assistant",
            is_termination_msg=lambda msg: msg.get("content") is not None
            and "TERMINATE" in msg["content"],
            llm_config=[],
        )
        if tools and isinstance(tools, list) and len(tools) > -1:
            for tool in tools:
                domain_tool = DomainTool(
                    tool["name"], tool["description"], tool["code"], tool["dependences"]
                )
                module_name = domain_tool.write_to_file()
                domain_tool.install_dependences()
                domain_tool.check_syntax()
                
                self._register_tool(module_name=module_name,function_name=domain_tool._name,description=domain_tool._description)

    def _config_llm(self):
        self._llm_config = {
            "config_list": list(map(lambda x: x.to_config(), self._models))
        }

    def _register_tool(self, module_name, function_name, description):
        """
        工具注册步骤

        1. 将用户定义的函数（字符串）写入文件（在特定的模块里），记录模块名、包名、函数名
        2. 使用模块名模块名、包名、函数名，动态导入

        比如，已经将用户函数写入到mymodule.py 文件，结构如下:
        -----------------
        mypackage/
            __init__.py
            mymodule.py
        -----------------

        其中， mymodule.py的内容如下：
        ------------------
        def my_function():
            print("Hello from my_function!")
        ------------------

        要注册my_function,则采用如下方式：
        -------------------
        agent.register_tool(
            module_name = "mypackage.mymodule", function_name="my_function", description = "Currency exchange calculator."
        )
        ------------------
        """
        print("register tool:")
        print(f"module: {module_name}")
        print(f"function: {function_name}")
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)

        register_function(
            function,
            caller=self._assistant,  # The assistant agent can suggest calls to the calculator.
            executor=self._userproxy,  # The user proxy agent can execute the calculator calls.
            name=function_name,  # By default, the function name is used as the tool name.
            description=description,  # A description of the tool.
        )
        
    def run(self, message):
        chat_res = self._userproxy.initiate_chat(
            self._assistant,
            message=message,
            summary_method=self._summary_method,
            summary_args={"summary_prompt":"Summarize the takeaway and translate it to chinese from the conversation. Do not add any introductory phrases."},
            clear_history=True,
        )
        self._executor.stop()
        return chat_res
