import os
import re
import shutil
import itertools
from pathlib import Path
from loguru import logger
from datetime import datetime


def create_file(filename):
    if os.path.exists(filename):
        raise FileExistsError
    else:
        with open(filename, "x+") as file:
            file.close()

def get_suffix(filename):
    return filename.split(".")[-1]


def check_file_path():
    curr_dir = os.getcwd()
    cmd = "../projects"
    logger.debug(curr_dir)
    logger.debug(os.path.relpath(cmd))
    logger.debug(os.path.realpath(cmd))


def resolve_file_path():
    '''Resolves from current working directory.'''
    p = Path("../projects")
    r = p.resolve()
    logger.debug(p)
    logger.debug(r)

def glob_check():
    p = Path('/home/development/Downloads/Themes')
    dirs = [d for d in p.glob("*") if d.is_dir()]
    logger.debug(len(dirs))
    logger.debug(len([d for d in p.rglob("*") if d.is_dir()]))
    regex = r"^(?:com.)(\w+).(\w+)(?:[-large]*)(?:.png)$"
    target = "com.apple.AppStore-large.png"
    res = re.match(regex, target)
    logger.debug(res[2])

def get_file_size(filename, units=None):
    file_path = Path(filename)
    file_bytes = file_path.stat().st_size
    if units == "GB":
        size_divisor = 1000000000
    elif units == "MB":
        size_divisor = 1000000
    elif units == 'KB':
        size_divisor = 1000
    else:
        size_divisor = 1
    file_size = round(file_bytes / size_divisor, 2)
    logger.debug(file_size)


def walk_dir(root_path="."):
    for root, dirs, files in os.walk(root_path, topdown=False):
        for f in files:
            filename = Path(os.path.join(root, f))
            sub_dir = filename.parent.name
            name = filename.name
            sub_dir = Path(root).name
            print(sub_dir, name, str(filename))
        #for name in dirs:
        #    print(os.path.join(root, name))

def get_modified_date(file_path):
    file = Path(file_path)
    m_time = file.stat().st_mtime
    modified_date = datetime.fromtimestamp(m_time)
    return modified_date


if __name__ == "__main__":
    resolve_file_path()
    logger.debug("{:08b}".format(ord('7')))
    a = set([1,2,3,4,5,6])
    b = set([2, 3, 4, 5, 6, 7, 8])
    c = len(list(itertools.product(a, b)))
    logger.debug(c)
    get_file_size("snippets/file_utils.py")
    print(get_modified_date("/home/development/toolkit/snippets/file_utils.py"))
    #walk_dir("/home/development/toolkit")
