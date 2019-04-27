import pyqtgraph.opengl as gl
import numpy as np


class Apple:
    def __init__(self, win, square_size):
        self.diameter = 10
        self.pos = np.array(
            [10 * square_size + 1.5,
             10 * square_size + 1.5,
             0])
        self.add_to_window(win)

    def add_to_window(self, win):
        self.mesh = gl.MeshData.sphere(rows=10, cols=10)
        self.item = gl.GLMeshItem(
                meshdata=self.mesh, smooth=True, color=(1, 0, 0, 0.2),
                shader='balloon', glOptions='additive')
        self.item.translate(*self.pos)
        self.item.scale(1, 1, 2)
        win.addItem(self.item)

    def rotate(self):
        temp_pos = np.array(self.pos)
        self.item.translate(*(-temp_pos))
        self.item.rotate(5, 1, 0, 0)
        self.item.translate(*temp_pos)
