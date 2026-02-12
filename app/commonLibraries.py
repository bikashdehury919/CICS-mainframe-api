import csv

from .mainFrame_Utility import *
from win32com.client import DispatchEx
from .IBMReflectionConfiguration import *
from datetime import date
import random
import string
from app import app,session
import time
import os



#def writetologger(levelname,message):
#    print("write to logger is called")
#    if levelname=="warning":
#        logging.warning(message)
#    elif levelname=="info":
#        logging.info(message)
#    print("write to logger is finished")

def getCredentials(authorization):
    if authorization is not None:
        return authorization.username,authorization.password
    else:
        raise Exception ("Authorization missing in the Auth section . Please enter Your CU username and Password in the Auth section")


def gerenrateRequestID():
    letters = string.ascii_letters
    result_str1 = ''.join(random.choice(letters) for i in range(4))
    result_str2 = ''.join(random.choice(letters) for i in range(6))
    result_str3 = ''.join(random.choice(letters) for i in range(6))
    curtime=str(int(round(time.time() * 1000)))
    RequestName="RequestID-"+str(curtime)+"-"+result_str1+"-"+result_str2+"-"+result_str3

    return RequestName


def getTotalPageNumber(ReflectionObject, intXCordinate, intYCordinate, intlength):
    return getText(ReflectionObject, intXCordinate, intYCordinate, intlength)

def gotoPova_withOrderId(ReflectionObject, intOrderID):
    gotoScreen(ReflectionObject, "POVA", "," + str(intOrderID))
    onr = getText(ReflectionObject, 8, 7, 9)
    if onr.strip() == "":
        raise Exception("Order Not found, Wrong Order in Input Request")
    else:
        return True

def gotoFord_withOrderId(ReflectionObject, intOrderID):
    gotoScreen(ReflectionObject, "FORD", "," + str(intOrderID))
    onr = getText(ReflectionObject, 10, 8, 9)
    if onr.strip() == "":
        raise Exception("Order Not found, Wrong Order in Input Request")
    else:
        return True

def gotoFord_withLid(ReflectionObject, lid):
    gotoScreen(ReflectionObject, "FORD", str(lid))
    lidno = getText(ReflectionObject, 11, 8, 11)
    if lidno.strip() == "":
        raise Exception("Order Not found, Wrong Order in Input Request")
    else:
        return True


def launchReflection():
    import pythoncom
    pythoncom.CoInitialize()
    objReflection = DispatchEx("ReflectionIBM.Session")
    objReflection.Visible = True
    objReflection.Hostname = "NVAS"
    objReflection.Connect()
    objReflection.WindowState = 2
    objReflection.NationalCharacterSet=16
    
    return objReflection


def gotoScreen(ReflectionObject, strScreenname, Option):
    
    setMousePosition(ReflectionObject, 23, 15)
    setTerminalMousePosition(ReflectionObject, 1, 23, 15)
    putText(ReflectionObject, strScreenname)
    if len(Option) != 0:
        putText(ReflectionObject, Option)
    sendKeys(ReflectionObject, EnterKey)
    waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)


def validateScreenAndEnterKeyValue(ReflectionObject, ScreenName, KeyCode):
    if (validateScreen(ReflectionObject, ScreenName)):
        waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)
        setMousePosition(ReflectionObject, 1, 1)
        setTerminalMousePosition(ReflectionObject, 1, -1, -1)
        setTerminalMousePosition(ReflectionObject, 1, -1, -1)
        setTerminalMousePosition(ReflectionObject, 1, -1, -1)
        sendKeys(ReflectionObject, KeyCode)
        waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)

def ValidateScreenAndEnterValueInSpecificField(ReflectionObject, ScreenName, FieldName, Value):
    if (validateScreen(ReflectionObject, ScreenName)):
        found = find_Text(ReflectionObject, FieldName, 1, 1)
        if (found != 0):
            tempRow = ReflectionObject.FoundTextRow
            tempColumn = ReflectionObject.FoundTextColumn
            setTerminalMousePosition(ReflectionObject, 1, tempRow, tempColumn + len(FieldName) + 1)
            putText(ReflectionObject, Value)
            waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)
        else:
            print("Field "+ FieldName + " not found")
            raise Exception("Field "+ FieldName + " not found! You may need to check your access type(Residential/Wholesale) or Check address")
            
    else:
        print("Screen not found")
        raise Exception("Screen  "+ ScreenName + " not found")


def ValidateScreenandChooseOption(ReflectionObject, ScreenName, strProductName):
    if (validateScreen(ReflectionObject, ScreenName)):
        productno = ""
        found = find_Text(ReflectionObject, strProductName, 1, 1)
        if (found != 0):
            temprow = ReflectionObject.FoundTextRow
            tempcolumn = ReflectionObject.FoundTextColumn
            productno = getText(ReflectionObject, temprow, tempcolumn-8, 2)
            waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 8)
            putText(ReflectionObject, productno)
            sendKeys(ReflectionObject, EnterKey)
            waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)
        else:
            print("product not found")
            raise Exception("product "+ strProductName + " not found! You may need to check your access type(Residential/Wholesale) or Check address")
    else:
        print("Screen not found")
        raise Exception("Screen  "+ ScreenName + " not found")


def ValidateScreenAndEnterValue(ReflectionObject, ScreenName, strProductName):
    if (validateScreen(ReflectionObject, ScreenName)):
        productno = ""
        found = find_Text(ReflectionObject, strProductName, 1, 1)
        if (found != 0):
            temprow = ReflectionObject.FoundTextRow
            tempcolumn = ReflectionObject.FoundTextColumn
            productno = getText(ReflectionObject, temprow, tempcolumn-4, 2)
            waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 8)
            putText(ReflectionObject, productno)
            sendKeys(ReflectionObject, EnterKey)
            waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)
        else:
            print("product not found")
            raise Exception("product "+ strProductName + " not found! You may need to check your access type(Residential/Wholesale) or Check address")
    else:
        print("Screen not found")
        raise Exception("Screen  "+ ScreenName + " not found")

def enterValueAccordingToOption(ReflectionObject, ScreenName, FieldName, Value):
    if (validateScreen(ReflectionObject, ScreenName)):
        found = find_Text(ReflectionObject, FieldName, 1, 1)
        if (found != 0):
            tempRow = ReflectionObject.FoundTextRow
            tempColumn = ReflectionObject.FoundTextColumn
            setTerminalMousePosition(ReflectionObject, 1, tempRow, tempColumn - 5)
            putText(ReflectionObject, Value)
            sendKeys(ReflectionObject, EnterKey)
            waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)
        else:
            print("product not found")
            raise Exception("FieldName "+ FieldName + " not found! You may need to check your access type(Residential/Wholesale) or Check address")
    else:
        print("Screen not found")
        raise Exception("Screen  "+ ScreenName + " not found")



def logoutFromColumbus(ReflectionObject):
    ReflectionObject.DisConnect()
    ReflectionObject.Quit()


def takeScreenshot(ReflectionObject,screenshotname):
    ReflectionObject.PrintToFile = True
    ReflectionObject.PrintFileName = screenshotname
    ReflectionObject.PrintFileExistsAction = rcOverwrite
    ReflectionObject.PrintScreen(rcPrintScreen, 1)




def ValidateScreenAndEnterCharInSpecificField(ReflectionObject, ScreenName, FieldName, Value):
    if (validateScreen(ReflectionObject, ScreenName)):
        found = find_Text(ReflectionObject, FieldName, 1, 1)
        if (found != 0):
            tempRow = ReflectionObject.FoundTextRow
            tempColumn = ReflectionObject.FoundTextColumn
            ReflectionObject.TerminalMouse(1, tempRow, tempColumn - 5)
            ReflectionObject.TransmitANSI(Value)
            ReflectionObject.WaitForEvent(KbdEnabled, "50", "0", 23, 8)
        else:
            print("Field not found")
            raise Exception("FieldName "+ FieldName + " not found! You may need to check your access type(Residential/Wholesale) or Check address")
    else:
        print("Screen not found")
        raise Exception("Screen  "+ ScreenName + " not found")

