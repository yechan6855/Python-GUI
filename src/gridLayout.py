from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window frame")
        self.setGeometry(0,0,400,400)
        self.btnLabels = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+']
        ]
        self.makeWindow()

    def makeWindow(self):
        layout = QGridLayout()
        self.setLayout(layout)

        for i in range(4):
            for j in range(4):
                btn = QPushButton(self.btnLabels[i][j])
                layout.addWidget(btn,i,j)
                btn.clicked.connect(self.btnClicked)
    
    def btnClicked(self):
        btn = self.sender()
        print(btn.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())