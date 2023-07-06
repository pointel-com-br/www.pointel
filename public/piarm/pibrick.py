import os
import time

import pilibs
import pyperclip

ROOT_PATH = '..\\pibulk\\brick\\'
LAST_ONE = pyperclip.paste()


def get_next():
    global LAST_ONE
    while True:
        this_one = pyperclip.paste()
        if this_one == LAST_ONE:
            time.sleep(0.5)
        else:
            LAST_ONE = this_one
            return this_one


if __name__ == '__main__':
    print("PiBrick saves all that goes on the clipboard in brick files...")
    while True:
        print("Getting article...")
        article = get_next().strip()
        print("Got", article)
        if article:
            index = 1
            file_path = ROOT_PATH + 'brick (' + str(index).rjust(5, '0') + ').md'
            while os.path.isfile(file_path):
                file_path = ROOT_PATH + 'brick (' + str(index).rjust(5, '0') + ').md'
                index += 1
            print("Saving", file_path)
            with open(file_path, mode='w', encoding='UTF-8') as file:
                file.write(article)
            print("Saved", file_path)
            


