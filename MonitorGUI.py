from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MonitorGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        start = QPushButton("Start")
        pause = QPushButton("Pause")
        quit = QPushButton("Quit")

        self.label1 = QLabel("Bedroom")
        self.label2 = QLabel("Bathroom")
        self.label3 = QLabel("Garage")

        self.reading1 = QLCDNumber()
        self.reading2 = QLCDNumber()
        self.reading3 = QLCDNumber()

        layout.addWidget(self.label1,1,0)
        layout.addWidget(self.reading1,0,0)

        layout.addWidget(self.label2,1,1)
        layout.addWidget(self.reading2,0,1)

        layout.addWidget(self.label3,1,2)
        layout.addWidget(self.reading3,0,2)

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
        # self.label.setText("hola")
        self.reading1.display(99.90)
        self.reading2.display(24.3)
        self.reading3.display(17.2)


    def pause(self):
        pass

app = QApplication(sys.argv)
mon = MonitorGUI()
mon.show()
app.exec_()