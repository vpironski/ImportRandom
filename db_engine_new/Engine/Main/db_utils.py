import re


class InvalidIDError(Exception):
    pass


class InvalidSyntaxError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidTableError(Exception):
    def __init__(self, message: str):
        self.message = message


class CreationError(Exception):
    def __init__(self, message: str):
        self.message = message


def validate_name(name: str):
    reg = re.compile(r'[a-zA-Z][a-zA-Z0-9]*(_[a-zA-Z][a-zA-Z0-9]*)*')
    return True if reg.fullmatch(name) else False
    pass


def cut_entry_to(labeled_entry: dict, columns: list):
    cut_entry = []
    for column in labeled_entry.keys():
        if column in columns:
            cut_entry.append(labeled_entry[column])
    return cut_entry


def like(column_value, pattern: str):
    if type(column_value) is not str:
        raise InvalidSyntaxError('The like operator only works with strings.')
    try:
        pattern = re.compile(pattern)
    except re.error:
        raise InvalidSyntaxError(f'`{pattern}` is not a valid regular expression.')

    return True if pattern.fullmatch(column_value) else False
