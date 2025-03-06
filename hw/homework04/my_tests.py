from Grid import *
from Sand import *


if __name__ == '__main__':
    grid_1 = Grid(3,4)
    sand_1 = Sand( grid_1 , 2 , 2 )

    print( f"Sand_1: { sand_1.grid.array }")

    sand_1.move()


