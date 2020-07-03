# python-quickbooks-com  

 A custom importable python script (wannabe library) that will hopefully make talking to old versions of Quickbooks easier with python. This will hopefully allow for a band-aid solution for integrating with newer, REST based integrations powered by open source code. This way, we don't have to deal with soap garbage, and eventually, we won't have to deal with xml at all - only JSON
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
- [ ] Base: QBXML to JSON conversion
- [ ] Base: Flask api endpoint
- [x] Base: QBPOS communication
- [ ] API (return): itemquantity  
- [x] API (fetch): itemquantity(data)  
- [ ] API (return): itemcost
- [x] API (fetch): itemcost(data)  
- [ ] API (return): itemprice
- [x] API (fetch): itemprice(data)
