def get_stickers():
    file = open('stickers.txt', 'r', encoding='utf8')
    lines = file.readlines()
    stickers = []
    for line in lines:
        line = line.replace('\n', '')
        stickers.append(line)
    file.close()
    return stickers
