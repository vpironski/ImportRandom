import re


class OpenDatabase:  # обект(клас) който ще съдържа конфигурацията на базата данни
    colons = dict()
    path = ''
    entry_length = 0

    def __init__(self, path_to_db):
        self.path = path_to_db

        with open(path_to_db, encoding='utf-8') as database_file:
            config = database_file.read(1)
            while config[-1] != '!':
                config += database_file.read(1)

        # print(config)
        
        if bool(self.validate_config(config)):
            for colon in config.lower().strip(',!').split(','):
                name = re.sub(r'\|.*?\||[0-9]+', '', colon)
                size_or_type = colon.replace(name, '').strip('|')
                if size_or_type.isnumeric():
                    size_or_type = int(size_or_type)
                self.colons.update({name: size_or_type})
        else:
            print("Invalid config!")

        self.entry_length = self.get_entry_length()

    @staticmethod
    def validate_config(config):
        regex = re.compile(r'(([a-z]+(_[a-z]+)*[0-9]+,)|([a-z]+(_[a-z]+)*\|[^|]+\|,))+!$')
        return re.fullmatch(regex, config)

    def get_entry_length(self):
        length = 0
        for value in list(self.colons.values()):
            if str(value).isnumeric():
                length += value
            else:
                # add different data types here with their corresponding length (example 'date': 10)
                types_length = {'date': 10}
                length += types_length.get(value)
        return length
