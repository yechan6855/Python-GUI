from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
import sys

class mainwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edit")
        self.setGeometry(100,100,700,400)
        self.makeWindow()

    def makeWindow(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(50,100,200,50)
        self.lineEdit.textChanged.connect(self.textChanged)

        self.label = QLabel('',self)
        self.label.setGeometry(50,50,300,50)

    def textChanged(self,textValue):
        self.label.setText(textValue)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec())