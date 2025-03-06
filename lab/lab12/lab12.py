from Grid import Grid
from random import *

def print_grid(grid):
    """
    Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    """
    Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    grid_copy = grid.copy()
    return modify_grid(grid_copy, lambda x, y: grid_copy.set(x, y, "r"), chance_of_rock)


def random_bubbles(grid, chance_of_bubbles):
    """
    Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    grid_copy = grid.copy()
    return modify_grid(grid_copy, lambda x, y: grid_copy.set(x, y, "b"), chance_of_bubbles)


def modify_grid(grid, func, prob):
    """
    Write a function which can take in a grid, a function
    and a probability as parameters and updates the grid using
    the function passed in.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) is None and random() <= prob:
                func(x, y)
    return grid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    def can_move_up(x, y):
        try:
            return grid.get(x, y) == "b" and grid.get(x, y - 1) is None
        except IndexError:
            return False

    grid_copy = grid.copy()
    if can_move_up(x, y):
        grid_copy.set(x, y, None)
        grid_copy.set(x, y - 1, "b")
    return grid_copy


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    grid_copy = grid.copy()
    for y in range(grid.height):
        for x in range(grid.width):
            grid_copy = bubble_up(grid_copy, x, y)
    return grid_copy


def animate_grid(grid, delay):
    """
    Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1

if __name__ == "__main__":
    grid1 = Grid( 3 , 4 )
    grid3 = random_bubbles(grid1, 0.5)
    animate_grid(grid3, 1)
