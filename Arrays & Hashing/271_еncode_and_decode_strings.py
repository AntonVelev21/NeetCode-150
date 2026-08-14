import random
import string


class Solution:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter_separator = random.choice(string.ascii_letters)
    secret_number = random.choice(numbers)
    empty_string_symbol = random.choice(string.ascii_letters)
    word_separator = '|'


    def letter_separator_differs_from_empty_string_symbol(self):
        while self.letter_separator == self.empty_string_symbol:
            self.letter_separator = random.choice(string.ascii_letters)


    def encode(self, strs: list[str]) -> str:
        encoded_string = ''
        for i, word in enumerate(strs):
            if word == '':
                encoded_string += self.empty_string_symbol
                if i != len(strs) - 1:
                    encoded_string += self.word_separator
                continue
            for j, letter in enumerate(word):
                if letter == ' ':
                    encoded_string += ' '
                else:
                    encoded_string += str(ord(letter) + self.secret_number)
                if j != len(word) - 1:
                    encoded_string += self.letter_separator
            if i != len(strs) - 1:
                encoded_string += self.word_separator
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_words = []
        if not s:
            return []
        for word in s.split(self.word_separator):
            if word == self.empty_string_symbol:
                decoded_words.append('')
                continue
            else:
                decoded_word = ''
                for letter in word.split(self.letter_separator):
                    if letter == ' ':
                        decoded_word += ' '
                    else:
                        decoded_word += chr(int(letter) - self.secret_number)
                decoded_words.append(decoded_word)

        return decoded_words

