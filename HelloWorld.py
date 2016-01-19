from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys



class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.label = QLabel("Hello World!")
        lineEdit = QLineEdit()
        button = QPushButton("close")

        layout.addWidget(self.label)
        layout.addWidget(lineEdit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        lineEdit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()
