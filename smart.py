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
        prompt = f'Ответь как {self.active_mode} на следующее сообщение - ' + text
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
