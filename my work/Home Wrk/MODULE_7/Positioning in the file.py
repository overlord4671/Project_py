def custom_write(file_name, string):
    file = open(file_name, 'w', encoding='utf8')

    strings_positions = {}

    for index, line in enumerate(string):
        byte_pos = file.tell()

        file.write(line + '\n')

        strings_positions[index + 1, byte_pos] = line

    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('Positioning in the file.txt', info)
for elem in result.items():
    print(elem)
