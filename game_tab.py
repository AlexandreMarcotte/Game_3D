# -- General Packages --
from PyQt5.QtCore import pyqtSlot
import pyqtgraph.opengl as gl
from PyQt5 import QtGui, QtCore
from functools import partial
# -- My packages --
import numpy as np
from game_components.snake import Snake


class GameTab:
    def __init__(self, dock):
        self.dock = dock
        self.square_size = 3
        self.w = self.init_win()
        self.add_snake()
        self.dock.addWidget(self.w, 1, 0)

        self.timer_effect = self.init_timer()
        self.add_start_button()

    def init_win(self):
        w = gl.GLViewWidget()
        w.setCameraPosition(distance=220, azimuth=-90, elevation=90)
        return w

    def add_snake(self):
        self.snake = Snake(self.w, self.square_size)

    def add_start_button(self):
        b_start = QtGui.QPushButton('')
        b_start.setStyleSheet('background-color: rgba(0, 0, 0, 0.5)')
        b_start.clicked.connect(partial(self.start_game_timer))
        self.dock.addWidget(b_start, 0, 0)

    def init_timer(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.snake.update)
        timer.start(50)
        return timer

    @pyqtSlot()
    def start_game_timer(self):
        pass




