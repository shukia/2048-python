from agent import *
from random import randint


class RandomPlayer:
    def __init__(self):
        self.agent = Agent()
        self.agent.initialize_game()
        self.state = 'not over'
        self.score = 0
        self.matrix = []

    def play(self):
        direction_enumerate = ['up', 'right', 'down', 'left']
        while self.state == 'not over':
            direction = direction_enumerate[randint(0, 3)]
            self.matrix, self.score, self.state = self.agent.move(direction)
        # print('score: ', self.score)
        print('max tile: ', max(max(x) for x in self.matrix))


class GreedyPlayer:
    def __init__(self):
        self.agent = Agent()
        self.agent.initialize_game()
        self.state = 'not over'
        self.score = 0
        self.matrix = []

    def play(self):
        direction_enumerate = ['up', 'right', 'down', 'left']
        while self.state == 'not over':
            simulated_score = [-1 for _ in range(4)]
            for j in range(4):
                mat, score, state, board_changed = self.agent.simulate_move(direction_enumerate[j])
                # print('d= ', j, ', mat= ', mat, ', self.matrix= ', self.matrix, ', board_changed= ', board_changed)
                if board_changed:
                    simulated_score[j] = score
            self.matrix, self.score, self.state = self.agent.move(
                direction_enumerate[simulated_score.index(max(simulated_score))])
            # print(simulated_score.index(max(simulated_score)))
        # print('score: ', self.score)
        print('max tile: ', max(max(x) for x in self.matrix))


for i in range(100):
    game = GreedyPlayer()
    game.play()
