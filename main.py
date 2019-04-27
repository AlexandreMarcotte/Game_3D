# General packages
from PyQt5.QtWidgets import QApplication
import sys
import qdarkstyle
from pyqtgraph.dockarea.Dock import DockLabel
import pyqtgraph as pg
# My packages
from main_window import MainWindow
from extra_function.change_pyqtgraph_tab_color import update_style_patched

def main():
    pg.setConfigOptions(antialias=True)  # Look at how much it change the performances
    # Change color of pyqtgraph's tabs
    DockLabel.updateStyle = update_style_patched

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window = MainWindow()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



