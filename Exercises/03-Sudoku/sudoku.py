# %% ----- Sudoko ------------------------------


import random
from typing import List
import re


def mirror(i, j):
    return 9-1-i, 9-1-j

def init_sudoku_board(n=18) -> List[List[int]]:
    sudoku_board = []
    for i in range(9):
        x = [0 for j in range(9)]
        sudoku_board.append(x)

    free_indices = list(range(0, 81))

    k = 0
    while k < n:
        ix = random.choice(free_indices)
        i1 = ix // 9
        j1 = ix % 9

        v1 = random.randint(1, 9)
        if can_place(sudoku_board, i1, j1, v1):
            sudoku_board[i1][j1] = v1
            k += 1

        # here we mirror the indices to generate a (quasi) symmetric board
        i2, j2 = mirror(i1, j1)
        v2 = random.randint(1, 9)
        if can_place(sudoku_board, i2, j2, v2) and k < n:
            sudoku_board[i2][j2] = v2
            k += 1

    return sudoku_board


def can_place(sudoku_board, i, j, v):
    # On the board, place value v at coordinates (i,j)

    if sudoku_board[i][j] != 0:
        return False # Return false, if the place is already taken

    for k in range(9):  # Check horizontal and vertical in one loop
        if sudoku_board[i][k] == v:
            return False
        if sudoku_board[k][j] == v:
            return False

    # Check 3 by 3 square
    i_o = (i // 3) * 3
    j_o = (j // 3) * 3
    for x in range(i_o, i_o+3):
        for y in range(j_o, j_o+3):
            if sudoku_board[x][y] == v:
                return False

    return True  # if there are no violations, it safe to place the value


def pretty_print_sudoku_board(board: List[List[int]]):
    print("┌───────┬───────┬───────┐")
    for i in range(9):
        row = board[i]
        if i in (3, 6):
            print("├───────┼───────┼───────┤")
        values_to_print = [" " if v == 0 else str(v) for v in row]
        print("│ {} {} {} │ {} {} {} │ {} {} {} │".format(*values_to_print))
    print("└───────┴───────┴───────┘")


def find_first_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def solve_sudoku(board: List[List[int]], print_board=False) -> bool:
    """solve_sudoku

    Solves the given sudoku board using backtracking.

    Args:
        board (List[List[int]]): the sudoku board to solve
        print_board (bool, optional): Print the board when successfully solved. Defaults to False.

    Returns:
        bool: True, if the board has been solved, otherwise false
    """
    i, j = find_first_empty(board)  # find first that value that is not zero
    if i == -1 and j == -1:         # in case there are no more free spaces (sudoku is solved)
        if print_board:             # print the board, if we wish so
            pretty_print_sudoku_board(board)
        return True                 # return True, to mark it as solved

    for k in range(1, 10):
        if can_place(board, i, j, k):
            board[i][j] = k  # we can place the number 'k' so try it
            is_solved = solve_sudoku(board, print_board=print_board)
            if is_solved:
                return True
            board[i][j] = 0  # undo
    return False


def play(n=22):
    is_solvable = False
    board = None
    MAX_TRIES = 100
    PATTERN = re.compile(r"(\d)\s+(\d)\s+(\d)")     # matches 3 digits separated by whitespaces

    k = 0
    while k < MAX_TRIES and is_solvable is False:
        board = init_sudoku_board(n=n)
        board_copy = [[board[i][j] for j in range(9)] for i in range(9)]
        is_solvable = solve_sudoku(board=board_copy)
        k += 1

    if board is None and k == MAX_TRIES:
        print("ERROR: could not find a solvable sudoku after 100 tries, maybe reduce number of digits")
        exit(-1)

    wants_to_quit_game = False
    while wants_to_quit_game is False:
        pretty_print_sudoku_board(board)
        print("Enter three numbers to place a digit (1 2 3) or q to quit or s to solve.")
        response = input("> ")
        if response == "q":
            wants_to_quit_game = True
            print("Bye!")
        elif response == "s":
            wants_to_quit_game = True
            print("solving....")
            solve_result = solve_sudoku(board, print_board=False)
            if solve_result == False:
                print("Sorry, you entered some wrong numbers and the board is not solvable :( ")
            else:
                pretty_print_sudoku_board(board)
        else:
            m = PATTERN.match(response)  # check 
            if m is None:
                print(f"input '{response}' not recognized.")
                continue
            i, j, v = m.groups()
            i, j, v = int(i), int(j), int(v)

            if can_place(board, i, j, v):
                board[i][j] = v
            else:
                print("This move is not allowed")





#S = init_sudoku_board(n=22)
#pretty_print_sudoku_board(S)
#solve_sudoku(S, print_board=True)

play(n=25)

# %%
