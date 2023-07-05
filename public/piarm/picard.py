## Automatic Card Compile
import csv
import os

import piarm


def fix_csv(text):
    text = text.replace(' \\" ', '"')
    text = text.replace(' \\n ', "\n")
    text = text.replace(' \\s ', " ")
    text = text.replace(' \\b ', "")
    text = text.replace(' /b ', "")
    text = text.replace(' \\i ', "")
    text = text.replace(' /i ', "")
    text = text.replace(' \\u ', "")
    text = text.replace(' /u ', "")
    return text


def make_all_cards(origin, destiny):
    with open(origin, mode ='r', encoding='utf-8') as file:
        csvFile = csv.reader(file)
        for i, data in enumerate(csvFile):
            try:
                question = fix_csv(data[1]).split("\n")
                answer = fix_csv(data[2]).split("\n")
                card = []
                card.append("Cartão " + str(i) + ".\n\n")
                card.append("Questão.\n\n")
                card.append("{{Pause=1}}")
                card.append("\n\n")
                for line in question:
                    card.append(line)
                card.append("\n\n")
                card.append("{{Pause=5}}")
                card.append("\n\n")
                card.append("Resposta.\n\n")
                card.append("{{Pause=1}}")
                card.append("\n\n")
                for line in answer:
                    card.append(line)
                card.append("\n\n")
                card.append("{{Pause=5}}\n\n")
                card.append("\n\n")
                card = piarm.adjust_text(card, 'Cartão')
                path = os.path.join(destiny, "Card " + str(i)) + ".txt"
                with open(path, mode='w', encoding='utf-8') as writer:
                    for line in card:
                        writer.write(line)
            except Exception as e:
                print("Error on card " + str(i + 1) + " : " + str(e))
                exit(-1)


if __name__ == "__main__":
    make_all_cards('..\\picard\\aptar.csv', 'C:\\Users\\emuvi\\Downloads')