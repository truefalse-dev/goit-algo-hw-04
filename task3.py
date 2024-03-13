import sys
from pathlib import Path
from colorama import Fore, Back

BOLD_INIT = '\033[1m'
BOLD_RESET = '\033[0m'

try:
    path = Path(sys.argv[1])
except IndexError as err:
    print('you have to provide a path')
    exit()


items = [(0, path.name, 'd')]


def read_path(path, shift=0):
    shift += 1
    for item in path.iterdir():
        if item.is_dir():
            items.append((shift, item.name, 'd'))
            read_path(item, shift)
        else:
            items.append((shift, item.name, 'f'))


def shift_build(k, type):
    return ' ' * k + ('📄' if type == 'f' else '📁')


try:
    read_path(path)
except FileNotFoundError as err:
    print(err)
    exit()


for item in items:
    fore_folders_files = Fore.LIGHTWHITE_EX + BOLD_INIT if item[2] == 'd' else Fore.WHITE
    fore_shift = Fore.WHITE
    print(Back.RESET + BOLD_RESET + f"{fore_shift + shift_build(item[0], item[2])}{fore_folders_files + item[1]}")
