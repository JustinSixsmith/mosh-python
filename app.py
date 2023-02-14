# from time import ctime
# import shutil
from pathlib import Path
# from zipfile import ZipFile
# import csv
import json

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("files.zip") as zip:
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")

# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"
# shutil.copy(source, target)


# print(ctime(path.stat().st_ctime))
# print(path.read_text())


# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)
