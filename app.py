from pathlib import Path

path = Path("ecommerce")

paths = [p for p in path.iterdir()]
print(paths)
