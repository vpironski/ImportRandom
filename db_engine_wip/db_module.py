import re
from datetime import date


class Init_db:  # обект(клас) който ще съдържа конфигурацията на базата данни
    colons = dict
    path = ''

    def __init__(self, path_to_db):
        self.path = path_to_db
        name = str
        size_or_type = str

        # Ч ете първия ред(конфигурация) и го запазва в config
        with open(path_to_db, encoding="utf-8") as f:
            config = f.readline()

        # Разделя config  на отделни елементи (разделени със ,)
        for colon in config.lower().split(','):
            # името на колоната се разделя от останалата конфигурация и се запазва
            name = re.sub(r"\|.*?\||[0-9]+", "", colon)
            # размера (или типа) на колоната се отделя от името и се запазва
            size_or_type = re.findall(r"\|.*?\||[0-9]+", colon)[0]
            # може да стане и със: size_or_type = colon.replace(name, "") *може да е по-бързо

            # проверява дали в променливата size_or_type се съдържа размера(int) или типа(str) и променя вида на променливата
            if size_or_type.isnumeric():
                size_or_type = int(size_or_type)

            # print for testing
            print(f"Colon: {name}, size/type: {size_or_type}")
