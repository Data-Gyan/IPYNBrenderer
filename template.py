import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s : %(levelname)s] : %(message)s"
)

while True:
    project_name = input("Enter the project name : ")
    if project_name != '':
        break

logging.info(f"Creating project by name {project_name}")

#list of files
list_of_files = [
    ".gitignore",
    "README.md",
    "LICENSE",
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",                         # conda and other environment setup
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created a directory structure : {filedir}")
    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as new_file:
            logging.info(f"Creating a new file name {filename} in path {filedir}")
            pass
    else:
        logging.info(f"File {filepath} already exists")



