import sys
#this module provides the exit() function

from functools import partial
#Use this function to connect signals with methods that need to take extra arugments
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
#imports necessary classes from PyQt6.QtWidgets
    QApplication, 
    QMainWindow, 
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERROR"
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
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        #creates QWIdget object and sets it as central Widget; acts as the parent of all required GUI components 
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        #Use a QLineEdit widget
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        #Set a fixed height of 35 pixels using display_height
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        #left-aligned
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        #Adds the display to the general layout of the calculator

    def _createButtons(self):
        self.buttonMap = {}
        #First we create an empty dictionary to hold the calculator buttons
        buttonsLayout = QGridLayout()
        keyBoard =  [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]
        #create a list of lists to store the key labels
        for row, keys in enumerate(keyBoard):
        # goes through each row
            for col, key in enumerate(keys):
                #goes through each key and is assigned a column number
                self.buttonMap[key] = QPushButton(key)
                #create a button and add them to buttonMap
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

            self.generalLayout.addLayout(buttonsLayout)
            #embeds grid layout into calculator general layout
    
    def setDisplayText(self, text):
    #set the display's text
        self.display.setText(text)
        self.display.setFocus()
        #setFocus sets the cursor focus on the display

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText("")

def evaluateExpression(expression):
#(Model)
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class Calc:
    def __init__(self, model, view):
    #define the class initializer which takes two arguments
        self._evaluate = model
        self._view = view
        #store these arguments into instance attributes
        self._connectSignalsAndSlots()
        #makes all the required connections of signals and slots

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        #use ._evaluate to solve the math expression that the user typed in the display
        self._view.setDisplayText(result)
        #updates the display text with the result
    
    def _buildExpression(self, subExpression):
    #builds the target math expression
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)
        #concatenates the initial display value with every new value that the user enters on the keyboard

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def main():
#defines calc's main funciton
    calcApp = QApplication([])
    calcWindow = CalcWindow()
    #creates an instance of app's window
    calcWindow.show()
    #shows the GUI by callin .show()
    Calc(model=evaluateExpression, view=calcWindow)
    #Model arguments holds reference to evaluateExpression Function, while view argument holds reference to calcWindow Object - provides GUI
    sys.exit(calcApp.exec())
    #runs application's event loop with .exec()

if __name__ == "__main__":
        main()