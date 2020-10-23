from PySide2.QtWidgets import QPushButton, QApplication
import sys
from mainwindow import MainWindow

app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())