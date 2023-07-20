import fsecont
import json

# All contracts have Leasee name, aircraft type, aircraft tail number, lease length in months, and payment due date
# This data can be stored as JSON key pairs
# Can store the aircraft tail number as its serial number and its tail number to reduce FSE API calls, as we no longer have to convert its tail number to its serial
# Can store the leasee in two entries, their FSE username and their user ID
# Could also create a contract ID system for internal contract tracking and contract lookup
# Maybe also do contract lookup using AC tail number.
# Show AC location in staff channel?

# Contracts will be stored as individual JSON files, with one "meta" JSON file to which stores contracts as 

def createContract(leasee, actype, actail, length, due): # Creates a contract with 5 pieces of data
    ncontract = {
        "leasee": leasee,
        "actype": actype,
        "actail": actail,
        "length": length,
        "due": due
    }
    ncontractfname = "contracts/contract_" + str(findNewID()) + ".json"
    contractFile = open(ncontractfname, "w", "w")
    json.dump(ncontract, contractFile)
    return True

def viewContractID(id): # returns contract information based on ID
    cfname = "contract_" + str(id) + ".json"
    contract = open(cfname, "r", encoding="utf-8")
    contractJson = json.loads(contract)
    return contractJson["leasee"], contractJson["actype"], contractJson["actail"], contractJson["length"], contractJson["due"]

def deleteContract(id): # Removes contract using ID number
    return True

def editContract(leasee, actype, actail, length, due, cid): # Edits contract, takes all 5 pieces of data plus ID
    return True

def contractLookupID(id): # Looks up contract by ID number
    return True

def contractLookupUsername(uname): # Lists all contract IDs for a given username
    cids = [0,0,0]
    metaInfo = open("contracts/contracts-meta-username.json", "r", encoding="utf-8")
    metaJson = json.loads(metaInfo)
    cids = metaJson[uname]
    return cids

def updateMetaUname(name, ids): # Name var type string, IDs var type array of ints
    return True

def updateMetaID(name, id): # Name var type string, ID var type int
    return True

def findNewID(): # Finds a unique contract ID
    newID = 0
    meta = open("contracts/contracts-meta-ID.json", "r", encoding="utf-8")
    metaJson = json.loads(meta)
    newID = len(metaJson) + 1
    return newID