def solve_sudoku(sudoku):
    """
    Solves a given Sudoku puzzle.
    :param sudoku: List of 81 integers representing the Sudoku puzzle (0 for empty cells).
    :return: Solved Sudoku board as a list of 81 integers, or None if unsolvable.
    """
    # Input validation
    if not isinstance(sudoku, list) or len(sudoku) != 81:
        raise ValueError("Input must be a list of 81 integers.")
    if any(not isinstance(v, int) or v < 0 or v > 9 for v in sudoku):
        raise ValueError("All elements must be integers between 0 and 9.")

    numbers = set(range(1, 10))

    def options(cell, state):
        """Determines the possible values for a cell."""
        row_idx = cell // 9
        col_idx = cell % 9
        box_row = row_idx // 3 * 3
        box_col = col_idx // 3 * 3

        row = set(state[row_idx * 9:(row_idx + 1) * 9])
        col = set(state[col_idx::9])
        box = set(
            state[r * 9 + c]
            for r in range(box_row, box_row + 3)
            for c in range(box_col, box_col + 3)
        )
        return numbers - (row | col | box)

    initial_state = sudoku[:]
    stack = [initial_state]

    while stack:
        state = stack.pop()
        try:
            empty_idx = state.index(0)
        except ValueError:
            return state  # Solved

        opts = options(empty_idx, state)
        if not opts:
            continue  # Dead end
        for num in opts:
            new_state = state[:]
            new_state[empty_idx] = num
            stack.append(new_state)

    return None  # Unsolvable
