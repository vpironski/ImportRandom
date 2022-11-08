import datetime
import random
import os
from database_core import Database
import database_utils


def random_date():
    start_date = datetime.date(1880, 1, 1)
    end_date = datetime.date(1890, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)


name_list = [
    'Atif',
    'Ian',
    'Danny',
    'Malcolm',
    'Matthew',
    'Ian',
    'Sarah',
    'Stuart',
    'Kim',
    'Paul',
    'David',
    'Mary',
    'Patricia',
    'Graham',
    'John',
    'Steven',
    'Stuart',
    'Derek',
    'Helen',
    'Robert',
    'Andrea',
    'Peter',
    'Kim',
    'Tomas',
    'Sean',
    'Robert',
    'John',
    'Stephen',
    'Freda',
    'Bernhard',
    'Rebecca',
    'Geoffrey',
    'Dylan',
    'Ap',
    'Daniel',
    'Gayatri',
    'Jonathan',
    'Rita',
    'Ann',
    'Neil',
    'David',
    'Christopher',
    'Thomas',
    'Sean',
    'Deborah',
    'Richard',
    'David',
    'Kristofer',
    'Anne',
    'Melanie',
    'Geralt',
    'Adolf'
]
surname_list = [
    'Anderson',
    'Astbury',
    'Bagshaw',
    'Bashir',
    'Bayne',
    'Bowring',
    'Cardwell',
    'Clark',
    'Coady',
    'Dalton',
    'Davies',
    'Dennison',
    'Donkor',
    'Doyle',
    'Feeley',
    'Gizzi',
    'Gowers',
    'Griffiths',
    'Grosvenor',
    'Hall',
    'Halliday',
    'Hamilton',
    'Harper',
    'Houston',
    'Huston',
    'Johal',
    'Johnson',
    'Kendrew',
    'Lambert',
    'Lee',
    'Marino',
    'Moore',
    'Norton',
    'Pye',
    'Riley',
    'Robertson',
    'Sadler',
    'Shine',
    'Smith',
    'Stagg',
    'Steward',
    'Taylor',
    'Tierney',
    'Tomkins',
    'Wainwright',
    'Waite',
    'Webb',
    'Whittle',
    'Wilcock',
    'Wishart',
    'Hitler',
]

os.chdir('..')
database = Database(f'{os.getcwd()}/Databases/generated.datab')

for i in range(10):
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    gender = random.choice(['m', 'f', 'n'])
    birth_date = random_date()
    course_number = str(random.randint(19000, 20000))
    database_utils.insert(database, [name, surname, course_number, gender, str(birth_date)])
database.close()
