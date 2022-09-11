import sys
#this module provides the exit() function

from PyQt6.QtWidgets import (
#imports necessary classes from PyQt6.QtWidgets
    QApplication, 
    QMainWindow, 
    QWidget
)

WINDOW_SIZE = 235
#creates a python constant to hold fixed window size in pixels

class CalcWindow(QMainWindow):
#Acts as Calculators main window(view) - inherits from Mainwindow class and provides GUI

    def __init__(self):
    #Defines the initializer
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        #Gives the window a fixed size and prevents user from resizing the window during execution
        centralWidget = QWidget(self)
        #creates QWIdget object and sets it as central Widget; acts as the parent of all required GUI components 
        self.setCentralWidget(centralWidget)

    def main():
    #defines calc's main funciton
        calcApp = QApplication([])
        calcWindow = CalcWindow()
        #creates an instance of app's window
        calcWindow.show()
        #shows the GUI by callin .show()
        sys.exit(calcApp.exec())
        #runs application's event loop with .exec()

    if __name__ == "__main__":
        main()