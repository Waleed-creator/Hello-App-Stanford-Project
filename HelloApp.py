import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtGui import QIcon, QFontDatabase, QFont
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        # Set Title 
        self.setWindowTitle("Hello App")
        # Set icon
        self.setWindowIcon(QIcon(resource_path('.\\icon.ico')))
        # Set Window Size (width,Height)
        self.resize(500,350)

        layout = QVBoxLayout()
        self.setLayout(layout)


        # Set Input Field

        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello', clicked=self.SayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
    
    def SayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))



# App Main Runner
app = QApplication(sys.argv)

app.setStyleSheet('''
QWidget{
                  font-size: 25px;
    }
QPushButton{
                  font-size: 20px;
                  
        }
''')
window = Myapp()
window.show()
app.exec()
