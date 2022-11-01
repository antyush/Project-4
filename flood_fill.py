from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    # If it's not a boundary or old value we can continue
    if input_board[x][y] != "x" or input_board[x][y] == new:
        return
    #Checking if it is not any other character
    if input_board[x][y] != old:
        return
    # set current value to new value
    input_board[x][y] == new
    # fill above, to the left, to the right, and below
    # call the function for each position
    flood_fill(x, y+1, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x+1, y, old, new)
    flood_fill(x, y-1, old, new)
    return(input_board)

flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....