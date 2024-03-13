import re
from pathlib import Path
from typing import Any

path = Path('storage/phonebook.txt')


def add_contact(args: list) -> str:
    """
    :param args:
    :return:
    """
    if len(args) != 2:
        return 'Input error'

    username, phone = args

    if len(phone) != 10:
        return 'Input phone error'

    with open(path, encoding='utf-8') as fh:
        if username in fh.read():
            return 'Contact is exists'

    with open(path, 'a', encoding='utf-8') as fh:
        fh.write(f'{username},{phone}\n')
        return 'Contact added.'


def change_contact(args: list) -> str:
    """
    :param args:
    :return:
    """
    if len(args) != 2:
        return 'Input error'

    username, phone = args

    if len(phone) != 10:
        return 'Input phone error'

    with open(path, encoding='utf-8') as fh:
        if username not in fh.read():
            return 'Contact not found'

        fh.seek(0)
        lines = [line.strip() for line in fh.readlines()]
        for k, line in enumerate(lines):
            lines[k] = f'{line}\n'
            if username in line:
                lines[k] = f'{username},{phone}\n'

    with open(path, '+w', encoding='utf-8') as fh:
        fh.writelines(lines)

    return 'Contact changed.'


def show_phone(args: list) -> str:
    """
    :param args:
    :return:
    """
    if len(args) != 1:
        return 'Input error'

    username = args[0]

    with open(path, encoding='utf-8') as fh:
        if username not in fh.read():
            return 'Contact not found'

        fh.seek(0)
        lines = [line.strip() for line in fh.readlines()]
        for line in lines:
            if username in line:
                return dict_to_text([line_to_dict(line)])


def show_all() -> str:
    """
    :return:
    """
    try:
        with open(path, encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
    except FileNotFoundError as err:
        return f'{err.strerror}: {path.name}'

    return dict_to_text([line_to_dict(line) for line in lines])


def parse_input(command: str) -> tuple[Any, Any]:
    """
    :param command:
    :return:
    """
    cmd, *args = re.split(r"\s+", command)
    cmd = cmd.lower()

    return cmd, args


def line_to_dict(line: str) -> dict:
    """
    :param line:
    :return:
    """
    return dict(zip(['name', 'phone'], line.split(',')))


def dict_to_text(function) -> str:
    """
    :param function:
    :return:
    """
    return '\n'.join([pattern(item) for item in function])


def pattern(item: dict) -> str:
    """
    :param item:
    :return:
    """
    return f"{item['name']}: {phone_format(item['phone'])}"


def phone_format(phone_number: str) -> str:
    """
    :param phone_number:
    :return:
    """
    return re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'(\1) \2-\3-\4', phone_number)


def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip()

        command, args = parse_input(command)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "add":
            result = add_contact(args)

        elif command == "change":
            result = change_contact(args)

        elif command == "phone":
            result = show_phone(args)

        elif command == "all":
            result = show_all()

        elif command == "hello":
            result = "How can I help you?"

        else:
            result = "Invalid command."

        print(result)


if __name__ == "__main__":
    main()
