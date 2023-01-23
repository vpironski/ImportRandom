import os

import db_engine_new.Engine.Main.db_engine_main as eng
import tabulate


def input_choice(options: tuple):
    for i, item in enumerate(options):
        print("{}. {}".format(i + 1, item))
    print("Please choose one of the above options:")
    while True:
        choice = input()
        if choice.isnumeric() and 1 <= int(choice) <= len(options):
            break
        else:
            print("Invalid choice. Please try again.")
    return int(choice)


# first_action = input_choice(('USE', 'CREATE', 'DROP', 'QUIT'))
# if first_action == 1:
#     databases = os.listdir('Databases/')
#
data = [['apple', 20, '400'],
        ['banana', 15, '120'],
        ['potato', 30, '60'],
        ]
print(tabulate.tabulate(data, tablefmt=tabulate.tabulate_formats[1], headers=['name', 'weight', 'price']))
