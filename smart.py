import os

import openai

openai.api_key = os.environ['ChatToken']


def GenerateAnswer(text: str):
    prompt = 'Ответь как быдло токсично с максимально возможным использованием матов на следующее сообщение - ' + text
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text

