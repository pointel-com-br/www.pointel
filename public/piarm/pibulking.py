import os
import time

import pilibs
import pyperclip

ROOT_PATH = '..\\pibulk\\pool\\'
LAST_ONE = pyperclip.paste()


def get_next():
    global LAST_ONE
    while True:
        this_one = pyperclip.paste()
        if this_one == LAST_ONE:
            time.sleep(1)
        else:
            LAST_ONE = this_one
            return this_one
        

def clean_title(title):
    while (title.endswith('.')):
        title = title[0:-1]
    return title


if __name__ == '__main__':
    while True:
        print("Getting title...")
        title = clean_title(get_next().strip())
        print("Got", title)
        print("Getting article...")
        article = get_next().strip()
        print("Got", article)
        if title and article:
            file_path = ROOT_PATH + pilibs.clean_file_name(title) + '.md'
            index = 2
            while os.path.isfile(file_path):
                file_path = ROOT_PATH + pilibs.clean_file_name(title) + '(' + str(index) + ').md'
                index += 1
            print("Saving", file_path)
            with open(file_path, mode='w', encoding='UTF-8') as file:
                file.write("# ")
                file.write(title)
                file.write("\n\n")
                file.write(article)
                file.write("\n")
            print("Saved", file_path)
            


