import os

ROOT_PATH = '..\\pibulk\\book\\'
DEST_PATH = '..\\pibulk\\asks\\'

def read_source(file_name):
    print('Lendo fonte: ' + file_name)
    with open(ROOT_PATH + file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

if __name__ == '__main__':
    for origin in os.listdir(ROOT_PATH):
        source = read_source(origin)
        file_index = 1
        name, ext = os.path.splitext(origin)
        while len(source) > 0:
            with open(DEST_PATH + name + ' - ' + str(file_index).rjust(3, '0') + ext, 'w', encoding='utf-8') as file:
                file.write('Me explique com perguntas e respostas o seguinte texto:\n\n\n')
                line_index = 0
                while len(source) > 0:
                    line = source.pop(0)
                    file.write(line)
                    line_index += 1
                    if line_index == 100:
                        file_index += 1
                        break

