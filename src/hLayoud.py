from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QHBoxLayout, QPushButton, QVBoxLayout
import sys

class mainwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,700,500)
        self.makeWindow()

    def makeWindow(self):
        vBox = QVBoxLayout()
        self.setLayout(vBox)

        hBox = QHBoxLayout()
        label = QLabel('Name: ')
        lineEdit = QLineEdit()
        btn = QPushButton('OK')
        hBox.addWidget(label)
        hBox.addWidget(lineEdit)
        hBox.addWidget(btn)
        vBox.addLayout(hBox)

        hBox = QHBoxLayout()
        label = QLabel('Password: ')
        lineEdit = QLineEdit()
        btn = QPushButton('Cancel')
        hBox.addWidget(label)
        hBox.addWidget(lineEdit)
        hBox.addWidget(btn)
        vBox.addLayout(hBox)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())