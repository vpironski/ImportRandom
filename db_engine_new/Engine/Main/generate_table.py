import random
import string
import Engine.Main.db_engine_main as eng

first_names = [
    'Emma',
    'Ethan',
    'Olivia',
    'Noah',
    'Ava',
    'Liam',
    'Sophia',
    'William',
    'Isabella',
    'James'
]

last_names = [
    'Smith',
    'Johnson',
    'Williams',
    'Jones',
    'Brown',
    'Garcia',
    'Miller',
    'Davis',
    'Rodriguez',
    'Martinez'
]

jobs = [
    'Teacher',
    'Nurse',
    'Engineer',
    'Programmer',
    'Construction worker',
    'Electrician',
    'Salesperson',
    'Chef',
    'Accountant',
    'Lawyer'
]


def generate(row_count: int):
    symbols = list(string.ascii_letters + string.digits + '!$#')

    try:
        eng.Database.create('generated')
    except eng.CreationError as err:
        print(err.message, 'Skipping...\n')
    db = eng.Database('generated')
    try:
        db.create_table('worker', [('first_name', 's', 20),
                                   ('last_name', 's', 20),
                                   ('position', 's', 20),
                                   ('salary', 'd', 1),
                                   ('identification', 's', 5)])
    except eng.CreationError as err:
        print(err.message, 'Skipping...\n')

    for i in range(row_count):
        entry = [
            random.choice(first_names),
            random.choice(last_names),
            random.choice(jobs),
            random.uniform(1000, 100000),
            ''.join(random.choices(symbols, k=5))
        ]
        db.insert('worker', entry)
