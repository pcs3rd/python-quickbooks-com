# python-quickbooks-com  

 A custom importable python script (eventually library) that will hopefully make talking to old versions of Quickbooks easier with python. This will hopefully allow for a band-aid solution for integrating with newer, REST based integrations powered by open source code. This way, we don't have to deal with soap garbage, and eventually, we won't have to deal with xml at all - only JSON. hopefully, this doesn't just dissapear since the quickbooks accountant used by my workplace told us to upgrade :/
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
- [ ] Base: Parse a configuration file  
- [x] Haha, inventory machine go burrrrr
- [ ] code works too well; returns ENTIRE inventory and not just requested item. Make itemquery only return data for item requested. need to fix xml string. (https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbpos/iteminventoryquery)


