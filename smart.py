import os
import openai

from settings_loader import settings_loader


class smart:
    openai.api_key = os.environ['ChatToken']

    def __init__(self):
        self.active_mode = 'быдло'
        self.settings_loader = settings_loader()
        self.settings_loader.LoadSettings()
        self.mode_list = self.settings_loader.modes

    def GenerateAnswer(self, text: str):
        if self.active_mode == 'быдло':
            prompt = 'Ответь как быдло токсично с максимально возможным использованием матов на следующее сообщение - ' + text
        elif self.active_mode == 'аристократ':
            prompt = 'Ответь как самый настоящий аристократ с использованием сложных и умных фраз, которые присущи только высшему обществу, на вопрос - ' + text
        elif self.active_mode == 'офисный работяга':
            prompt = 'Ответь как обычный человек работяга, который работает в офисе, на вопрос - ' + text
        elif self.active_mode == 'стандарт':
            prompt = text
        elif self.active_mode == 'глупый школьник':
            prompt = 'Ответь как глупый школьник, который учится в 7 классе Российской школы, который максимально неадекватный и тупой, с использованием фраз присущих только малолетним школьникам, на вопрос - ' + text
        else:
            prompt = f'Ответь как {self.active_mode} на вопрос - ' + text
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

    def UpdateModesFromFile(self):
        self.settings_loader.LoadSettings()
        self.mode_list = self.settings_loader.modes

    def SetMode(self, mode: str):
        self.active_mode = mode

    def AddMode(self, mode: str):
        self.settings_loader.AddNewMode(mode)
        self.UpdateModesFromFile()
