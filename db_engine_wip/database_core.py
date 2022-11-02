import re
import os
import shutil

# add different data types here with their corresponding length (example 'date': 10)
types_length = {'date': 10, 'gender': 1}
file_extension = '.datab'


class Database:  # обект(клас) който ще съдържа конфигурацията на базата данни
    colons = dict()
    path = ''
    name = ''
    entry_length = 0

    def __init__(self, path_to_db):
        self.path = path_to_db
        self.colons = dict()
        with open(path_to_db, 'r', encoding='utf-8') as database_file:
            config = database_file.read(1)
            while config[-1] != '!':
                config += database_file.read(1)
            database_file.close()

        # print(config)

            for colon in config.lower().strip(',!').split(','):
                name = re.sub(r'\|.*?\||[0-9]+', '', colon)
                size_or_type = re.search(r'\|.*?\||[0-9]+', colon)[0].strip('|')
                if size_or_type.isnumeric():
                    size_or_type = int(size_or_type)
                self.colons.update({name: size_or_type})

        self.entry_length = self.get_entry_length()
        self.name = re.sub(file_extension, '', os.path.basename(self.path))

    @staticmethod
    def validate_name(name):
        regex = re.compile(r'[a-z]+(_[a-z]+)*')
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
        os.chdir(os.getcwd()+"/db_engine_wip")
        file =  f"Databases/{name}{file_extension}"
        path = str(f"{os.getcwd()}/Databases/{file}")

        if not os.path.exists(f"Databases/{file}"):
            list_columns = []
            for i in config_dictionary:
                # if config_dictionary[i] in types_length:
                #     config_dictionary[i] = f"|{config_dictionary[i]}|"
                list_columns.append(i + str(config_dictionary[i]))

            with open(file, 'w', encoding='utf-8') as f:
                for i in list_columns:
                    f.write(i + ',')
                f.write('!')
            
            # src = os.getcwd() + "/db_engine_wip"
            # dst = os.getcwd() + "/db_engine_wip/Databases"

            
            # os.popen(f'cp db_engine_wip/{file} db_engine_wip/Databases/{file}')
        else:
            return ['File already exists!']

        # print(list_columns)

    def drop(self):
        if os.path.exists(self.path):
            os.remove(self.path)
    # must always delete the object of this instance after calling this method