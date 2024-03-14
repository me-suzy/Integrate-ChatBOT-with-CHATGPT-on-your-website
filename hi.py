import os

# Get the absolute path to the database file
database_path = os.path.join(os.path.dirname(__file__), "database articles (english)[1].txt")

# Open and read the database file
with open(database_path, "r") as file:
content = file.read().strip()
print(content)