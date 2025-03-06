from Grid import *

class Particle:
    def __init__( self , grid:Grid , x:int=0 , y:int=0 ):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__( self ):
        return f"{ type( self ).__name__ }({ self.x },{ self.y })"

    def move( self ):
        if not self.physics():
            return
        else:
            self.grid.set( self.x , self.y , None ) # set pre-move to None
            self.x , self.y = self.physics() # update x and y pos
            self.grid.set( self.x , self.y , self ) # update grid

