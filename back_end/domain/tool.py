class Tool:
    _name = None
    _description = None
    _code = None
    _dependences = None
    
    base_dir = "user_functions"

    def __init__(self, name, description, code, dependences):
        self._name = name
        self._description = description
        self._code = code
        self._dependences = dependences

        self.package_name = name
        self.module_name = name

        self._init_package()

    def _init_package(self):
        os.makedirs(self.base_dir + self.package_name, exist_ok=True)
        file_path = self.base_dir + self.package_name + "/__init__.py"
        with open(file_path, "w") as file:
            file.write(f"from .{self.module_name} import *")
        return

    def write_to_file(self):
        file_path = self.base_dir + self.package_name + f"/{self.module_name}.py"
        with open(file_path, "w") as file:
            file.write(self.code)
        return ".".join(
            ["user_functions", self.package_name, self.module_name]
        )

    def install_dependences(self):
        if self.dependences and len(self.dependences) > 0:
            target_directory = self.base_dir + self.package_name + "/packages/"
            packages = " ".join(self.dependences)
            command = ["pip", "install", "--target", target_directory, packages]
            try:
                result = subprocess.run(command, check=True)
                if result.returncode == 0:
                    print("Package installed successfully.")
                else:
                    print("Failed to install package")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while installing the package: {e}")

    def check_syntax(self):
        file_path = self.base_dir + self.package_name + f"/{self.module_name}.py"
        command = ["python", "-m", "py_compile", file_path]
        try:
            result = subprocess.run(command, check=True)
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing the package: {e}")
            return False
