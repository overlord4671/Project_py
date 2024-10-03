class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        dict = {}

        for filenames in self.file_names:

            with open(filenames, encoding='windows-1251') as file:
                content = file.read().lower()

                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(i, '')

                words = content.split()
                dict[filenames] = words

        return dict

    def find(self, word):

        find = {}
        word = word.lower()
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            if word in words:
                find[filename] = words.index(word)
            else:
                find[filename] = None

        return find

    def count(self, word):

        count = {}
        word = word.lower()
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            count[filename] = words.count(word)

        return count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
