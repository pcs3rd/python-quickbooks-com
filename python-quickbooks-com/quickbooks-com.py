import json
from win32com import client as win32
import struct
response = setresponse
#start defining functions
def quickbooks_connect():
    #I believe this is the correct statement for the above import.
    qb = win32.gencache.EnsureDispatch("QBPOSXMLRPLib.RequestProcessor")
    #qb = win32.client.Dispatch("QBXMLRPLib.RequestProcessor")
    qb.OpenConnection("python-quickbooks-com", "REST api application for quickbooks.")
    ticket = qb.BeginSession("")

#Request item quantity. This should return some data?
def itemquantity(data):
    xmlstream = """
    <?qbxml version=\"8.0\"?>
        <QBXML>
            <QBXMLMsgsRq onError=\"stopOnError\">
                <ItemInventoryQueryRq requestID=\"""" + data +"""\" />
            </QBXMLMsgsRq>
        </QBXML>\""""
    #debug print(xmlstream)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

#Request item cost wholesale. This should return some data?
def itemcost(data):
    xmlstream = """
    <?qbxml version=\"8.0\"?>
        <QBXML>
            <QBXMLMsgsRq onError=\"stopOnError\">
                <ItemInventoryQueryRq requestID=\"""" + data +"""\" />
            </QBXMLMsgsRq>
        </QBXML>\""""
    #debug print(xmlstream)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

def itemprice(data):
    xmlstream = """
    <?qbxml version=\"8.0\"?>
        <QBXML>
            <QBXMLMsgsRq onError=\"stopOnError\">
                <ItemInventoryQueryRq requestID=\"""" + data +"""\" />
            </QBXMLMsgsRq>
        </QBXML>\""""
    #debug print(xmlstream)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

#this is where the magic happens.
#First, we need to determine if this is running with 64-bit python, because quickbooks is 32-bit.
if (( 8 * struct.calcsize("P")) == '64'):
    print("ERROR: Quickbooks POS is a 32-bit ONLY application. \n This will prevent this library from accessing Quickbooks POS \n Please run this in a 32 bit address space.")
