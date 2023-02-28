# f = open("sample.txt", "w")
# f.write("Some text")
# f.close()
import os
from contextlib import contextmanager

# Checking Whats in your dir
cwd = os.getcwd()
os.chdir("Sample-Dir-One")
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir("Sample-Dir-Two")
print(os.listdir())
os.chdir(cwd)


# Now we don't have to remember to do it on our own each time with this.
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("Sample-Dir-One"):
    print(os.listdir())

with change_dir("Sample-Dir-Two"):
    print(os.listdir())
    # Another Check
    # @contextmanager
    # def open_file(file, mode):
    #     try:
    #         f = open(file, mode)
    #         yield f
    #     finally:
    #         f.close()

    # with open_file("sample.txt", "w") as f:
    #     f.write("Some text")

    # CONTEXT MANAGER IN CLASS
    # class Open_File():

    #     def __init__(self, filename, mode):
    #         self.filename = filename
    #         self.mode = mode

    #     def __enter__(self):
    #         self.file = open(self.filename, self.mode)
    #         return self.file

    #     def __exit__(self, exc_type, exc_val, traceback):
    #         self.file.close()

    # if __name__ == "__main__":
    #     with Open_File("sample.txt", "w") as f:
    #         f.write("Testing")

    # Another Check
    # print(f.closed)
