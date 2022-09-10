# hello.py

##handles application's termination and exit status
import sys

##all the packages for the gui and such
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

##created an instance of QApplication
app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt APP")

#first two arguments are the x and y screen coordinates where the window will be placed. The third and fourth arguments are the window’s width and height.
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window) 
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec())