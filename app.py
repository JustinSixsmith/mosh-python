from pathlib import Path

path = Path("ecommerce")

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)
