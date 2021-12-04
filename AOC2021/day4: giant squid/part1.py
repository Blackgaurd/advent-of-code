# completely forgot to check for diagonals but hey it works

import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

arr = map(int, input().split(','))
boards = []
for i in range(100):
    input()
    board = [list(map(int, input().split())) for i in range(5)]
    boards.append(board)

if __name__ == "__main__":
    for num in arr:
        for board in boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1
            for row in range(5):
                if sum(board[row]) == -5:
                    ttl = 0
                    for i in range(5):
                        for j in range(5):
                            if board[i][j] != -1:
                                ttl += board[i][j]
                    print(ttl * num)
                    sys.exit()
            board = list(map(list, zip(*board)))
            for row in range(5):
                if sum(board[row]) == -5:
                    ttl = 0
                    for i in range(5):
                        for j in range(5):
                            if board[i][j] != -1:
                                ttl += board[i][j]
                    print(ttl * num)
                    sys.exit()


