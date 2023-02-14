# from time import ctime
# import shutil
# from pathlib import Path
# from zipfile import ZipFile
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["trancaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])


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
