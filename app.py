from time import ctime
import shutil
from pathlib import Path
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
from datetime import datetime, timedelta
import random
import string
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import smtplib
import sys
import subprocess

try:
    completed = subprocess.run(["python3", "other.py"],
                               capture_output=True,
                               text=True,
                               check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)


# if len(sys.argv) == 1:
#     print("USAGE: python3 app.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)

# template = Template(Path("template.html").read_text())


# message = MIMEMultipart()
# message["from"] = "Justin Sixsmith"
# message["to"] = "testuser@codewithmosh.com"
# message["subject"] = "This is a test"
# body = template.substitute(name="John")
# message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("justin.jpeg").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
#     smtp.send_message(message)
#     print("Sent...")


# print("Deployment completed")
# webbrowser.open("http://google.com")

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)


# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
# print(dt1)
# dt2 = datetime.now()
# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total seconds", duration.total_seconds())

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
