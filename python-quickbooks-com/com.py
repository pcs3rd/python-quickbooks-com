import json
from win32com import client as win32
import struct

########################################################
#Session managing functions                            #
########################################################

def open(): #Open a connection, instantate QBPOSXMLRPLib
    #I believe this is the correct statement for the above import.
    qb = win32.gencache.EnsureDispatch("QBPOSXMLRPLib.RequestProcessor")
    qb.OpenConnection("python-quickbooks-com", "REST api application for quickbooks.")
    return qb

def begin(qb): #Begin a session
        ticket = qb.BeginSession("")
        return ticket
    
def close(qb, ticket): #Drop the session. Just like the now broken microphone.
    qb.EndSession(ticket)
    qb.CloseConnection()
    #Do not return anything for the time being. It is not needed... At least I don't think... to include an exit code.

#########################################################
#  library functions                                    #
#########################################################

def xml(qb, ticket, data): #Lets user just feed xml into library to be sent and parsed. Any errors come back from QBPOS itself. This is so peeps can pass the xml strings for funcions that are not yet implemented.
    xmlstream = str(data)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

def itemquery(qb, ticket, data): #Request item information. This should return some data?
    xmlstream = "    <?qbposxml version=\"1.0\"?>\n    <QBPOSXML>\n       <QBPOSXMLMsgsRq onError=\"stopOnError\">\n          <ItemInventoryQueryRq>\n             <ItemNumberFilter> \n             <MatchNumericCriterion >Equal</MatchNumericCriterion>\n             <ItemNumber >" + str(data) + "</ItemNumber>\n              </ItemNumberFilter>\n          </ItemInventoryQueryRq>\n       </QBPOSXMLMsgsRq>\n    </QBPOSXML>"
    #debug print(xmlstream)
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

def inventory(qb, ticket): #prints entire inventory. May be good for making a backup of a QB database. Don't know. What I do know is that it's piped output makes a finicky .txt file. Kinda weird.
    xmlstream = "<?qbposxml version=\"1.0\"?>\n<QBPOSXML>\n  <QBPOSXMLMsgsRq onError=\"stopOnError\">\n     <ItemInventoryQueryRq></ItemInventoryQueryRq>\n  </QBPOSXMLMsgsRq>\n</QBPOSXML>"
    response = qb.ProcessRequest(ticket, xmlstream)
    return response

#this is where the magic happens.
if (( 8 * struct.calcsize("P")) == '64'): #check for a 32 bit address space, because the quickbooks I'm developing on is 32-bit only. The more I work on this, the more I am reminded that this is OLD software.
    print("ERROR: Quickbooks POS is a 32-bit ONLY application. \n This will prevent this library from accessing Quickbooks POS \n Please run this in a 32 bit address space.")
