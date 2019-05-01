# Shape
from shape.cube import Cube
from shape.pyramid import pyramid
from shape.square import square
from shape.triangle import triangle
import pyqtgraph.opengl as gl
from PyQt5 import QtGui, QtCore
from collections import deque
# -- My Packages --
from game_components.brain import Brain
from game_components.apple import Apple
from extra_function.keyboard_listener import KeyboardListener
import numpy as np


class Snake:
    def __init__(self, win, square_size):
        self.square_size = square_size
        # Keyboard listener
        self.kb_listener = KeyboardListener()
        self.kb_listener.start()

        self.len = 20
        self.head_pos = np.array([0, 0, 0])
        self.body_mvts = deque([], maxlen=self.len)
        self.body_mvts.append(self.kb_listener.key_pressed)
        self.body = []
        self.body_mvts_dict = {
                'l': (self.square_size, 0, 0),
                'j': (-self.square_size, 0, 0),
                'i': (0, self.square_size, 0),
                'k': (0, -self.square_size, 0)}
        self.previous_body_mvt = 'l'

        self.add_to_window(win)
        # Brain
        self.brain = Brain(win, square_size)

    def add_to_window(self, win):
        # Create the snake and it's moving pattern
        for i in range(-self.len, 0):
            if i == 0:
                body_type = Cube
            else:
                body_type = Cube

            body_square = body_type(
                    pos=(i*self.square_size, 0, 0),
                    s=(self.square_size, self.square_size, self.square_size))
            self.body.append(body_square.mesh_item)
            win.addItem(body_square.mesh_item)
            self.body_mvts.append(self.kb_listener.key_pressed)

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
                self.brain.translate(translate_arr)
                self.brain.update_neurons_weight()

                if body_mvt != self.previous_body_mvt:
                    # self.brain.rotate(body_mvt, self.head_pos)
                    self.previous_body_mvt = body_mvt

        self.head_pos += translate_arr
