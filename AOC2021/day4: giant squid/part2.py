# oh my gosh is this messy
# tried to go for globals today

import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

arr = map(int, input().split(","))
boards = []
for i in range(100):
    input()
    board = [list(map(int, input().split())) for i in range(5)]
    boards.append(board)

completed = [True for i in range(len(boards))]


def sum2d(board):
    ret = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != -1:
                ret += board[i][j]
    return ret


if __name__ == "__main__":
    foundfinal = False
    for num in arr:
        idx = 0
        if not foundfinal:
            for board in boards:
                if not completed[idx]:
                    idx += 1
                    continue
                for i in range(5):
                    for j in range(5):
                        if board[i][j] == num:
                            board[i][j] = -1
                for row in board:
                    if sum(row) == -5:
                        completed[idx] = False
                board = list(map(list, zip(*board)))
                for row in board:
                    if sum(row) == -5:
                        completed[idx] = False
                board = list(map(list, zip(*board)))
                dagttl = sum(board[i][i] for i in range(5))
                dag2ttl = sum(board[i][5 - i - 1] for i in range(5))
                if dagttl == -5 or dag2ttl == -5:
                    completed[idx] = False
                idx += 1
            if sum(completed) == 1:
                for i in range(len(boards)):
                    if completed[i]:
                        finalboard = boards[i]
                        foundfinal = True
        else:
            for i in range(5):
                for j in range(5):
                    if finalboard[i][j] == num:
                        finalboard[i][j] = -1
            for row in board:
                if sum(row) == -5:
                    print(sum2d(finalboard) * num)
                    sys.exit()
            board = list(map(list, zip(*board)))
            for row in board:
                if sum(row) == -5:
                    print(sum2d(finalboard) * num)
                    sys.exit()
