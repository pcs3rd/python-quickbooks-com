import python-quickbooks-com/com as pyqb
qb = pyqb.quickbooks_open()
pyqb.itemquantity(qb, itemnumber)
pyqb.quickbooks_close(qb)
