from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.makeWindow()

    def makeWindow(self):
        hBox = QHBoxLayout()
        vBox = QVBoxLayout()

        btn1 = QPushButton("+")
        btn2 = QPushButton("-")
        btn3 = QPushButton("*")
        btn4 = QPushButton("/")

        hBox.addWidget(btn1)
        hBox.addWidget(btn2)
        hBox.addWidget(btn3)
        hBox.addWidget(btn4)

        inputBox = QVBoxLayout()
        self.num1Input = QLineEdit(self)
        self.num1Input.setPlaceholderText("Number 1")
        self.num2Input = QLineEdit(self)
        self.num2Input.setPlaceholderText("Number 2")
        inputBox.addWidget(self.num1Input)
        inputBox.addWidget(self.num2Input)

        vBox.addLayout(inputBox)
        vBox.addLayout(hBox)

        self.resultLabel = QLabel("Result: ")
        vBox.setSpacing(20)
        vBox.addWidget(self.resultLabel)
        self.setLayout(vBox)

        btn1.clicked.connect(self.onButtonClicked)
        btn2.clicked.connect(self.onButtonClicked)
        btn3.clicked.connect(self.onButtonClicked)
        btn4.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        button = self.sender()
        op = button.text()
        
        num1 = self.num1Input.text()
        num2 = self.num2Input.text()

        if not num1 or not num2:
            self.resultLabel.setText("")
            return

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.resultLabel.setText("")
            return

        result = self.calculateTwoNumbers(num1, num2, op)
        self.resultLabel.setText(f"Result: {result}")

    def calculateTwoNumbers(self, num1, num2, op):
        result = 0
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())