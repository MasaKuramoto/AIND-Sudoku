
from utils import *
import os

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units

# TODO: Update the unit list to add the new diagonal units
diagonal_unit = []
j = 0
for i in rows:
    c2 = cols[j]
    diagonal_unit.append(i + c2)
    j = j + 1
diagonal_unit2 = []
for i in rows:
    c2 = cols[j-1]
    diagonal_unit2.append(i + c2)
    j = j - 1
diagonal_units = [diagonal_unit] + [diagonal_unit2]
unitlist = unitlist + diagonal_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

possible_solutions_1 = {
'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1',
 'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8',
 'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
 'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4',
 'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
 'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347',
 'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
 'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279',
 'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'}

possible_solutions_2 = {
'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7',
 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9',
 'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
 'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
 'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
 'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6',
 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}

test = {"C3": "7", "D7": "14579", "E6": "7", "E1": "135689", "C7": "2456",
"I6": "12458", "E2": "135689", "H8": "27", "F2": "12345789", "G7":
"1569", "D5": "12356", "C5": "12568", "G9": "5689", "I8": "27", "B5":
"123567", "E9": "2", "A3": "34589", "F6": "123589", "A7": "24567",
"H2": "3589", "C8": "3", "C6": "1245689", "G2": "34589", "A5":
"235678", "I5": "9", "G6": "134568", "B7": "8", "H7": "25679", "B9":
"567", "F9": "3579", "A2": "2345689", "I1": "458", "I9": "578", "G3":
"2", "D2": "12345679", "I2": "458", "F5": "12358", "F8": "6", "E8":
"15", "C2": "1245689", "H6": "23568", "F1": "1234589", "E3": "3589",
"E4": "135689", "B3": "345", "F4": "123589", "E7": "159", "G8": "15",
"H3": "1", "I4": "124578", "G5": "13568", "D6": "123569", "G4":
"134568", "B4": "1234567", "E5": "4", "A4": "23456789", "H4":
"235678", "D3": "3459", "D1": "1234569", "C1": "1245689", "B6":
"123456", "H9": "4", "H1": "3589", "B2": "123456", "C4": "1245689",
"A6": "2345689", "B1": "123456", "B8": "9", "A8": "4", "G1": "7",
"A9": "1", "D8": "8", "H5": "235678", "D9": "3579", "A1": "2345689",
"D4": "123569", "C9": "56", "I7": "3", "F7": "14579", "I3": "6", "F3":
"34589"}

test_solution = {"C3": "7", "D7": "47", "E6": "7", "I6": "12458", "F9": "39", "G9":
"8", "E2": "3689", "B5": "123567", "E9": "2", "F6": "123589", "A7":
"2", "C8": "3", "G2": "34589", "A5": "235678", "H4": "235678", "D8":
"8", "B7": "8", "H7": "69", "B9": "567", "G7": "69", "A2": "2345689",
"I1": "458", "I9": "8", "E5": "4", "I2": "458", "F8": "6", "C2":
"1245689", "E3": "389", "B3": "345", "E7": "15", "G5": "13568", "B4":
"1234567", "A4": "23456789", "C1": "1245689", "I4": "124578", "H9":
"4", "H1": "3589", "C4": "1245689", "A6": "2345689", "B8": "9", "G1":
"7", "D2": "12345679", "D9": "39", "C9": "56", "F7": "47", "I3": "6",
"F3": "34589", "E1": "3689", "C7": "2", "F2": "12345789", "F1":
"1234589", "C5": "12568", "I8": "27", "H5": "235678", "A3": "34589",
"H2": "3589", "C6": "1245689", "D1": "1234569", "I5": "9", "G6":
"134568", "B2": "123456", "D4": "123569", "G3": "2", "H8": "27", "F5":
"12358", "H6": "23568", "D5": "12356", "E4": "3689", "E8": "15", "G8":
"15", "D6": "123569", "G4": "134568", "H3": "1", "A9": "1", "B6":
"123456", "F4": "123589", "B1": "123456", "D3": "3459", "A8": "4",
"A1": "2345689", "I7": "3"}

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).
    """
    # TODO: Implement this function!

    # list of values
    values_sorted = dict()
    for key, item in sorted(values.items()):
        values_sorted[key] = item
    values = values_sorted

    val_list = []
    for box in values.keys():
        val_list.append(values[box])
    # list of naked_twins
    naked_twins = []
    for box in values.keys():
        if val_list.count(values[box]) > 1 and len(values[box]) == 2:
            naked_twins.append(box)

    # search from the list of naked twins
    for box in naked_twins:
        d = values[box]
        # search from the list of units
        for unit in units[box]:
            # find if the unit includes with the numbers in the naked twins list
            naked_twins_set = set(naked_twins)
            unit_set = set(unit)
            matched_list = list(naked_twins_set & unit_set)
            matched_list_val = []
            for matched in matched_list:
                matched_list_val.append(values[matched])
            for matched_val in matched_list_val:
                # only search for the same numbers
                if matched_list_val.count(matched_val) == 2 and matched_val == d:
                    for x in unit:
                        # ignore if the nubmers are the naked pairs or the only value
                        if d == values[x] or len(values[x]) == 1:
                            continue
                        # else delete the numbers and update the list
                        else:
                            for num in d:
                                if num in values[x]:
                                    values[x] = values[x].replace(num,'')
                                else:
                                    continue
    return values

def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    # TODO: Copy your code from the classroom to complete this function
    s = []
    for box in values.keys():
        if len(values[box]) == 1:
            s.append(box)
    for box in s:
        d = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(d,'')
    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """
    # TODO: Copy your code from the classroom to complete this function
    for x in unitlist:
        # print(x)
        for num in '123456789':
            d = [box for box in x if num in values[box]]
            if len(d) == 1:
                values[d[0]] = num
    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable
    """
    # TODO: Copy your code from the classroom and modify it to complete this function
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """
    # TODO: Copy your code from the classroom to complete this function
    values = reduce_puzzle(values)

    if values is False:
        return False
    if all(len(values[x]) == 1 for x in boxes):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    y,x = min((len(values[x]), x) for x in boxes if len(values[x]) != 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for i in values[x]:
        new_sudoku = values.copy()
        new_sudoku[x] = i
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
