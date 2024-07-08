from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class mainwindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Button")
        self.setGeometry(100,100,600,400)
        self.makeWindow() # 위젯 생성

    def makeWindow(self):
        btn1 = QPushButton("Python",self) # QPushButton을 생성하면서 부모를 self로 설정
        btn2 = QPushButton("C++",self)

        btn1.setGeometry(300,200,100,30) # x, y, width, height
        btn2.setGeometry(100,200,100,30)
        # icon1 = QIcon('src/images/python.png') # 아이콘 불러오기
        # btn1.setIcon(icon) # 버튼에 아이콘 설정
        btn1.setIconSize(QSize(26,26)) # 아이콘 크기 설정
        btn1.clicked.connect(lambda:self.btnClicked(1)) # 버튼을 클릭하면 btnClick 함수 실행
        btn2.clicked.connect(lambda:self.btnClicked(2)) # lambda 안쓰면 인자를 넘길 수 없음

        self.label = QLabel("",self)
        self.label.setGeometry(170,100,200,30)
        self.label.setFont(QFont('Arial', 20, QFont.Weight.ExtraBold))

    def btnClicked(self,x): # 버튼 클릭 시 실행할 함수
        if(x==1):
            self.label.setText("I don't like Python")
            self.label.setStyleSheet("color: red")
        else:
            self.label.setText("I love C++")
            self.label.setStyleSheet("color: white")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())