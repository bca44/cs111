from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__( self , width : int , height : int ):
        """
        init Grid obj
        >>> grid_1 = Grid(3, 4)
        >>> grid_1.width
        3
        >>> grid_1.height
        4
        """
        self.width = width
        self.height = height
        self.array = [ [ None for _ in range( width ) ] for _ in range( height ) ]

    def __str__( self ):
        """
        Grid(<height>, <width>, first = <first element>)
        """
        return f"Grid({ self.height }, { self.width }, first = { self.array[ 0 ][ 0 ] })"

    def __repr__( self ):
        """
        Grid.build({self.array})
        """
        return f"Grid.build({self.array})"

    def __eq__( self , other : any ):
        """
        checks if other is Grid
        and if other self's and other's arrays are equal
        >>> grid_1 = Grid( 3 , 4 )
        >>> grid_2 = Grid( 3 , 4 )
        >>> grid_1 == grid_2
        True
        >>> grid_2.set( 1 , 1 , "Milk" )
        >>> grid_1 == grid_2
        False
        >>> "grid_1" == grid_2
        False
        """
        if isinstance( other , Grid ):
            return self.array == other.array
        elif isinstance( other , list ):
            return self.array == other
        return False

    def get( self , x : int , y : int ):
        """
        return contents of grid at (x, y) OR error if out of bounds
        >>> grid = Grid(2, 2)
        >>> grid.array = [[1, 2], [4, 5]]
        >>> grid.get(0, 1)
        4
        >>> grid.get(1, 0)
        2
        """
        if not self.in_bounds( x , y ):
            raise IndexError( f"Index ({ x }, { y }) is out of bounds" )
        return self.array[y][x]

    def set( self , x  : int , y : int , val : any ):
        """
        set grid at (x, y) to val
        error if (x, y) out of bounds
        >>> grid = Grid(2, 2)
        >>> grid.set(1, 1, "Milk")
        >>> grid.set(1, 0, "Dud")
        >>> grid.array
        [[None, 'Dud'], [None, 'Milk']]
        """
        if not self.in_bounds( x , y ):
            raise IndexError( f"Index ({ x }, { y }) is out of bounds" )
        self.array[y][x] = val

    def copy( self ):
        return deepcopy( self )

    def in_bounds( self , x , y ):
        """
        Check if (x, y) is in bounds of grid
        """
        return ( 0 <= x < self.width ) and ( 0 <= y < self.height )

    @staticmethod
    def check_list_malformed( lst : list ):
        """
        Given a list that represents a 2D nested Grid, check that it has the right shape.
        Raise a ValueError if it is malformed.
        >>> Grid.check_list_malformed([[1, 2], [4, 5]])
        >>> Grid.check_list_malformed(1)
        Traceback (most recent call last):
        ...
        ValueError: Input must be a non-empty list of lists.
        >>> Grid.check_list_malformed([[1, 2], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: All items in list must be lists of the same length.
        >>> Grid.check_list_malformed([[1, 2], 3])
        Traceback (most recent call last):
        ...
        ValueError: Input must be a list of lists.
        """
        # The object passed in should be a list object
        if isinstance( lst , list ) and (
            len( lst ) > 0 ) and (
            all( [ isinstance( sublist , list ) for sublist in lst] ) ) and (
            all( [ len( sublist ) == len( lst[ 0 ] ) for sublist in lst] )
        ):
            return

        raise ValueError ( "Input must be a non-empty list of lists." )

    @staticmethod
    def build( lst : list ):
        """
        Given a list that represents a 2D nested Grid, construct a Grid object.
        Grid.build([[1, 2, 3], [4, 5 6]])
        >>> Grid.build([[1, 2, 3], [4, 5, 6]]).array
        [[1, 2, 3], [4, 5, 6]]
        """
        try:
            Grid.check_list_malformed( lst )
        except ValueError as e:
            return
        grid_obj = Grid( len( lst[ 0 ] ) , len( lst ) )
        grid_obj.array = deepcopy( lst )

        return grid_obj

