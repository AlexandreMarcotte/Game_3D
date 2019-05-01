import pyqtgraph.opengl as gl
from PyQt5 import QtGui
from shape.cube import cube

class Grid:
    def __init__(self, win, square_size):
        self.side_size = 35
        self.add_grid_to_window(win, square_size)
        self.add_walls(win, square_size)

    def add_grid_to_window(self, win, square_size):
        g = gl.GLGridItem(size=QtGui.QVector3D(
                self.side_size, self.side_size, 1))
        g.scale(square_size, square_size, square_size)
        win.addItem(g)

    def add_walls(self, win, square_size):
        for j in range(100):
            for i in range(10):
                brick = cube(pos=(i, j, 10), s=(square_size, square_size, square_size))
                win.addItem(brick)
