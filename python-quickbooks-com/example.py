import com as pyqb
qb = pyqb.open()
tk = pyqb.begin()
pyqb.itemquery(qb, tk, 43313)
pyqb.close(qb, tk)
