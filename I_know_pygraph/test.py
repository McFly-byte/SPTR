import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication

app=QApplication([])

plot = pg.PlotItem()
plot.plot([1,4,3])

view = pg.GraphicsView()
view.setCentralWidget(plot)

view.show()
app.exec_()
