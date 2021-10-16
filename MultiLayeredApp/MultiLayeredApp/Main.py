

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtWidgets

from MainSetup import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # sadece uygulama açılırken yapılacak işlemler: (diğerleri için farklı klasörlerde işlemler yaparak aşağıya aktarıcaz)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # designer'da oluşturulmuş başlangıç uygulaması
        self.setGeometry(150, 50, 1175, 800) # uygulamanın başlangıç konumunu belirtir
        self.ui.Tab.setCurrentIndex(0) # Uygulama ilk açılışınca 0 indexli sayfayı açar (Home Page)


        # uygulama açıldıktan sonra yapmak istediğimiz işlemler:
        self.setMouseTracking(True)

    def declaration(self):
        sender = self.sender
        print(dir(sender))
        pass


def app():
    App = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(App.exec())

app()


