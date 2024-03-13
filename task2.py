def get_cats_info(path):
    """
    :param path:
    :return:
    """
    try:
        with open(path, encoding='utf-8') as fh:
            lines = [el.strip().split(',') for el in fh.readlines()]

        if not lines:
            print('not found data')
            exit()

        items = []
        for k, line in enumerate(lines):
            items.append(dict(zip(['id', 'name', 'age'], line)))

        return items

    except FileNotFoundError as error:
        print(error)
        exit()


cats_info = get_cats_info('storage/cats.txt')
print(cats_info)