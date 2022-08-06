"""
Display a plot and an image with minimal setup. 

pg.plot() and pg.image() are indended to be used from an interactive prompt
to allow easy data inspection (but note that PySide unfortunately does not
call the Qt event loop while the interactive prompt is running, in this case
it is necessary to call QApplication.exec_() to make the windows appear).
"""

# 知识点 https://www.freesion.com/article/8072325707/

import numpy as np

import pyqtgraph as pg

# data 是一维数组，plot画曲线
data = np.random.normal(size=20)
print( data)
pg.plot(data, title="Simplest possible plotting example")

# 二维位图
data = np.random.normal(size=(50,50))
pg.image(data, title="Simplest possible image example")

if __name__ == '__main__':
    pg.exec()
