import os

import openai

ROOT_PATH = '..\\pibulk\\asks\\'
openai.api_key = os.getenv("OPENAI_API_KEY")


def read_question(origin):
    print('Lendo fonte: ' + origin)
    with open(ROOT_PATH + origin, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == '__main__':
    for origin in os.listdir(ROOT_PATH):
        name, ext = os.path.splitext(origin)
        destiny = ROOT_PATH + name + '_answer' + ext
        if not os.path.exists(destiny):
            source = read_question(origin)
            messages = [{"role": "user", "content": source}]
            print('Criando chat...')
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            print('Perguntando...')
            respond = completion.choices[0].message.content
            finish_reason = completion.choices[0].finish_reason
            while finish_reason == 'stop':
                messages = [{"role": "user", "content": "continue"}]
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                respond = completion.choices[0].message.content
                finish_reason = completion.choices[0].finish_reason
            print('Salvando ' + destiny)
            with open(destiny, mode='w', encoding='utf-8') as file:
                file.write(respond)
