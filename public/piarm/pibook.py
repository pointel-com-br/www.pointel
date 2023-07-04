import os
import re

import piarm

ROOT_PATH = '..\\pibook\\'


def save_text(text, name):
    text = piarm.adjust_text(text, name)
    destiny = os.path.splitext(name)[0] + '.txt'
    print('Salvando texto: ' + destiny)
    with open(ROOT_PATH + destiny, 'w', encoding='utf-8') as file:
        file.writelines(text)
    return text


def save_marked(text, name):
    text = piarm.adjust_marked(text, name)
    print('Salvando marcado: ' + name)
    with open(ROOT_PATH + name, 'w', encoding='utf-8') as file:
        file.writelines(text)
    return text


def read_marked(name):
    print('Lendo marcado: ' + name)
    with open(ROOT_PATH + name, 'r', encoding='utf-8') as file:
        return file.readlines()


def is_marked(name):
    return name[-3:] == '.md'


def has_changes(marked):
    text = os.path.splitext(marked)[0] + ".txt"
    if os.path.isfile(ROOT_PATH + text):
        if os.path.getmtime(ROOT_PATH + text) > os.path.getmtime(ROOT_PATH + marked):
            return False
    return True


def list_marked_with_changes():
    return [path for path in os.listdir(ROOT_PATH) if is_marked(path) and has_changes(path)]


if __name__ == '__main__':
    for marked in list_marked_with_changes():
        save_text(save_marked(read_marked(marked), marked), marked)
