from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QSystemTrayIcon
import threading
import sys
from refresher import Refresher
import os


class window(QMainWindow):

    def __init__(self, app: QApplication):

        QMainWindow.__init__(self)

        icon = QIcon(self.resource_path('assets/SPLREFRESHER.ICO'))
        pic = QPixmap(self.resource_path('assets/image.jpg'))
        picScaled = pic.scaled(QSize(312, 195))
        label = QLabel()
        label.setPixmap(picScaled)
        tray = QSystemTrayIcon(icon, parent=app)
        trayMenu = QMenu()
        trayExitAction = trayMenu.addAction("Salir")
        trayMenu.addAction(trayExitAction)

        self.setWindowIcon(icon)
        self.setFixedSize(QSize(312, 195))
        self.setGeometry(200, 200, 312, 195)
        self.setWindowTitle('SPL Refresher 1.1')
        self.setCentralWidget(label)

        tray.setToolTip('SPL Refresher')
        tray.show()
        tray.setContextMenu(trayMenu)
        tray.activated.connect(self.dobleClick)
        trayExitAction.triggered.connect(sys.exit)

        app.aboutToQuit.connect(self.closeEvent)

        threading.Thread(target=Refresher.main, daemon=True).start()

    def dobleClick(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isVisible() == True:
                self.hide()
            else:
                self.show()

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

def main():
    app = QApplication(sys.argv)
    win = window(app)
    win.show()
    sys.exit(app.exec_())
        

if __name__ == "__main__":
    main()