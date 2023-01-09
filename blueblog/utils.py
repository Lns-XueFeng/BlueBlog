import os


dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

print("sqlite:///" + os.path.join(dir, "data-dev.db"))
