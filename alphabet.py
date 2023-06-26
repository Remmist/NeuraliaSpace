import re
from typing import List

dictionary = {
    ' ': ' ',
    ',': ',',
    '.': '.',
    '?': '?',
    '!': '!',
    'а': 'уэ',
    'б': 'ай',
    'в': 'жо',
    'г': 'гхы',
    'д': 'лог',
    'е': 'ау',
    'ё': 'аю',
    'ж': 'пир',
    'з': 'ла',
    'и': 'ео',
    'й': 'ио',
    'к': 'врэ',
    'л': 'хвы',
    'м': 'дыг',
    'н': 'оуст',
    'о': 'ыва',
    'п': 'прэ',
    'р': 'гви',
    'с': 'сарь',
    'т': 'йы',
    'у': 'уга',
    'ф': 'сик',
    'х': 'пфу',
    'ц': 'хр',
    'ч': 'кер',
    'ш': 'кас',
    'щ': 'лир',
    'ь': 'б',
    'ы': 'сви',
    'ъ': 'ъ',
    'э': 'эй',
    'ю': 'фты',
    'я': 'ря'
}

reversed_dictionary = {value: key for key, value in dictionary.items()}


def translate(list: List[str]):
    for word in list:
        list[list.index(word)] = word.lower()
    letters = []
    out = ''
    for word in list:
        for letter in word:
            letters.append(letter)
    for letter in letters:
        out += dictionary.get(letter)
    return out.capitalize()


def retranslate(text: str):
    words = re.split(r'(\s+)', text)
    for word in words:
        words[words.index(word)] = word.lower()
    out = ''
    for word in words:
        letter = ''
        for i in range(word.__len__()):
            letter += word[i]
            if reversed_dictionary.__contains__(letter):
                out += reversed_dictionary.get(letter)
                letter = ''
                continue
            if i + 1 == word.__len__():
                return f'Была обнаружена ошибка при переводе: буквы "{letter}" в алфавите уэайжо не существует.'
    return out.capitalize()


def getAlphabet():
    out = 'Алфавит языка уэайжо выглядит следующим образом:\n'
    for key in dictionary:
        if key == '.' or key == ',' or key == '!' or key == '?' or key == ' ':
            continue
        out += f'буква "{key}" — это "{dictionary.get(key)}"\n'
    return out

# print(translate(['Привет как дела']))
# print(retranslate('Прэгвиеожоауйы, врэуэврэ логаухвыуэ?'))
