# генераторы

# pairs = [(i, j) for i in range(5) for j in range(5) if i != j]
#
# number = range(1, 16)
# every_third = [item for item in number if item % 3 == 0]

# Задача: Фильтрация и преобразование строк
# У тебя есть список строк, содержащих различные слова. Твоя задача — создать новый список, который будет содержать только те слова, которые:
# Состоят из более чем 5 символов.
# Начинаются с заглавной буквы.

# words = ['Python', 'is', 'a', 'programming', 'language', 'with', ]
# sorted_words = [item for item in words if len(item) > 5 and item.istitle()]
# print(sorted_words)
# new_words = [item for item in words if item not in sorted_words]
# print(new_words)


def text(text):
    unique_words = set(text.split())
    print(f'Количество уникальных слов в тексте: {len(unique_words)}')
    text_word = {}
    for word in unique_words:
        text_word[word] = text.split().count(word)
        if word == word[::-1] and len(word) > 1:
            print(f'{word} - палиндром')
    print(f'Слова и их количество в тексте: {text_word}')
    word_count = len(text.split())
    print(f'Количество слов в тексте: {word_count}')
    sing_count = len(text)
    print(f'Количество символов в тексте: {sing_count}')
    if word_count >= 500:
        print('Это удовлетворительный текст')
    elif word_count <= 100:
        print('Это короткий текст')
    if 'привет' in text.lower():
        print('В тексте есть слово "привет"')
    if any(item in text for item in ["@", '&', '#', '$', '%', '^', '*', '(', ')', '-', '_', '+', '=', '[', ']']):
        print('В тексте есть знаки пунктуации')


text("""
Это пример текста, содержащего несколько слов. Этот текст включает в себя палиндромы, такие как уровень, казак, и мадам. Кроме того, в тексте есть другие слова, которые могут быть полезны для проверки. Например, анна, каток, и топот. Текст также содержит знаки пунктуации: @, #, $, и %%. Кроме того, слова, такие как hello и привет, могут быть найдены в тексте. Проверьте, есть ли здесь палиндромы и знаки пунктуации.
""")
