from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MonitorGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()
        self.label = QLabel()
        start = QPushButton("Start")
        pause = QPushButton("Pause")
        quit = QPushButton("Quit")
        self.reading = QLCDNumber()

        layout.addWidget(self.label,0,0)
        layout.addWidget(self.reading,1,0)
        layout.addWidget(start,2,0)
        layout.addWidget(pause,2,1)
        layout.addWidget(quit,2,2)

        self.setLayout(layout)
        self.setWindowTitle("Rowdy Pi")
        self.resize(600,400)

        quit.clicked.connect(self.close)
        pause.clicked.connect(self.pause)

        start.clicked.connect(self.display)

    def display(self):
        # self.reading.setText = "xxx"
        self.label.setText("hola")
        self.reading.display(99.90)


    def pause(self):
        pass

app = QApplication(sys.argv)
mon = MonitorGUI()
mon.show()
app.exec_()