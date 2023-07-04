def adjust_text_code_blocks(text):
    print('Ajustando texto - blocos de código...')
    result = []
    inside_code_block = False
    for line in text:
        test = line.strip()
        if test.startswith('```'):
            suffix = test[3:] if len(test) > 3 else ''
            if not inside_code_block:
                test = 'Iniciando bloco de código.'
            else:
                test = 'Fechando bloco de código.'
            if suffix:
                test += ' ' + suffix
            if not test.endswith('.'):
                test += '.' 
            result.append(test + '\n\n')
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
                test = test.replace('%', ' % ')
                test = test.replace('<', ' < ')
                test = test.replace('>', ' > ')
                test = test.replace('=', ' = ')
                test = test.replace('(', ' ( ')
                test = test.replace(')', ' ) ')
                test = test.replace('[', ' [ ')
                test = test.replace(']', ' ] ')
                test = test.replace('{', ' { ')
                test = test.replace('}', ' } ')
                result.append(test + '\n\n')
            else:
                result.append(line)
    return result