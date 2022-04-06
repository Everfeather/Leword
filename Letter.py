from State import State


class Letter:

    def __init__(self, letter):
        self.letter = letter
        self.totalOccurs = 0
        self.pos = [0, 0, 0, 0, 0]
        self.states = [State.WHITE, State.WHITE, State.WHITE, State.WHITE, State.WHITE]

    def increase_pos(self, index):
        self.pos[index] += 1
        self.totalOccurs += 1

    def change_state(self, state, index):
        if state is State.GRAY:
            for i in range(len(self.states)):
                self.states[i] = State.GRAY
        else:
            self.states[index] = state

    def reset_frequency(self):
        self.pos = [0, 0, 0, 0, 0]
        self.totalOccurs = 0
