import random


def gen_wordle_word():
    words = open("all-words.txt", 'r')
    possible_answers = []
    for line in words.readlines():
        word = line.strip()
        possible_answers.append(word)
    return possible_answers[random.randint(0,len(possible_answers))]


class Wordle:
    def __init__(self):
        self.wordle_word = gen_wordle_word()
        self.num_guesses = 0

    def guess(self, word):
        if len(word) != 5:
            return None
        s = ""
        for i in range(5):
            if self.wordle_word[i] == word[i]:
                s += "g"
            elif word[i] in self.wordle_word:
                s += "y"
            else:
                s += "n"
        self.num_guesses += 1
        if word == self.wordle_word:
            return "you win!"
        if self.num_guesses == 6:
            print("word was: " + self.wordle_word)
            self = Wordle()
            return "you lose ):"

        return s

    def run(self):
        while True:
            word =  input("guess a word\n")
            print(self.guess(word))


game = Wordle()
game.run()