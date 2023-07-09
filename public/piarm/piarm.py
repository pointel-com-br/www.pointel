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
            if test.startswith('```'):  
                inside_code_block = False
        elif test.startswith('```'):
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
    while len(result) >= 1:
        if result[-1].strip() == "":
            result.pop()
        else:
            break
    return result


def adjust_marked_main_chapter(text, name):
    print('Ajustando marcado - capítulo principal...')
    text[0] = text[0].strip()
    main_title = '# ' + os.path.splitext(os.path.basename(name))[0] + '\n'
    if not text[0] == main_title:
        text[0] = main_title
    return text


def adjust_marked_chars(text):
    print('Ajustando marcado - caracteres...')
    result = []
    for line in text:
        line = line.replace('“', '"')
        line = line.replace('”', '"')
        line = line.replace('’', '\'')
        line = line.replace('‘', '\'')
        line = line.replace('–', '-')
        line = line.replace('■', '-')
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


def adjust_marked_weird_chars(text):

    def is_only_weird(test):
        if len(test) < 3:
            return False
        weird_count = False
        for c in test:
            if not (c == ' ' or c == '.' or c == ',' or c == ':' or c == ';' or c == '*' or c == '/' or c == '\\' or c == '|'):
                return False
            if c == '.' or c == ',' or c == ':' or c == ';' or c == '*' or c == '/' or c == '\\' or c == '|':
                weird_count += 1
        return weird_count >= 3

    print('Ajustando marcado - caracteres estranhos...')
    result = []
    inside_block = False
    for line in text:
        test = line.strip()
        if inside_block:
            result.append(line)
            if test.startswith('```'):
                inside_block = False
        elif test.startswith('```'):
            result.append(line)
            inside_block = True
        elif not is_only_weird(test):
            if test.startswith('#') and test[len(test) -1] == '.':
                line = test[0:len(test) -1] + '\n'
            result.append(line)
    return result


def adjust_marked_broken_lines(text):

    def is_the_case(char):
        return char.isalpha() and char.islower() and not char.isdigit()

    print('Ajustando marcado - linhas quebradas...')
    i = 0
    result = []
    last_line = ''
    inside_block = False
    while i < len(text):
        line = text[i]
        test = line.strip()
        if inside_block:
            result.append(line)
            last_line = ''
            if test.startswith('```'):
                inside_block = False
        elif test.startswith('```'):
            result.append(line)
            last_line = ''
            inside_block = True
        else:
            if test != '':
                if is_the_case(test[-1]):
                    j = i + 1
                    while j < len(text):
                        test_next = text[j].strip()
                        if test_next != '':
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
                result.append(test + '\n')
            else:
                result[-1] = result[-1].strip() + ' ' + test
            last_line = test
        i += 1
    return result


def adjust_marked_temp(text):
    print('Ajustando marcado - processos temporários...')
    return text

def adjust_text_initial(text):
    text.insert(0, "{{Voice=Acapela Marcia22 (Brazilian Portuguese)/}}<rate absspeed=\"-2\"/>\n")
    return text

def adjust_text_hierarchy(text):
    print('Ajustando texto - hierarquia...')
    result = []
    inside_code_block = False
    had_chapter = False
    for line in text:
        test = line.strip()
        if test.startswith('```'):
            inside_code_block = not inside_code_block
        if inside_code_block:
            result.append(line)
        else:
            if test.startswith('###### '):
                test = 'Sub Sub Sub Tópico. ' + test[len('###### '):]
                if not test.endswith('.'):
                    test += '.'
            elif test.startswith('##### '):
                test = 'Sub Sub Tópico. ' + test[len('##### '):]
                if not test.endswith('.'):
                    test += '.'
            elif test.startswith('#### '):
                test = 'Sub Tópico. ' + test[len('#### '):]
                if not test.endswith('.'):
                    test += '.'
            elif test.startswith('### '):
                test = 'Tópico. ' + test[len('### '):]
                if not test.endswith('.'):
                    test += '.'
            elif test.startswith('## '):
                test = '{{Pause=2}} Início de Sub Capítulo. ' + test[len('## '):]
                if not test.endswith('.'):
                    test += '.'
                test += ' {{Pause=1}}' 
            elif test.startswith('# '):
                test = '{{Pause=3}} Início de Capítulo. ' + test[len('# '):]
                if not test.endswith('.'):
                    test += '.'
                test += ' {{Pause=2}}'
                had_chapter = True
            result.append(test + '\n')
    if had_chapter:
        result.append('\n')
        result.append('{{Pause=1}} Fim de Capítulo. {{Pause=2}}\n')
        result.append('\n')
    return result


def replace_code_signals(text):
    text = text.replace('{', ' open braces ')
    text = text.replace('}', ' close braces ')
    text = text.replace('=', ' equals {{Pause=1}} ')
    text = text.replace(' open braces ', ' open braces {{Pause=1}} ')
    text = text.replace(' close braces ', ' close braces {{Pause=1}} ')
    text = text.replace('< equals {{Pause=1}} >', ' left right double arrow {{Pause=1}} ')
    text = text.replace(' equals {{Pause=1}} >', ' equals or bigger {{Pause=1}} ')
    text = text.replace(' equals {{Pause=1}} <', ' equals or less {{Pause=1}} ')
    text = text.replace('< equals {{Pause=1}}', ' less or equals {{Pause=1}} ')
    text = text.replace('> equals {{Pause=1}}', ' bigger or equals {{Pause=1}} ')
    text = text.replace('<->', ' left right arrow {{Pause=1}} ')
    text = text.replace('<-', ' left arrow {{Pause=1}} ')
    text = text.replace('->', ' right arrow {{Pause=1}} ')
    text = text.replace('-', ' hyphen {{Pause=1}} ')
    text = text.replace('\'', ' single quote {{Pause=1}} ')
    text = text.replace('"', ' double quotes {{Pause=1}} ')
    text = text.replace('...', ' three dots {{Pause=1}} ')
    text = text.replace('.', ' dot {{Pause=1}} ')
    text = text.replace(',', ' comma {{Pause=1}} ')
    text = text.replace(':', ' colon {{Pause=1}} ')
    text = text.replace(';', ' semicolon {{Pause=1}} ')
    text = text.replace('_', ' underscore {{Pause=1}} ')
    text = text.replace('+', ' plus {{Pause=1}} ')
    text = text.replace('*', ' asterisk {{Pause=1}} ')
    text = text.replace('`', ' backtick {{Pause=1}} ')
    text = text.replace('/', ' slash {{Pause=1}} ')
    text = text.replace('\\',  ' backslash {{Pause=1}} ')
    text = text.replace('%', ' percent {{Pause=1}} ')
    text = text.replace('$', ' dollar {{Pause=1}} ')
    text = text.replace('#', ' sharp {{Pause=1}} ')
    text = text.replace('&', ' ampersand {{Pause=1}} ')
    text = text.replace('|', ' vertical bar {{Pause=1}} ')
    text = text.replace('~', ' tilde {{Pause=1}} ')
    text = text.replace('^', ' caret {{Pause=1}} ')
    text = text.replace('@', ' at {{Pause=1}} ')
    text = text.replace('!', ' exclamation {{Pause=1}} ')
    text = text.replace('?', ' question {{Pause=1}} ')
    text = text.replace('<', ' less {{Pause=1}} ')
    text = text.replace('>', ' bigger {{Pause=1}} ')
    text = text.replace('(', ' open parenthesis {{Pause=1}} ')
    text = text.replace(')', ' close parenthesis {{Pause=1}} ')
    text = text.replace('[', ' open brackets {{Pause=1}} ')
    text = text.replace(']', ' close brackets {{Pause=1}} ')
    return text



def adjust_text_code_blocks(text):
    print('Ajustando texto - blocos de código...')
    result = []
    inside_code_block = False
    for line in text:
        test = line.strip()
        if test.startswith('```'):
            suffix = test[3:] if len(test) > 3 else ''
            if not inside_code_block:
                test = 'Iniciando bloco de código. {{Voice=Acapela Ryan22/}}<rate absspeed=\"-2\"/> '
            else:
                test = ' {{Voice=Acapela Marcia22 (Brazilian Portuguese)/}}<rate absspeed=\"-2\"/> Fechando bloco de código.'
            if suffix:
                test += ' ' + suffix
            if not test.endswith('.'):
                test += '.' 
            result.append(test + '\n\n')
            inside_code_block = not inside_code_block
        else: 
            if inside_code_block and line.strip():
                test = line.rstrip()
                test = replace_code_signals(test)
                result.append(test + '\n\n')
            else:
                last = line.find('`')
                if last == -1:
                    result.append(line)
                else:
                    make = ""
                    until = 0
                    while last > -1:
                        make += line[until:last]
                        until = last
                        next = line.find('`', last + 1)
                        if next > -1:
                            make += ' {{Voice=Acapela Ryan22/}}<rate absspeed=\"-2\"/> '
                            inside = line[last+1:next]
                            make += replace_code_signals(inside)
                            make += ' {{Voice=Acapela Marcia22 (Brazilian Portuguese)/}}<rate absspeed=\"-2\"/> '
                            until = next + 1
                            last = line.find('`', next + 1)
                        else:
                            raise Exception("Did not found the closings single line code block.")
                    make += line[until:]
                    result.append(make)
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
                text[i] = 'Item. ' + text[i]
    return text


def adjust_text_temp(text):
    print('Ajustando texto - processos temporários...')
    return text


def adjust_marked(text, name):
    print('Ajustando marcado: ' + name)
    text = adjust_marked_empty_lines(text)
    text = adjust_marked_main_chapter(text, name)
    text = adjust_marked_chars(text)
    text = adjust_marked_page_numbers(text)
    text = adjust_marked_broken_lines(text)
    text = adjust_marked_weird_chars(text)
    text = adjust_marked_temp(text)
    return text


def adjust_text(text, name):
    print('Ajustando texto: ' + name)
    text = adjust_text_hierarchy(text)
    text = adjust_text_items(text)
    text = adjust_text_code_blocks(text)
    text = adjust_text_initial(text)
    text = adjust_text_temp(text)
    return text
