# 1) import components
from PySide6 import QtWidgets
import sys

# 3) create window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First QApp")
        self.setGeometry(100, 300, 300, 500)  # x, y, width, height

        # 4) add widgets and components
        # --------- Add widgets, layout, other stuff to the window -----------

        # --------------------------------------------------------------------

    # ---- methods to use with widgets and component in window ---

    # ------------------------------------------------------------

    # end of class

# 2) create application
class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # 3) Create the main window
        self.main_window = MainWindow()

        # 5) show the window
        self.main_window.show()

def main():

    # 2) Create the Qt Application
    app = Application(sys.argv)

    # 6) Start the event loop
    return app.exec()

if __name__ == "__main__":
    sys.exit(main()) # proper application cleanup and exit code handling