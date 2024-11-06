#!/usr/bin/python3
""" N queens puzzle, challenge of placing N non attacking queens
on a NxN chessboard
This program solves the N queens problem """

import sys

def print_solution(solution):
    print(solution)

def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def backtrack(row):
        if row == N:
            # Convert board to required format and print it
            solution = [[i, board[i]] for i in range(N)]
            print_solution(solution)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    backtrack(0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)

if __name__ == "__main__":
    main()