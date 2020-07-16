# python-quickbooks-com  

 A custom importable python script (eventually library) that will hopefully make talking to old versions of Quickbooks easier with python. This will hopefully allow for a band-aid solution for integrating with newer, REST based integrations powered by open source code. This way, we don't have to deal with soap garbage. Hopefully, this doesn't just dissapear since the quickbooks accountant used by my workplace told us to upgrade :/
# Compatibility note:  
 The 32-bit version of python3 must be installed because of how windows applications work.
# Dependencies  
  
### Windows dependancies:  
`python 3.x (32 bit)`  
`pip`  
### python libraries:  
`pywin32`  

# Setup  

regsvr32 "C:\Program Files\Common/ Files\Intuit\QBPOSSDkRuntime\QBPOSSMLRPLib.dll"\  
EDIT: This may not be needed^  
  
# Usage  
  
Importing: Not sure, haven't used this as a installed library, but import com.py (from the .py file) with:  
```import com as pyqb```  
  
Create a connection object  
```qb = pyqb.open()```  
  
Create a ticket object. The variable `qb` has to be passed to the begin() function. `qb` has to be created first for eveything to be happy. This will also use the active company file on the first available server, the network I am developing on has a single qbpos server.  
```tk = pyqb.begin(qb)```  

Request item information by item number. This needs the `qb` and `tk` variables passed to it in this exact order:  
```pyqb.itemquery(qb, tk, <ItemNumber>)```  
  
Print the inventory. The original function name was proposed to be `NowThatsALotOfData`. Long story short, if this is put in a print() statement and the output pipped, it may create a huge file with potentially weird encoding. This only needs the `qb, tk` variables passed.  
```pyqb.inventory(qb, tk)```  
  
Close the session. This also needs `qb, tk`.  
```pyqb.close(qb, tk)```  
  
  
# Working on / High priority features:  
- [x] Base: Grab item data using item number.
- [x] Haha, inventory machine go burrrrr (inventory() function)  
- [ ] Implament some more functions.
