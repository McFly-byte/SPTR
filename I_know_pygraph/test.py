
import pyqtgraph as pg

y = [1,2,4,4,5]

# win = pg.GraphicsLayoutWidget(show=True, title="困惑度曲线")
# win.resize(1000, 600)
# Enable antialiasing for prettier plots
pg.setConfigOption('background', 'w')
pg.setConfigOptions(antialias=True)
# p = win.addPlot(title="困惑度曲线")
pg.plot(y, pen=(11,
23,
70
), name="curve")
pg.exec()