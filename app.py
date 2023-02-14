# from time import ctime
# import shutil
from pathlib import Path
# from zipfile import ZipFile
# import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()
duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())

# dt = datetime.strptime("2023/02/14", "%Y/%m/%d")
# datetime.fromtimestamp(time.time())

# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m"))

# print(dt2 > dt1)


# def send_emails():
#     for i in range(10000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)


# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)


# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1993}
# ]
# data = json.dumps(movies)

# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[0]["title"])

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
