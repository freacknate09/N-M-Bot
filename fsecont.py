import pandas as pd
import requests
import json
import time
import math

conf = open("config.json", "r", encoding="utf-8")
confJson = json.load(conf)
servicekey = confJson["FSEKey"]

def getUserID(username):
    api_url = "https://server.fseconomy.net/rest/api/v2/account/search/name"
    data = {"accountname": username}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "servicekey": servicekey
        }
    r = requests.post(api_url, data=data, headers=headers)
    return r.json()["data"]
def checkLeased(reg):
    urlcsv = "https://server.fseconomy.net/data?servicekey=" + servicekey + "&format=csv&query=aircraft&search=registration&aircraftreg=" + reg
    data = pd.read_csv(urlcsv)
    try:
        math.isnan(data.at[0, "LeasedFrom"])
    except:
        return True
    else:
        return False
def getACSerial(reg):
    urlcsv = "https://server.fseconomy.net/data?servicekey=" + servicekey + "&format=csv&query=aircraft&search=registration&aircraftreg=" + reg
    data = pd.read_csv(urlcsv)
    return data.at[0,"SerialNumber"]

def leaseACSerial(usrfrom, usrto, acserial):
    url_base = "https://server.fseconomy.net/rest/api/v2/aircraft/lease"
    from_id = getUserID(usrfrom)
    to_id = getUserID(usrto)
    data = {"note": "Automated N&M Leasing Action"}
    headers = {
        "servicekey": servicekey
    }
    api_url = url_base + "/" + str(from_id) + "/" + str(to_id) + "/" + str(acserial)
    r = requests.post(api_url, data=data, headers=headers)
    if r.json()["meta"]["error"] != "Bad Request":
        return True
    else:
        return False

def leaseACReg(usrfrom, usrto, acreg):
    url_base = "https://server.fseconomy.net/rest/api/v2/aircraft/lease"
    from_id = getUserID(usrfrom)
    to_id = getUserID(usrto)
    acserial = getACSerial(acreg)
    data = {"note": "N&M Aircraft Lease"}
    headers = {
        "servicekey": servicekey
    }
    api_url = url_base + "/" + str(from_id) + "/" + str(to_id) + "/" + str(acserial)
    r = requests.post(api_url, data=data, headers=headers)
    if r.json()["meta"]["error"] != "Bad Request":
        return True
    else:
        return False
    
def returnLease(usrfrom, acreg):
    url_base = "https://server.fseconomy.net/rest/api/v2/aircraft/returnlease"
    from_id = getUserID(usrfrom)
    acserial = getACSerial(acreg)
    data = {"note": "N&M Aircraft Lease Return"}
    headers = {
        "servicekey": servicekey
    }
    api_url = url_base + "/" + str(from_id) + "/" + str(acserial)
    r = requests.post(api_url, data=data, headers=headers)
    if r.json()["meta"]["error"] != "Bad Request":
        return True
    else:
        return False
