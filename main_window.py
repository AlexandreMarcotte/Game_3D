# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
import os
from functools import partial
# My packages
from game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win_name = 'Game 3D'
        self.win_icon = QtGui.QIcon('./img/polycortex_logo.png')
        self.pos = (0, 0)
        self.size = (1350, 950)
        self.win_intro_message = 'Play the game'
        self.tabs = {GameWidget(): 'Game Widget'}

        self.init_mainwindow()

    def init_mainwindow(self):
        self.setWindowTitle(self.win_name)
        self.setWindowIcon(self.win_icon)
        self.setGeometry(*self.pos, *self.size)
        self.create_menu_bar()
        self.create_toolbar()
        self.create_tabs()
        self.statusBar().showMessage(self.win_intro_message)

    def create_tabs(self):
        tab_w = QTabWidget()

        for name, tab in self.tabs.items():
            tab_w.addTab(name, tab)

        self.setCentralWidget(tab_w)
        self.show()

    def create_menu_bar(self):
        main_menu = self.menuBar()
        self.file = QMenu('&File')
        main_menu.addMenu(self.file)

    def create_toolbar(self):
        base_path = os.getcwd()
        path = os.path.join(base_path, 'img/exit.png')
        exitAct = QAction(QIcon(path), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)