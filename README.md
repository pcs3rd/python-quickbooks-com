# python-quickbooks-com  

 A custom importable python script (wannabe library) that will hopefully make talking to old versions of Quickbooks easier with python. This will hopefully allow for a band-aid solution for integrating with newer, REST based integrations powered by open source code.
# Compatibility note:  

 The 32-bit version of python3 must be installed because of how windows applications work.
# Dependencies  

python 3.x
  python libraries:
pywin32
json

# Setup  

regsvr32 "C:\Program Files\Common/ Files\Intuit\QBPOSSDkRuntime\QBPOSSMLRPLib.dll"\

# Working on / High priority features:  

Base: Making a flask api endpoint.
Base: Communicating with quickbooks POS 2008
api: itemquantity
api: itemcost
