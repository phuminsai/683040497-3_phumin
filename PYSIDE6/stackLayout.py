import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QStackedLayout, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtCore import Qt

class WizardPages(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()

        # Add pages
        page1 = QWidget()
        page1.setLayout(QVBoxLayout())
        page1.layout().addWidget(QLabel("Page 1 Content"))

        page2 = QWidget()
        page2.setLayout(QVBoxLayout())
        page2.layout().addWidget(QLabel("Page 2 Content"))

        page3 = QWidget()
        page3.setLayout(QVBoxLayout())
        page3.layout().addWidget(QLabel("Is this a final page?"))

        # Add pages to stacked layout
        self.stacked_layout.addWidget(page1)
        self.stacked_layout.addWidget(page2)
        self.stacked_layout.addWidget(page3)

        # Navigation buttons
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_page)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.stacked_layout)
        main_layout.addWidget(next_button)

        self.setLayout(main_layout)

    def next_page(self):
        current = self.stacked_layout.currentIndex()
        self.stacked_layout.setCurrentIndex((current + 1) % self.stacked_layout.count())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wizard Pages Example")
        self.setCentralWidget(WizardPages())
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())