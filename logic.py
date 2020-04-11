# CS1010FC --- Programming Methodology

from random import *


def new_game(n):
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix


def add_two(mat):
    a = randint(0, len(mat) - 1)
    b = randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a = randint(0, len(mat) - 1)
        b = randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat


def game_state(mat):
    for i in range(len(mat) - 1):  # intentionally reduced to check the row on the right and below
        for j in range(len(mat[0]) - 1):  # more elegant to use exceptions but most likely this will be their solution
            if mat[i][j] == mat[i + 1][j] or mat[i][j + 1] == mat[i][j]:
                return 'not over'
    for i in range(len(mat)):  # check for any zero entries
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for k in range(len(mat) - 1):  # to check the left/right entries on the last row
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):  # check up/down entries on last column
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'over'


def reverse(mat):
    new_matrix = []
    for i in range(len(mat)):
        new_matrix.append([])
        for j in range(len(mat[0])):
            new_matrix[i].append(mat[i][len(mat[0]) - j - 1])
    return new_matrix


def transpose(mat):
    new_matrix = []
    for i in range(len(mat[0])):
        new_matrix.append([])
        for j in range(len(mat)):
            new_matrix[i].append(mat[j][i])
    return new_matrix


def slide_tiles_left(mat):
    new_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_matrix[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new_matrix, done


def merge(mat):
    done = False
    score_change = 0
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                score_change += mat[i][j]
                mat[i][j + 1] = 0
                done = True
    return mat, done, score_change


def move(game, direction):
    if direction == 'up':
        return up(game)
    elif direction == 'down':
        return down(game)
    elif direction == 'left':
        return left(game)
    elif direction == 'right':
        return right(game)


def up(game):
    # print("up")
    # return matrix after shifting up
    game = transpose(game)
    game, done = slide_tiles_left(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = slide_tiles_left(game)[0]
    game = transpose(game)
    return game, done, temp[2]


def down(game):
    # print("down")
    game = reverse(transpose(game))
    game, done = slide_tiles_left(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = slide_tiles_left(game)[0]
    game = transpose(reverse(game))
    return game, done, temp[2]


def left(game):
    # print("left")
    # return matrix after shifting left
    game, done = slide_tiles_left(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = slide_tiles_left(game)[0]
    return game, done, temp[2]


def right(game):
    # print("right")
    # return matrix after shifting right
    game = reverse(game)
    game, done = slide_tiles_left(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = slide_tiles_left(game)[0]
    game = reverse(game)
    return game, done, temp[2]
