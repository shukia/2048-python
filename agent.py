from logic import *


class Agent:
    def __init__(self):
        self.matrix = []
        self.score = 0

    def initialize_game(self):
        self.score = 0
        self.matrix = new_game(4)
        self.matrix = add_two(self.matrix)
        self.matrix = add_two(self.matrix)

    def move(self, direction):
        self.matrix, board_changed, score_change = move(self.matrix, direction)
        if board_changed:
            self.matrix = add_two(self.matrix)
        self.score += score_change
        return self.matrix, self.score, game_state(self.matrix)

    def simulate_move(self, direction):
        mat, board_changed, score_change = move(self.matrix, direction)
        return mat, self.score + score_change, game_state(mat), board_changed

