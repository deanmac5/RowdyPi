import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

buttons = {}

for i in range(10):
    for j in range(10):
        # keep a reference to the buttons
        buttons[(i, j)] = QtGui.QPushButton('row %d, col %d' % (i, j))
        # add to the layout
        layout.addWidget(buttons[(i, j)], i, j)

widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())