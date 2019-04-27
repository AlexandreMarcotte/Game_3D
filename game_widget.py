# -- General Packages --
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph.dockarea import *
# -- My Packages --
from game_tab import GameTab


class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_tab_w()
        self.init_docks()
        self.create_tab()

        self.setLayout(self.layout)

    def init_tab_w(self):
        self.layout = QHBoxLayout(self)
        # Add docs to the tab
        self.area = DockArea()
        self.layout.addWidget(self.area)

    def init_docks(self):
        self.eeg_layout, self.eeg_dock = self.create_layout(
                'Game', 'left', size=(5, 15))

    def create_layout(
            self, dock_name, pos, related_dock=None, size=(1, 1),
            hide_title=False, scroll=False):
        dock = Dock(dock_name, size=size)
        self.area.addDock(dock, pos, related_dock)
        layout = pg.LayoutWidget()
        dock.addWidget(layout)
        return layout, dock

    def create_tab(self):
        game_tab = GameTab(self.eeg_dock)
