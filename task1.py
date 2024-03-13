def total_salary(path):
    """
    :param path:
    :return:
    """
    global sum
    try:
        with open(path, encoding='utf-8') as fh:
            lines = [float(el.strip().split(',')[1]) for el in fh.readlines()]

        if not lines:
            print('not found data')
            exit()

        sum = sum(lines)
        return sum, sum / len(lines)

    except FileNotFoundError as error:
        print(error)
        exit()


total, average = total_salary('storage/salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
