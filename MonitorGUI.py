from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Sensor import Sensor
import sys

class MonitorGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        start = QPushButton("Start")
        pause = QPushButton("Pause")
        quit = QPushButton("Quit")

        self.reading1 = QLCDNumber()
        self.reading2 = QLCDNumber()
        self.reading3 = QLCDNumber()

        layout.addWidget(start,2,0)
        layout.addWidget(pause,2,1)
        layout.addWidget(quit,2,2)

        bathSensor = Sensor("Bathroom",9)
        bedroomSensor = Sensor("Bedroom",10)
        garageSensor = Sensor("Garage",11)

        sensors = [bathSensor,bedroomSensor,garageSensor]
        count = 0
        for i in sensors:

            templayout = self.create_sensor_view(i)
            layout.addLayout(templayout,0,count)
            count += 1


        self.setLayout(layout)
        self.setWindowTitle("Rowdy Pi")
        self.resize(600,400)

        quit.clicked.connect(self.close)
        pause.clicked.connect(self.pause)

        start.clicked.connect(self.display)

    def display(self):

        self.reading1.display(99.90)
        self.reading2.display(24.3)
        self.reading3.display(17.2)

    def create_sensor_view(self,sensor):
        self.locationLabel = QLabel(sensor.location + "     Pin: " + str(sensor.pin))
        self.templabel = QLabel("Temp:")
        self.reading = QLCDNumber()
        self.reading.display(55.3)

        self.sensor_grid = QGridLayout()
        self.sensor_grid.addWidget(self.locationLabel,0,0)
        self.sensor_grid.addWidget(self.templabel,1,0)
        self.sensor_grid.addWidget(self.reading,1,1)

        return self.sensor_grid



    def pause(self):
        pass

app = QApplication(sys.argv)
mon = MonitorGUI()
mon.show()
app.exec_()