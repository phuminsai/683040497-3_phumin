import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,QLabel,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
            }
        """)
        
        main_layout = QVBoxLayout()
        
        title_layout = QHBoxLayout()
        title = QLabel("Calculator")
        title.setFont(QFont('Segoe UI', 20, QFont.Bold))
        title.setStyleSheet("color: white;")
        title_layout.addWidget(title)
        title_layout.addStretch()
        main_layout.addLayout(title_layout)
        
        
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setFont(QFont('Segoe UI', 48, QFont.Bold))
        self.display.setMinimumHeight(100)
        main_layout.addWidget(self.display)
        

        layout = QGridLayout()
        
        layout.addWidget(QPushButton("%"), 0, 0)
        layout.addWidget(QPushButton("CE"), 0, 1)
        layout.addWidget(QPushButton("C"), 0, 2)
        layout.addWidget(QPushButton("⌫"), 0, 3)
        
        layout.addWidget(QPushButton("1/x"), 1, 0)
        layout.addWidget(QPushButton("x²"), 1, 1)
        layout.addWidget(QPushButton("²√x"), 1, 2)
        layout.addWidget(QPushButton("÷"), 1, 3)
        
        layout.addWidget(QPushButton("7"), 2, 0)
        layout.addWidget(QPushButton("8"), 2, 1)
        layout.addWidget(QPushButton("9"), 2, 2)
        layout.addWidget(QPushButton("×"), 2, 3)
        
        layout.addWidget(QPushButton("4"), 3, 0)
        layout.addWidget(QPushButton("5"), 3, 1)
        layout.addWidget(QPushButton("6"), 3, 2)
        layout.addWidget(QPushButton("-"), 3, 3)
        
        layout.addWidget(QPushButton("1"), 4, 0)
        layout.addWidget(QPushButton("2"), 4, 1)
        layout.addWidget(QPushButton("3"), 4, 2)
        layout.addWidget(QPushButton("+"), 4, 3)
        
        layout.addWidget(QPushButton("+/-"), 5, 0)
        layout.addWidget(QPushButton("0"), 5, 1)
        layout.addWidget(QPushButton("."), 5, 2)
        
    
        equal_btn = QPushButton("=")
        equal_btn.setStyleSheet("""
                    QPushButton:pressed {
                        background-color: #2a2a2a;
                    }
                """)
        layout.addWidget(equal_btn, 5, 3)
        
   
        for i in range(layout.count() - 1):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setMinimumSize(80, 60)
                widget.setFont(QFont('Segoe UI', 14))
                widget.setStyleSheet("""
                    QPushButton:pressed {
                        background-color: #2a2a2a;
                    }
                """)
        
        equal_btn.setMinimumSize(80, 60)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 10, 10, 10)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setCentralWidget(CalculatorLayout())
        self.resize(400, 650)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())