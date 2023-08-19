import os


class settings_loader:

    def __init__(self):
        self.modes = []
        self.settings = []

    def LoadSettings(self):
        project_directory = os.getcwd()
        settings_directory = os.path.join(project_directory, 'settings')
        factory_path = os.path.join(settings_directory, 'factory.txt')
        file = open(factory_path, encoding='utf8')
        self.settings = file.readlines()
        for line in self.settings:
            nline = line.replace('\n', '')
            self.settings[self.settings.index(line)] = nline
            if line.startswith('Режимы'):
                line = line.replace('Режимы:', '')
                line = line.replace('\n', '')
                self.modes = line.split(';')
        file.close()

    def AddNewMode(self, mode: str):
        project_directory = os.getcwd()
        settings_directory = os.path.join(project_directory, 'settings')
        factory_path = os.path.join(settings_directory, 'factory.txt')
        file = open(factory_path, 'r', encoding='utf8')
        lines = file.readlines()
        index = 0
        nline = ''
        for line in lines:
            if line.startswith('Режимы'):
                index = lines.index(line)
                nline = line.replace('\n', '')
                nline += f';{mode}\n'
        lines[index] = nline
        file = open(factory_path, 'w', encoding='utf8')
        for line in lines:
            file.write(line)
        file.close()


