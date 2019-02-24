# AI Problem 1

from queue import PriorityQueue
from random import randint

def make_puzzle():
    n_puzzle_list = [0,1,2,3,4,5,6,7,8]
    row1 = [0]*3
    row2 = [0]*3
    row3 = [0]*3
    puzzle = []

    size = 8

    for i in range(0,3):
        index = randint(0, size)
        size -= 1
        row1[i] = n_puzzle_list[index]
        del n_puzzle_list[index]

    for i in range(0, 3):
        index = randint(0, size)
        row2[i] = n_puzzle_list[index]
        del n_puzzle_list[index]
        size -= 1

    for i in range(0, 3):
        index = randint(0, size)
        row3[i] = n_puzzle_list[index]
        del n_puzzle_list[index]
        size -= 1

    puzzle.append(row1)
    puzzle.append(row2)
    puzzle.append(row3)

    return puzzle

print(make_puzzle())
