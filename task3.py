import sys
from pathlib import Path
from colorama import Fore, Back

try:
    path = Path(sys.argv[1])
except IndexError as err:
    print('you have to provide a path')
    exit()


items = [(0, path.name, 'd')]


def read_path(path, shuffle=0):
    shuffle += 1
    for item in path.iterdir():
        if item.is_dir():
            items.append((shuffle, item.name, 'd'))
            read_path(item, shuffle)
        else:
            items.append((shuffle, item.name, 'f'))


def shuffle_build(k, type):
    return ' ' * k + ('-' if type == 'f' else '')


try:
    read_path(path)
except FileNotFoundError as err:
    print(err)
    exit()


for item in items:
    fore_folders_files = Back.GREEN + Fore.BLACK if item[2] == 'd' else Fore.WHITE
    fore_shuffles = Fore.WHITE
    print(Back.RESET + f"{fore_shuffles + shuffle_build(item[0], item[2])}{fore_folders_files + item[1]}")
