# Shape
from shape.cube import cube
from shape.pyramid import pyramid
from shape.square import square
from shape.triangle import triangle
import pyqtgraph.opengl as gl
from PyQt5 import QtGui, QtCore
from collections import deque
# -- My Packages --
from game_components.brain import Brain
from extra_function.keyboard_listener import KeyboardListener


class Snake:
    def __init__(self, win, square_size):
        self.square_size = square_size
        # Keyboard listener
        self.kb_listener = KeyboardListener()
        self.kb_listener.start()

        self.len = 20
        self.body_mvts = deque([], maxlen=self.len)
        self.body_mvts.append(self.kb_listener.key_pressed)
        self.body = []
        self.body_mvts_dict = {
            'l': (self.square_size, 0, 0),
            'j': (-self.square_size, 0, 0),
            'i': (0, self.square_size, 0),
            'k': (0, -self.square_size, 0)}

        self.add_to_window(win)
        # Brain
        self.brain = Brain(win, square_size)

    def add_to_window(self, win):
        # Create the snake and it's moving pattern
        for i in range(-self.len, 0):
            if i == 0:
                body_type = cube
            else:
                body_type = square

            body_square = body_type(pos=(i*self.square_size, 0, 0),
                                    s=(self.square_size,
                                    self.square_size,
                                    self.square_size))
            self.body.append(body_square)
            win.addItem(body_square)
            self.body_mvts.append(self.kb_listener.key_pressed)

        g = gl.GLGridItem(size=QtGui.QVector3D(50, 50, 1))
        g.scale(self.square_size, self.square_size, self.square_size)
        win.addItem(g)

    def add_mvt_to_body(self):
        self.body_mvts.append(self.kb_listener.key_pressed)

    def update(self):
        self.add_mvt_to_body()

        for i, (body_part, body_mvt) in enumerate(zip(self.body, self.body_mvts)):
            try:
                translate_arr = self.body_mvts_dict[body_mvt]
            except KeyError:
                # You cannot use this key
                translate_arr = (0, 0, 0)

            body_part.translate(*translate_arr)
            # Head of the snake
            if i == self.len-1 and body_mvt in ['l', 'i', 'j', 'k']:
                self.brain.update_brain_lines(translate_arr)


