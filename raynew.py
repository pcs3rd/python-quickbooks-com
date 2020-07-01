import win32com.client

query_rqs = (
  'Host',
  'Company',
  'Account',
  'Entity',
  'Terms',
  'Class',
  'CustomerType',
  'VendorType',
  'JobType',
  'PaymentMethod',
  'ShipMethod',
  'SalesTaxCode',
  'Item',
  )

qbxml_header = """



"""

qbxml_footer = """

;
"""

qb = win32com.client.Dispatch("QBXMLRP.RequestProcessor")
qb.OpenConnection("Data Sucker", "Data Sucker")
ticket = qb.BeginSession("",0)

for rq in query_rqs:
    print "Exporting " + rq + "(s)"
    output_file = open("c:\\qb-export-data\\" + rq + ".xml", 'w')
    output_file.write(qb.ProcessRequest(ticket, qbxml_header + "<" + rq + "QueryRq>" + qbxml_footer))
    output_file.close()
print "Data Export Completed"

qb.EndSession(ticket)
qb.CloseConnection()
qb = None #drop our QB object