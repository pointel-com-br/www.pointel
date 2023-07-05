import os


def pop_title(source):
    for i, line in enumerate(source):
        line = line.strip()
        if line.startswith("# "):
            line = line[2:]
            line = line[0].lower() + line[1:]
            if line.endswith('?'):
                line = line[0:-1]
            source.pop(i)
            return line
    return ''

def del_empty_lines(source):
    result = []
    for line in source:
        if len(line.strip()) > 0:
            result.append(line.rstrip())
    return result


def del_first_last_lines(source):
    source.pop(0)
    source.pop(-1)
    return source


def is_item(line):
    test = line.strip()
    if len(test) < 1:
        return False
    return test[0].isdigit() or test[0] == '-'


def has_items(source):
    for line in source:
        if is_item(line):
            return True
    return False


def prepare_question(question, title):
    result = 'Em, ' + title + ', como se define o item, ' + question + '.'
    return result


def split_item(item):
    parts = item.split(":")
    question = None
    answer = None
    for part in parts:
        if not question:
            question = part
        elif not answer:
            answer = part.lstrip()
        else:
            answer += ":"
            answer += part
    return question, answer


def get_items(source, title):
    result = []
    item = ""
    for line in source:
        if is_item(line):
            if item:
                question, answer = split_item(item)
                if not question or not answer:
                    return None
                question = prepare_question(question, title)
                result.append((question, answer))
            item = line
        else:
            if item:
                item += '\n'
            item += line
    return result
    

def get_cards(source):
    title = pop_title(source)
    source = del_empty_lines(source)
    source = del_first_last_lines(source)
    if has_items(source):
        return get_items(source, title)
    return None


def read_source(file_name):
    print('Lendo fonte: ' + file_name)
    with open(ROOT_PATH + file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

ROOT_PATH = '..\\pibulk\\pool\\'
if __name__ == '__main__':
    for file_name in os.listdir(ROOT_PATH):
        cards = get_cards(read_source(file_name))
        if cards:
            for line in cards:
                print(line)
                print()
