import python-quickbooks-com/com as pyqb
qb = pyqb.quickbooks_open()
pyqb.itemquantity(qb, 43313)
pyqb.quickbooks_close(qb)
