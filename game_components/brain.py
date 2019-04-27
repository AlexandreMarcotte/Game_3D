import pyqtgraph.opengl as gl
import numpy as np


class Brain:
    def __init__(self, win, square_size):
        self.square_size = square_size

        self.add_brain_lines(win)

    def add_brain_lines(self, win):
        self.lines = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                top_pos = [i * self.square_size, j * self.square_size, 10]
                self.lines.append(gl.GLLinePlotItem(
                    pos=np.array([[-1.5, 1.5, 0], top_pos]), width=0.8,
                    color=np.array([[200, 200, 200, 0.5], [0, 0, 200, 0.5]])))
                win.addItem(self.lines[-1])

    def update_brain_lines(self, translate_arr):
        for line in self.lines:
            line.translate(*translate_arr)
