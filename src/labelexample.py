import sys
from PyQt6.QtCore import Qt
# 자주 사용하는 wiget들
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap, QIcon, QMovie # 폰트, 이미지, 아이콘, 동영상

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window frame")
        self.setGeometry(200,100,500,300) # x, y, width, height
        self.makeWindow() # 위젯 생성

    def makeWindow(self):
        label = QLabel("My First Widget QLabel", self) # QLabel을 생성하면서 부모를 self로 설정

        label.move(50,50) # label을 (50,50) 위치로 이동

        font = QFont('Arial', 20, QFont.Weight.ExtraBold) # 폰트 설정
        label.setFont(font) # label에 폰트 설정
        label.setStyleSheet("color: green; background-color: yellow") # label의 글자색을 초록색, 배경색을 노란색으로 설정
        label.setText("Change Text") # label의 텍스트를 변경

        pixmap = QPixmap('src/images/python.png') # 이미지 불러오기
        label.setPixmap(pixmap) # label에 이미지 설정

        movie=QMovie('src/images/moving-cute-boxes-cat-tired.gif') # 동영상 불러오기
        label.setMovie(movie) # label에 동영상 설정
        movie.start() # 동영상 재생(필수)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())