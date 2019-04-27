# -- General Packages --
from PyQt5.QtCore import pyqtSlot
import pyqtgraph.opengl as gl
from PyQt5 import QtGui, QtCore
from functools import partial
# -- My packages --
import numpy as np
# Shape
from shape.cube import cube
from shape.pyramid import pyramid
from shape.square import square
from shape.triangle import triangle
from pynput import keyboard
from collections import deque


class GameTab:
    def __init__(self, dock):
        self.dock = dock

        self.snake_len = 20
        self.key_pressed = 'l'
        self.keys_pressed = deque([], maxlen=self.snake_len)
        self.keys_pressed.append(self.keys_pressed)

        self.square_size = 3

        self.w = self.init_win()
        self.add_snake()
        self.add_brain_lines()
        self.dock.addWidget(self.w, 1, 0)

        self.timer_effect = self.init_timer()
        self.add_start_button()

        listen_keybr = keyboard.Listener(
                on_press=self.on_press, on_release=self.on_release)
        listen_keybr.start()

    def init_win(self):
        w = gl.GLViewWidget()
        w.setCameraPosition(distance=220, azimuth=-90, elevation=90)
        return w

    def add_snake(self):
        self.snake = []
        # Create the snake and it's moving pattern
        for i in range(-self.snake_len, 0):
            shape = square(pos=(i*self.square_size, 0, 0), s=(
                    self.square_size, self.square_size, self.square_size))
            self.snake.append(shape)
            self.w.addItem(shape)
            self.keys_pressed.append(self.key_pressed)

        g = gl.GLGridItem(size=QtGui.QVector3D(50, 50, 1))
        g.scale(self.square_size, self.square_size, self.square_size)
        self.w.addItem(g)

    def add_brain_lines(self):
        self.lines = []
        for i in range(-5, 6):
            for j in range(-5, 6):
                top_pos = [i*self.square_size, j*self.square_size, 10]
                self.lines.append(gl.GLLinePlotItem(
                        pos=np.array([[-1.5, 1.5, 0], top_pos]), width=0.8,
                        color=np.array([[200, 200, 200, 0.5], [0, 0, 200, 0.5]])))
                self.w.addItem(self.lines[-1])

    def update_brain_lines(self, translate_arr):
        for line in self.lines:
            line.translate(*translate_arr)

    def init_timer(self):
        timer_effect = QtCore.QTimer()
        timer_effect.timeout.connect(self.update_display)
        timer_effect.start(200)
        return timer_effect

    def update_display(self):
        self.keys_pressed.append(self.key_pressed)
        for i, (shape, key_pressed) in enumerate(zip(self.snake, self.keys_pressed)):
            if key_pressed == 'l':
                translate_arr = (self.square_size, 0, 0)
                shape.translate(*translate_arr)
                # self.x_pos += 0.2
            if key_pressed == 'j':
                translate_arr = (-self.square_size, 0, 0)
                shape.translate(*translate_arr)
                # self.x_pos -= 0.2
            if key_pressed == 'i':
                translate_arr = (0, self.square_size, 0)
                shape.translate(*translate_arr)
                # self.y_pos += 0.3
            if key_pressed == 'k':
                translate_arr = (0, -self.square_size, 0)
                shape.translate(*translate_arr)
                # self.y_pos -= 0.3
            # else:
            #     translate_arr = (0, 0, 0)
            # Head of the snake
            if i == self.snake_len-1 and key_pressed in ['l', 'i', 'j', 'k']:
                self.update_brain_lines(translate_arr)

    def on_press(self, key):
        try:
            self.key_pressed = key.char
        except AttributeError:
            # print(f'special key {key} pressed')
            self.key_pressed = key

    def on_release(self, key):
        pass
        if key == keyboard.Key.esc:
            # Stop listener
            pass
    # def update_display(self):
    #     for shape in self.shapes:
            # shape.rotate(0.5, 1, 0, 0)
            # shape.translate(1, 0, 0)

    def add_start_button(self):
        b_start = QtGui.QPushButton('')
        b_start.setStyleSheet('background-color: rgba(0, 0, 0, 0.5)')
        b_start.clicked.connect(partial(self.start_game_timer))
        self.dock.addWidget(b_start, 0, 0)

    @pyqtSlot()
    def start_game_timer(self):
        pass




