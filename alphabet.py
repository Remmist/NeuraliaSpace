from typing import List

dictionary = {
    '': '',
    ' ': ' ',
    ',': ' ',
    '.': ' ',
    '?': ' ',
    '!': ' ',
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

# print(translate(['Привет']).capitalize())
