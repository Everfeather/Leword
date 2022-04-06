from Letter import Letter
from Word import Word
from State import State
from wordle import Wordle


class Leword:

    def __init__(self):

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.letters = {}
        for char in alphabet:
            self.letters.update({char: Letter(char)})

        self.words = {}
        self.init_words()
        self.init_letters()
        self.cur_guess = ""

    def reset(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.letters = {}
        for char in alphabet:
            self.letters.update({char: Letter(char)})

        self.words = {}
        self.init_words()
        self.init_letters()
        self.cur_guess = ""

    def init_words(self):
        words = open("all-words.txt", 'r')
        lines = words.readlines()
        for line in lines:
            word = line.strip()
            self.words.update({word: Word(word)})

    def init_letters(self):
        for let in self.letters:
            self.letters.get(let).reset_frequency()

        for key, val in self.words.items():

            word = key.lower()
            count = 0
            for char in word:
                self.letters.get(char).increase_pos(count)
                count += 1
        for key, val in self.words.items():
            self.calc_word_score(self.words.get(key))

    def validate_words(self):
        '''
        removes all invalid words from the word list
        :return:
        '''
        for word in self.words.copy():
            word_lower = word.lower()
            count = 0
            for char in word_lower:
                if self.letters.get(char).states[count] == State.GRAY or \
                        self.letters.get(char).states[count] == State.YELLOW:
                    # print(word_lower)
                    self.words.pop(word_lower)
                    break

                count += 1

    def validate_word(self, word):
        '''
        removes the word from the word list if not a possible word to guess
        :param word: word to be removed. method used
        :return: void
        '''
        count = 0
        for char in word:
            if (self.letters.get(char).states[count] == State.GRAY) or \
                    (self.letters.get(char).states[count] == State.YELLOW):
                print("Invalid word")
                self.words.pop(word)
                return

            count += 1
        print("valid word")

    def calc_word_score(self, word):
        '''
        calculates a word score based on the letter frequency of the remaining words, and number of unique letters
        :param word: word to be scored
        :return: void
        '''
        score = 0

        for index in range(len(word.word)):
            let = word.word[index]
            score += self.letters.get(let).pos[index]
        modifier = word.num_unique_chars() * 0.1 + 1
        word.set_score(score * modifier)

    def find_best_word(self):
        temp = self.words.get(list(self.words.keys())[0])
        for word in self.words:
            if self.words.get(word).score > self.words.get(temp.word).score:
                temp = self.words.get(word)
        self.cur_guess = temp.word
        return temp

    def process_guess(self, colors):
        i = 0

        for c, d in zip(colors, self.cur_guess):
            if c == "g":
                state = State.GREEN
            elif c == "y":
                state = State.YELLOW
            elif c == "n":
                state = State.GRAY
            else:
                return

            self.letters.get(d).change_state(state, i)
            i += 1

    def run(self):
        running = True
        print("next guess: " + self.find_best_word().word)
        while running:
            cmd = input("Enter a command\n")
            cmd_list = cmd.split()
            if cmd_list[0] == "ins":
                self.process_guess(cmd_list[1])

            elif cmd_list[0] == "next":
                self.validate_words()
                self.init_letters()
                print("next guess: " + self.find_best_word().word)

            elif cmd_list[0] == "stop":
                running = False

            elif cmd_list[0] == "words":
                print(len(self.words))

            elif cmd_list[0] == "contains":
                print(cmd_list[1] in self.words)

            elif cmd_list[0] == "validate":
                self.validate_word(cmd_list[1])
            else:
                print("Invalid command\n")

    def auto_run(self, num_games):
        game = Wordle()
        for i in range(num_games):
            game.reset()
            while not game.game_over:
                guess = self.find_best_word().word
                #print("next guess: " + guess)
                colors = game.guess(guess)
                #print(colors)
                self.process_guess(colors)
                self.validate_words()
                self.init_letters()
            self.reset()
        game.print_stats()


def main():
    bot = Leword()
    bot.auto_run(50)


main()
