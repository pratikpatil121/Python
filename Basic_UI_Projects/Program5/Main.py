
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtGui import QColor
class ColorChangerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
# Create a QVBoxLayout
        layout = QVBoxLayout()
# Create a QComboBox and add colors to it
        color_combo = QComboBox(self)
        colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
        color_combo.addItems(colors)
        # Connect the color change signal to the slot
        color_combo.currentIndexChanged.connect(self.change_color)
        # Add the QComboBox to the layout
        layout.addWidget(color_combo)
        # Set the layout for the main window
        self.setLayout(layout)
        # Set the initial background color explicitly
        self.change_color(0)
        # Set the window properties
        self.setGeometry(500, 300, 500, 400)
        self.setWindowTitle('Color Changer App')

    def change_color(self, index):
# Get the selected color from the QComboBox
        color_name = self.sender().currentText() if self.sender() else "Red"
# Get the QColor object based on the color name
        color = QColor(color_name)
# Set the background color of the window
        self.setStyleSheet(f"background-color: {color.name()};")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorChangerApp()
    ex.show()
    sys.exit(app.exec_())