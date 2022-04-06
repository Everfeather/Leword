import random


def gen_wordle_word():
    words = open("all-words.txt", 'r')
    possible_answers = []
    for line in words.readlines():
        word = line.strip()
        possible_answers.append(word)
    return possible_answers[random.randint(0, len(possible_answers))]


class Wordle:
    def __init__(self):
        self.wordle_word = gen_wordle_word()
        self.num_guesses = 0
        self.game_over = False
        self.words_guessed = []
        self.states = []
        self.num_guesses_to_win = []
        self.wins = 0
        self.loses = 0

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
        self.words_guessed.append(word)
        self.states.append(s)

        if word == self.wordle_word:
            self.game_over = True
            self.wins += 1
            self.num_guesses_to_win.append(self.num_guesses)
            return "you win!"

        if self.num_guesses == 6:
            self.game_over = True
            self.loses += True
            return "you lose ):"

        return s

    def reset(self):
        self.wordle_word = gen_wordle_word()
        self.num_guesses = 0
        self.game_over = False
        self.words_guessed = []
        self.states = []

    def avg_number_of_guesses(self):
        n = 0
        for i in self.num_guesses_to_win:
            n += i
        return n / len(self.num_guesses_to_win)

    def print_stats(self):
        sum = self.wins + self.loses
        print("games played: " + str(sum))
        print("games won: " + str(self.wins))
        print("games lost: " + str(self.loses))
        print("win % : " + str((self.wins / sum) * 100))
        print("Average number of guesses to win: " + str(self.avg_number_of_guesses()))

    def run(self):
        while True:
            word = input("guess a word\n")
            print(self.guess(word))
            if self.game_over:
                print("word was: " + self.wordle_word)


#game = Wordle()
#game.run()
