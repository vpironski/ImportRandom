import re


class Init_Db:  # обект(клас) който ще съдържа конфигурацията на базата данни
    colons = dict()
    path = ''

    def __init__(self, path_to_db):
        self.path = path_to_db
        name = ''
        size_or_type = ''
        with open(path_to_db, encoding="utf-8") as f:
            config = f.readline()
        for colon in config.lower().split(','):
            name = re.sub(r"\|.*?\||[0-9]+", "", colon)
            size_or_type = colon.replace(name, "").strip('|')
            if size_or_type.isnumeric():
                size_or_type = int(size_or_type)
            self.colons.update({name: size_or_type})
