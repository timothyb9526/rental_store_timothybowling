from datetime import datetime
from core import *


def load_inventory(contents, string):

    name, stock, rent, replacement = string.split(',')
    return Property(name, int(stock), int(rent), int(replacement))


def get_inventory():
    count = 0
    with open('inventory.txt') as file:
        contents = file.readline().split(',')
        lines = file.readlines()
    properties = []
    for l in lines:
        count += 1
        p = load_inventory(contents, l)

        properties.append(p)

    return Inventory(properties)


def print_inventory():
    with open('inventory.txt') as file:
        contents = file.read()

        return contents


def give_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        files = file.write(inventory)


def write_to_log(rent):
    time = str(datetime.now())
    text = time + ', ' + rent.log_string()
    with open('history.txt', 'a') as file:
        file.write(text)


def write_to_log_return(return_list):
    time = str(datetime.now())
    text = time + ', ' + return_list.return_log()

    with open('history.txt', 'a') as file:
        file.write(text)


def employee():
    with open('history.txt') as file:
        files = file.read()
    return files


def is_number(s):
    return s.count('.') < 2 and s.replace('.', '').isnumeric()


def revenue():
    sales = []
    with open('history.txt') as file:
        lines = file.readlines()

    for line in lines:
        pieces = line.strip().split(',')
        number = pieces[-1].strip()
        if is_number(number):
            sales.append(float(number))
    return sum(sales)
