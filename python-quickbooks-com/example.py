import com as pyqb
qb = pyqb.quickbooks_open()
pyqb.itemquery(qb, 43313)
pyqb.quickbooks_close(qb)
