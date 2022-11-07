import os
import re

# add different data types here with their corresponding length (example 'date': 10)
types_length = {'date': 10, 'gender': 1, 'course_number': 5}
database_extension = '.datab'
meta_extension = '.meta'


class Database:
    colons = dict()
    path = ''
    name = ''
    entry_length = 0
    config_line_length = 1
    entry_count = 0
    db_file = None

    def __init__(self, path_to_db):
        self.path = path_to_db
        self.colons = dict()
        self.db_file = open(path_to_db, 'a+', encoding='utf-8')
        self.entry_length = self.get_entry_length()
        self.name = re.sub(database_extension, '', os.path.basename(self.path))

        with open(f'{os.getcwd()}/Databases/{self.name}{meta_extension}', 'r', encoding='utf-8') as meta_file:
            config = meta_file.read(1)
            while config[-1] != '!':
                config += meta_file.read(1)
                self.config_line_length += 1
            self.entry_count = int(meta_file.read(1))

        for colon in config.lower().strip(',!').split(','):
            name = re.sub(r'\|.*?\||[0-9]+', '', colon)
            size_or_type = re.search(r'\|.*?\||[0-9]+', colon)[0].strip('|')
            if size_or_type.isnumeric():
                size_or_type = int(size_or_type)
            self.colons.update({name: size_or_type})

    @staticmethod
    def validate_name(name):
        regex = re.compile(r'[a-zA-Z]+(_[a-zA-Z]+)*')
        return re.fullmatch(regex, name)

    def get_entry_length(self):
        length = 0
        for value in list(self.colons.values()):
            if str(value).isnumeric():
                length += value
            else:
                length += types_length.get(value)
        return length

    @staticmethod
    def create(config_dictionary, name):

        database_file = f"{name}{database_extension}"
        meta_file = f'{name}{meta_extension}'
        db_path = f"{os.getcwd()}/Databases/{database_file}"
        meta_path = f'{os.getcwd()}/Databases/{meta_file}'

        if not os.path.exists(db_path):
            list_columns = ['id5', 'is_active1']
            for i in config_dictionary:
                list_columns.append(i + str(config_dictionary[i]))

            with open(meta_path, 'w', encoding='utf-8') as f:
                for i in list_columns:
                    f.write(i + ',')
                f.write('!0')
            open(db_path, 'w').close()
        else:
            return ['File already exists!']

    def close(self):
        with open(f'{os.getcwd()}/Databases/{self.name}{meta_extension}', 'r+', encoding='utf-8') as meta_file:
            meta_file.seek(self.config_line_length)
            meta_file.write(str(self.entry_count))
        self.db_file.close()

    def drop(self):
        # self.close()
        if os.path.exists(self.path):
            os.remove(self.path)
