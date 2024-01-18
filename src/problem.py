import os

class Problem:
    def __init__(self, path):
        self.TESTS = f"{path}/test.py"
        self.SPECS = f"{path}/specs.md"
        self.MAIN = f"{path}/main.py"
        # read the files and store them in memory
        with open(self.TESTS, "r") as f:
            self.tests = f.read()
        with open(self.SPECS, "r") as f:
            self.specs = f.read()
        with open(self.MAIN, "r") as f:
            self.main = f.read()
    
    def write_problems(self, path):
        with open(f"{path}/test.py", "w") as f:
            f.write(self.tests)
        with open(f"{path}/specs.md", "w") as f:
            f.write(self.specs)
        with open(f"{path}/main.py", "w") as f:
            f.write(self.main)


if __name__ == "__main__":
    pwd = os.path.dirname(os.path.realpath(__file__))
    problem = os.path.join(pwd, "problems/no_duplicates")
    problem = Problem(problem)

