from pathlib import Path
from tomllib import load
from random import choice

with open("tasks.toml", "rb") as f:
    tasks = load(f)["tasks"]

students = []
for name in [p.name for p in Path(".").glob("*") if (p.is_dir() and p.name.find('_')>=0)]:
    if len(tasks) == 0:
        raise RuntimeError("задачи кончились")
    print(name)
    task = choice(tasks)
    tasks.remove(task)
    print(task)
    print()
