import os
import shutil


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
    if len(line) < 1:
        return False
    return line[0].isdigit() or line[0] == '-'


def has_items(source):
    for line in source:
        if is_item(line):
            return True
    return False


def prepare_question(question, title):
    result = 'Em, ' + title.strip() + ', como se define o item, ' + question.strip() + '.'
    return result


def prepare_answer(answer):
    result = answer.strip()
    if len(result) > 1:
        result = result[0].upper() + result[1:]
    return result


def split_item_colon(item):
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

def find_verb(item):
    verbs = ['é', 'são']
    for verb in verbs:
        if item.find(verb):
            return verb
    return ''

def split_item_verb(item):
    verb = find_verb(item)
    parts = item.split(verb)
    question = None
    answer = None
    for part in parts:
        if not question:
            question = part
        elif not answer:
            answer = part.lstrip()
        else:
            answer += verb
            answer += part
    return question, answer

def split_item(item):
    if item.find(':') > -1:
        return split_item_colon(item)
    else:
        return split_item_verb(item)    


def get_items(source, title):
    result = []
    item = ""
    for line in source:
        if is_item(line):
            if item:
                question, answer = split_item(item)
                if question and answer:
                    question = prepare_question(question, title)
                    answer = prepare_answer(answer)
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
    else:
        return (title, "\n".join(source))


def read_source(file_name):
    print('Lendo fonte: ' + file_name)
    with open(ROOT_PATH + file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

ROOT_PATH = '..\\pibulk\\pool\\'
PROC_PATH = '..\\pibulk\\proc\\'
DEST_PATH = '..\\picard\\append.txt'

if __name__ == '__main__':
    for file_name in os.listdir(ROOT_PATH):
        cards = get_cards(read_source(file_name))
        if cards:
            for card in cards:
                question, answer = card
                with open(DEST_PATH, mode='a', encoding='UTF-8') as file:
                    file.write('\n\n')
                    file.write('--------- Pergunta ---------')
                    file.write('\n\n')
                    file.write(question)
                    file.write('\n\n')
                    file.write('----- Resposta -----')
                    file.write('\n\n')
                    file.write(answer)
                    file.write('\n\n')
            shutil.move(ROOT_PATH + file_name, PROC_PATH + file_name)
