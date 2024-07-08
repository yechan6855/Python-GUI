from PyQt6.QtWidgets import QApplication, QWidget
import sys

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window frame")
        self.makeWindow() # 위젯 생성

    def makeWindow(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())