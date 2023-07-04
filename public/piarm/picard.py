## Automatic Card Compile
import csv
import os

import piarm


def transform_from_csv(text):
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
            question = transform_from_csv(data[1]).split("\n")
            answer = transform_from_csv(data[2]).split("\n")
            question = piarm.adjust_text(question, 'Questão')
            answer = piarm.adjust_text(answer, 'Resposta')
            path = os.path.join(destiny, "Card " + str(i)) + ".txt"
            with open(path, mode='w', encoding='utf-8') as writer:
                writer.write("Cartão " + str(i) + ".\n\n")
                writer.write("Questão.\n\n")
                writer.write("{{Pause=2}}")
                writer.write("\n\n")
                for line in question:
                    writer.write(line)
                writer.write("\n\n")
                writer.write("{{Pause=5}}")
                writer.write("\n\n")
                writer.write("Resposta.\n\n")
                writer.write("{{Pause=2}}")
                writer.write("\n\n")
                for line in answer:
                    writer.write(line)
                writer.write("\n\n")
                writer.write("{{Pause=5}}\n\n")
                writer.write("\n\n")

if __name__ == "__main__":
    make_all_cards('..\\picard\\aptar.csv', 'C:\\Users\\emuvi\\Downloads')