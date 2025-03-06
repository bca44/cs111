from Grid import Grid

if __name__ == "__main__":

    # BUILD test
    lst_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"lst_1: {lst_1}")
    grid_1 = Grid.build(lst_1)
    print(f"grid_1: {grid_1}")
    print(f"grid_1 before changing lst_1: {grid_1}")
    lst_1 = [[2, 2, 3], [4, 5, 6]]
    print(f"grid_1 after changing lst_1: {grid_1}")
    # pass
