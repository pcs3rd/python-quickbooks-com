import json
from win32com import client as win32
import struct
#start defining functions
qbxml_header = """



"""

qbxml_footer = """

;
"""
def quickbooks_connect():
    #I believe this is the correct statement for the above import.
    qb = win32.Dispatch("QBPOSXMLRPLib.RequestProcessor")
    #qb = win32.client.Dispatch("QBXMLRPLib.RequestProcessor")
    qb.OpenConnection("python-quickbooks-com", "REST api application for quickbooks.")
    ticket = qb.BeginSession("",0)
def itemquantity(obj):
    qb.ProcessRequest(ticket, "%s<%sQueryRq>%s" % (qbxml_header, obj, obj, qbxml_footer))







#this is where the magic happens.
#First, we need to determine if this is running with 64-bit python, because quickbooks is 32-bit.
if (( 8 * struct.calcsize("P")) == '64'):
    print("ERROR: Quickbooks POS is a 32-bit ONLY application. \n This will prevent this library from accessing Quickbooks POS \n Please run this in a 32 bit space.")
else:
    print("Starting Quickbooks_connect function")
    quickbooks_connect()
