from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QStackedLayout, QVBoxLayout
import sys

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window frame")
        self.setGeometry(0,0,500,400)
        self.makeWindow() # 위젯 생성

    def makeWindow(self):
        self.layout = QStackedLayout()
        label1 = QLabel('Label 1')
        label2 = QLabel('Label 2')
        label3 = QLabel('Label 3')

        self.layout.addWidget(label1)
        self.layout.addWidget(label2)
        self.layout.addWidget(label3)

        self.labelIdx = 0
        self.layout.setCurrentIndex(self.labelIdx)

        vBox = QVBoxLayout()
        vBox.addLayout(self.layout)

        btn = QPushButton('Label Change')
        vBox.addWidget(btn)
        self.setLayout(vBox)
        btn.clicked.connect(self.ChangeWidget)

    def ChangeWidget(self):
        self.labelIdx = (self.labelIdx + 1) % 3
        self.layout.setCurrentIndex(self.labelIdx)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())