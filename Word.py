class Word:

    def __init__(self, word):
        self.score = 0
        self.word = word

    def num_unique_chars(self):
        return len(set(self.word))

    def set_score(self, val):
        self.score = val
