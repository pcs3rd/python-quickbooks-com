import json
from win32com import client as win32
import struct

#start defining functions
def quickbooks_open():
    #I believe this is the correct statement for the above import.
    qb = win32.gencache.EnsureDispatch("QBPOSXMLRPLib.RequestProcessor")
    #qb = win32.client.Dispatch("QBXMLRPLib.RequestProcessor")
    qb.OpenConnection("python-quickbooks-com", "REST api application for quickbooks.")
    ticket = qb.BeginSession("")
    
    return qb

#Request item quantity. This should return some data?
def itemquery(qb, data, ticket=""):
    xmlstream = "<?qbposxml version=\"1.0\"?>\n<QBPOSXML>\n  <QBPOSXMLMsgsRq onError=\"stopOnError\">\n     <ItemInventoryQueryRq>" , str(data) , "</ItemInventoryQueryRq>\n  </QBPOSXMLMsgsRq>\n</QBPOSXML>"
    #debug print(xmlstream)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

def quickbooks_close(qb): #drop the session
    qb.EndSession()
    qb.CloseConnection()

#this is where the magic happens.
#First, we need to determine if this is running with 64-bit python, because quickbooks is 32-bit.
if (( 8 * struct.calcsize("P")) == '64'):
    print("ERROR: Quickbooks POS is a 32-bit ONLY application. \n This will prevent this library from accessing Quickbooks POS \n Please run this in a 32 bit address space.")
