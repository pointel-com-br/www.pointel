# aartc.py - Automatic Article Compile
import os
import re


def adjust_marked_empty_lines(text):
    print('Ajustando marcado - linhas vazias...')
    result = []
    empty = 0
    inside_code_block = False
    for line in text:
        test = line.strip()
        if inside_code_block:
            result.append(line)
            if test.startswith("```"):  
                inside_code_block = False
        elif test.startswith("```"):
            result.append(line)
            inside_code_block = True
            empty = 0
        else:
            test = re.sub(r'\s+', ' ', test)
            if not test:
                empty += 1
            else:
                empty = 0
            if empty <= 1:
                result.append(test + '\n')
    return result


def adjust_marked_main_chapter(text, path):
    print('Ajustando marcado - capítulo principal...')
    text[0] = text[0].strip()
    main_title = '# ' + os.path.splitext(os.path.basename(path))[0] + '\n'
    if not text[0] == main_title:
        text[0] = main_title
    return text


def adjust_marked_chars(text):
    print('Ajustando marcado - caracteres...')
    result = []
    for line in text:
        line = line.replace('■', '')
        line = line.replace('“', '"')
        line = line.replace('”', '"')
        line = line.replace('’', "'")
        line = line.replace('‘', "'")
        line = line.replace('–', '-')
        line = line.replace('□', '-')
        line = line.replace('•', '*')
        line = line.replace('♦', '*')
        line = line.replace('…', '...')
        result.append(line)
    return result


def adjust_marked_page_numbers(text):

    def is_only_three_numbers(line):
        line = line.strip()
        result = False
        if len(line) > 0 and len(line) < 4:
            result = True
            for c in line:
                if not c.isdigit():
                    result = False
                    break
        return result

    print('Ajustando marcado - números de página...')
    result = []
    for line in text:
        if not is_only_three_numbers(line):
            result.append(line)
    return result


def adjust_marked_only_dots(text):

    def is_only_dots(line):
        line = line.strip()
        for c in line:
            if not (c == " " or c == "."):
                return False
        return True

    print('Ajustando marcado - somente pontos...')
    result = []
    for line in text:
        if not is_only_dots(line):
            result.append(line)
    return result


def adjust_marked_broken_lines(text):

    def is_the_case(char):
        return char.isalpha() and char.islower() and not char.isdigit()

    print('Ajustando marcado - linhas quebradas...')
    i = 0
    result = []
    last_line = ""
    inside_block = False
    while i < len(text):
        line = text[i]
        test = line.strip()
        if inside_block:
            result.append(line)
            last_line = ""
            if test.startswith("```"):
                inside_block = False
        elif test.startswith("```"):
            result.append(line)
            last_line = ""
            inside_block = True
        else:
            if test != "":
                if is_the_case(test[-1]):
                    j = i + 1
                    while j < len(text):
                        test_next = text[j].strip()
                        if test_next != "":
                            if is_the_case(test_next[0]):
                                diff = (j - 1) - i
                                i += diff
                            break
                        j += 1
            append = True
            if last_line and test:
                if is_the_case(last_line[-1]) and is_the_case(test[0]):
                    append = False
            if append:
                result.append(test + "\n")
            else:
                result[-1] = result[-1].strip() + " " + test
            last_line = test
        i += 1
    return result


def adjust_marked_temp(text):
    print('Ajustando marcado - processos temporários...')
    return text


def adjust_text_hierarchy(text):
    print('Ajustando texto - hierarquia...')
    result = []
    inside_code_block = False
    for line in text:
        test = line.strip()
        if test.startswith("```"):
            inside_code_block = not inside_code_block
        if inside_code_block:
            result.append(line)
        else:
            if test.startswith("###### "):
                test = "Sub Sub Sub Tópico. " + test[len("###### "):]
                if not test.endswith("."):
                    test += "."
            elif test.startswith("##### "):
                test = "Sub Sub Tópico. " + test[len("##### "):]
                if not test.endswith("."):
                    test += "."
            elif test.startswith("#### "):
                test = "Sub Tópico. " + test[len("#### "):]
                if not test.endswith("."):
                    test += "."
            elif test.startswith("### "):
                test = "Tópico. " + test[len("### "):]
                if not test.endswith("."):
                    test += "."
            elif test.startswith("## "):
                test = "Sub Capítulo. " + test[len("## "):]
                if not test.endswith("."):
                    test += "."
            elif test.startswith("# "):
                test = "Capítulo. " + test[len("# "):]
                if not test.endswith("."):
                    test += "."
            result.append(test + '\n')
    return result


def adjust_text_items(text):
    print('Ajustando texto - itens...')
    for i in range(len(text)):
        line = text[i]
        initial_space = line.find(' ')
        if initial_space > 0:
            initial_part = line[:initial_space]
            only_numbers_or_dots = True
            there_is_a_dot = False
            there_is_a_number = False
            for c in initial_part:
                if not c.isdigit() and c != '.':
                    only_numbers_or_dots = False
                elif c.isdigit():
                    there_is_a_number = True
                elif c == '.':
                    there_is_a_dot = True
            if only_numbers_or_dots and there_is_a_number and there_is_a_dot:
                text[i] = "Item. " + text[i]
    return text


def adjust_text_code_blocks(text):
    print('Ajustando texto - blocos de código...')
    result = []
    inside_code_block = False
    for line in text:
        test = line.strip()
        if test.startswith("```"):
            suffix = test[3:] if len(test) > 3 else ""
            if not inside_code_block:
                test = "Iniciando bloco de código."
            else:
                test = "Fechando bloco de código."
            if suffix:
                test += " " + suffix
            if not test.endswith("."):
                test += "." 
            result.append(test + "\n\n")
            inside_code_block = not inside_code_block
        else: 
            if inside_code_block and line.strip():
                test = line.rstrip()
                test = test.replace('.', ' . ')
                test = test.replace(',', ' , ')
                test = test.replace(';', ' ; ')
                test = test.replace('-', ' - ')
                test = test.replace('+', ' + ')
                test = test.replace('*', ' * ')
                test = test.replace('/', ' / ')
                test = test.replace('\\', ' \\ ')
                test = test.replace('=', ' = ')
                test = test.replace('(', ' ( ')
                test = test.replace(')', ' ) ')
                test = test.replace('[', ' [ ')
                test = test.replace(']', ' ] ')
                test = test.replace('{', ' { ')
                test = test.replace('}', ' } ')
                result.append(test + "\n\n")
            else:
                result.append(line)
    return result


def adjust_text_temp(text):
    print('Ajustando texto - processos temporários...')
    return text


def adjust_marked(text, path):
    print('Ajustando marcado: ' + path)
    text = adjust_marked_empty_lines(text)
    text = adjust_marked_main_chapter(text, path)
    text = adjust_marked_chars(text)
    text = adjust_marked_page_numbers(text)
    text = adjust_marked_broken_lines(text)
    text = adjust_marked_temp(text)
    return text


def adjust_text(text, path):
    print('Ajustando texto: ' + path)
    text = adjust_text_hierarchy(text)
    text = adjust_text_items(text)
    text = adjust_text_code_blocks(text)
    text = adjust_text_temp(text)
    return text


def save_text(text, path):
    text = adjust_text(text, path)
    destiny = os.path.splitext(path)[0] + ".txt"
    print('Salvando texto: ' + destiny)
    with open(destiny, 'w', encoding="utf-8") as file:
        file.writelines(text)
    return text


def save_marked(text, path):
    text = adjust_marked(text, path)
    print('Salvando marcado: ' + path)
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(text)
    return text


def read_marked(path):
    print('Lendo marcado: ' + path)
    with open(path, 'r', encoding="utf-8") as file:
        return file.readlines()


def list_paths():
    return [p for p in os.listdir('.') if p[-3:] == '.md']


if __name__ == '__main__':
    for path in list_paths():
        save_text(save_marked(read_marked(path), path), path)
