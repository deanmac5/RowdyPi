from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MonitorGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        reading = QLabel("Reading text will go here")
        start = QPushButton("Start")
        pause = QPushButton("Pause")
        quit = QPushButton("Quit")

        layout.addWidget(reading,0,0)
        layout.addWidget(start,2,0)
        layout.addWidget(pause,2,1)
        layout.addWidget(quit,2,2)

        self.setLayout(layout)
        self.setWindowTitle("Rowdy Pi")
        self.resize(600,400)

        start.clicked.connect()

app = QApplication(sys.argv)
mon = MonitorGUI()
mon.show()
app.exec_()