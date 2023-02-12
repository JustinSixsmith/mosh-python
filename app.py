from pathlib import Path
from time import ctime

path = Path("ecommerce/__init__.py")
print(ctime(path.stat().st_ctime))


# paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.rglob("*.py")]
# print(py_files)
