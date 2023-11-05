# Завести класс, отвечающий за логику игры, который
#
# позволяет настраивать кол-во позволенных ошибок (API принимает соответствующий параметр)
#
#   позволяет клиентскому коду запрашивать генерацию слова
#
#    позволяет клиентскому коду передавать в логику догадку игрока (передача буквы)
#
#    позволяет клиентскому коду запрашивать:
#   - кол-во оставшихся попыток
#   - строку показывающую какие буквы открыты, а какие скрыты (если буква скрыта вместо неё ставим подчёркивание
#   или дефис), т.е., по сути, текущее состояние игры
#   - отсортированные буквы, которые игрок уже называл (вводил)
#
# Клиентский код организует цикл в котором пользуется API класса, который реализует логику игры, и выводит
# все необходимые строки для общения с игроком, показывает текущее состояние игры, поздравляет с победой и уведомляет о поражении.
#
# Файл со словами прикреплён к лекции. Читать можно в кодировке UTF8.

import random


class Game:
    with open('WordsStockRus.txt', mode='r') as file:
        rare_data = file.read()

    list_of_words = rare_data.split('\n')

    def __init__(self, free_tries: int = 10):
        self.current_symbol = None
        self.free_tries = free_tries
        self.attempts: int = 0
        self.key_word = random.choice(Game.list_of_words)
        self.key_symbols = []

        # while (not self.is_win_condition()) and (self.get_available_tries() > 0):
        #     print(f'try to guess this word: {(self.opened_symbols())}')
        #     print(f'Available tries: {self.get_available_tries()}')
        #     self.set_symbol()
        #     print(f'You used this chars: {self.get_symbols()}')

    def generate_word(self):
        self.attempts: int = 0
        self.key_word = random.choice(Game.list_of_words)

        return 'New word was generated.'

    def set_symbol(self):
        self.current_symbol = str(input('Fill one symbol: '))
        self.key_symbols.append(self.current_symbol)
        self.key_symbols.sort()
        if not (self.current_symbol in self.key_word):
            self.attempts += 1

        return 'Symbol was saved.'

    def get_available_tries(self):
        return self.free_tries - self.attempts

    def get_symbols(self):
        return self.key_symbols

    def opened_symbols(self):
        return "".join(i if i in self.key_symbols else '_' for i in self.key_word)

    def is_win_condition(self):
        return all(i in self.key_symbols for i in self.key_word)


# play = Game(10)

# key_word = 'абракадабра'
#
# key_symbols = ['а', 'б']
# print(all(i in key_symbols for i in key_word))
#
# print("".join(i if i in key_symbols else '_' for i in key_word))
