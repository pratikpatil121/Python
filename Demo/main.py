import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    # set the title of the window
        self.setWindowTitle("Main Window")
    # setGeometry(alignLeft, alignTop, width, height)
        self.setGeometry(500, 300, 500, 300)
    # create mainLayout with vertical box means all thw widgets added in
    #the mainLayout is in vertically
        self.mainLayout = QVBoxLayout(self)
    # here mainWindow Layout in the window
        self.setLayout(self.mainLayout)
    #function call in the MainWindow constructor for add the label in the
    #mainWindow layout
        self.LabelUI()
    # funtion for creating the label and set in the main Layout
    def LabelUI(self):  
    #Here create the label with parameter "ello Core2web"
        self.label = QLabel("Hello Core2Web")
    # set the label in the main layout window
        self.mainLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignCenter)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())