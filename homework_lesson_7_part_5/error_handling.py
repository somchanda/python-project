from datetime import datetime

class scanException(Exception):
    def __init__(self, msg):
        self.args = msg

def scanFloat(msg):
    try:
        value = float(input("Please enter " + str(msg) + " : "))
        return value
    except:
        return None

def scanDate(msg):
    try:
        value = datetime.strptime(str(input("Please enter " + str(msg) + " : ")), "%Y-%m-%d")
        return value
    except:
        return None

def scanTextOnly(msg):
    try:
        value = str(input("Please enter " + str(msg) + " : "))
        if not value.replace(' ', '').isalpha():
            return None
        return value
    except:
        return None

RESP = {'RSLT_CD': '', 'RSLT_SMS': ''}
try:
    name = scanTextOnly("Name")
    if name is None:
        raise scanException(['001', 'Invalid Name!'])
    sex = scanTextOnly("Sex")
    if sex is None:
        raise scanException(['002', 'Invalid Sex'])
    dob = scanDate("Dob")
    if dob is None:
        raise scanException(['003', 'Invalid DoB'])
    salary = scanFloat('Salary')
    if salary is None:
        raise scanException(['004', 'Invalid salary'])
    RESP['RSLT_CD'] = '000'; RESP['RSLT_SMS'] = "Success"
except scanException as ex1:
    RESP['RSLT_CD'] = ex1.args[0]; RESP['RSLT_SMS'] = ex1.args[1]
except Exception as ex2:
    RESP['RSLT_CD'] = '999'; RESP['RSLT_SMS'] = 'Unknown Error'

print(RESP)
