from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Sensor import Sensor
import sys

class MonitorGUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        buttonLayout = QHBoxLayout()
        start = QPushButton("Start")
        pause = QPushButton("Pause")
        quit = QPushButton("Quit")

        buttonLayout.addWidget(start)
        buttonLayout.addWidget(pause)
        buttonLayout.addWidget(quit)

        bathSensor = Sensor("Bathroom",9)
        bedroomSensor = Sensor("Bedroom 1",10)
        garageSensor = Sensor("Garage",11)
        kitchenSensor = Sensor("Kitchen",12)
        loungeSensor = Sensor("Lounge",13)
        bedroom2Sensor = Sensor("Bedroom 2",11)
        sensors = [bathSensor,bedroomSensor,garageSensor, kitchenSensor,loungeSensor, bedroom2Sensor ]



        for i in sensors:

            templayout = self.create_sensor_view(i)
            layout.addLayout(templayout,sensors.index(i))


        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        self.setWindowTitle("Rowdy Pi")
        self.resize(600,400)
        start.setFocus()

        quit.clicked.connect(self.close)
        pause.clicked.connect(self.pause)

        # start.clicked.connect(self.display)



    def create_sensor_view(self,sensor):
        self.locationLabel = QLabel(sensor.location + "\nPin:" + str(sensor.pin))

        self.reading = QLCDNumber()
        self.reading.display(55.3)
        heatButton = QPushButton("Turn On")

        self.sensor_grid = QHBoxLayout()
        self.sensor_grid.addWidget(self.locationLabel)

        self.sensor_grid.addWidget(self.reading)
        self.sensor_grid.addWidget(heatButton)

        return self.sensor_grid



    def pause(self):
        pass

app = QApplication(sys.argv)
mon = MonitorGUI()
mon.show()
app.exec_()