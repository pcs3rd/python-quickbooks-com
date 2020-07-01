import json
from win32com.client as win32
qbxml_header = """



"""

qbxml_footer = """

;
"""
qb = client.Dispatch("QBPOSXMLRPLib.RequestProcessor")
qb = win32.client.Dispatch("QBXMLRPLib.RequestProcessor")
qb.OpenConnection("python-quickbooks-com", "REST api application for quickbooks.")
ticket = qb.BeginSession("",0)
def itemquantity(obj):
    qb.ProcessRequest(ticket, "%s<%sQueryRq>%s" % (qbxml_header, rq, rq, qbxml_footer)))
