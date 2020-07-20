import qbcom as pyqb
import xmltodict
import json
print("open connection")
qb = pyqb.open()
tk = pyqb.begin(qb)
print("Fetch info for item 43313 in json format\n\n")
dictobject = xmltodict.parse(pyqb.itemquery(qb, tk, 43313), dict_constructor=dict, encoding='utf-8')
jsonobject = json.dumps(dictobject)
print(jsonobject)
print("Fetch info for item 43313 in xml format\n\n")
print(pyqb.itemquery(qb, tk, 43313))
pyqb.close(qb, tk)
print("Close session.")
print("Testing")
print(pyqb.inventory(qb, tk))
