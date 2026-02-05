# 1) import components
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import sys

# 2) create application
# Every Qt application must have ONE QApplication instance
app = QApplication(sys.argv)  # sys.argv allows command line arguments

# 3) create window -- Usually use a class to create and work with windows though
# Create and show the main window
window = QMainWindow()

# 4) create a central widget and add components
## --------- Add widgets, layout, other stuff to the window -----------
central_widget = QWidget()
window.setCentralWidget(central_widget)
## --------------------------------------------------------------------


# 5) show the window
window.show()  # Windows are hidden by default

# 6) Start the event loop
app.exec()     # Program stays here until last window is closed