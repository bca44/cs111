from Grid import *
from Particle import *

class Sand( Particle ):
    def is_move_ok( self , x , y):
        return self.grid.in_bounds( x , y ) and self.grid.get( x , y ) is None

    def physics( self ):
        # straight down
        if self.is_move_ok( self.x , self.y + 1 ):
            return self.x , self.y + 1

        # diag left - check corner case !
        elif self.is_move_ok( self.x - 1, self.y + 1 ):
            try:
                if self.grid.get(self.x - 1, self.y) is None:
                    return self.x - 1 , self.y + 1
            except IndexError as e:
                pass
        # diag right - check corner case !
        elif self.is_move_ok( self.x + 1, self.y + 1 ):
            try:
                if self.grid.get( self.x + 1 , self.y ) is None:
                    return self.x + 1 , self.y + 1
            except IndexError as e:
                pass
        # if nothing works
        else:
            return None
