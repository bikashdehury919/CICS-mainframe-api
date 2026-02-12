
import time
from .IBMReflectionConfiguration import *

#Reflection Event details


def gotoScreen(ReflectionObject, strScreenname, Option):
    waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 15)
    setMousePosition(ReflectionObject, 23, 15)
    setTerminalMousePosition(ReflectionObject, 1, 23, 15)
    putText(ReflectionObject, strScreenname)
    if len(Option) != 0:
        putText(ReflectionObject, Option)
    sendKeys(ReflectionObject, EnterKey)
    waitForScreenEvent(ReflectionObject, KbdEnabled, LargeWait, "0", 23, 8)


def gotoScreen(ReflectionObject, strScreenname, Option):
    #waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 15)
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

def logoutFromColumbus(ReflectionObject):
    ReflectionObject.DisConnect()
    ReflectionObject.Quit()


def validateScreen(ReflectionObject, strScreenname):
    stringFound = find_Text(ReflectionObject, strScreenname, 1, 1)
    return bool(stringFound != 0)


def waitForScreenEvent(ReflectionObject, strEnvName, strMaxWaitTime, strDuration, intXCordinate, intYCordinate):
    ReflectionObject.WaitForEvent(strEnvName, strMaxWaitTime, strDuration, intXCordinate, intYCordinate)


def waitForDisplay_String(ReflectionObject, strInput, strDuration, intXCordinate, intYCordinate):
    ReflectionObject.WaitForDisplayString(strInput, strDuration, intXCordinate, intYCordinate)


def putText(ReflectionObject, strInput):
    ReflectionObject.TransmitANSI(strInput)


def sendKeys(ReflectionObject, inputKey):
    ReflectionObject.TransmitTerminalKey(inputKey)


def setMousePosition(ReflectionObject, intXCordinate, intYCordinate):
    ReflectionObject.SetMousePos(intXCordinate, intYCordinate)


def setTerminalMousePosition(ReflectionObject, action, intXCordinate, intYCordinate):
    ReflectionObject.TerminalMouse(action, intXCordinate, intYCordinate)


def getText(ReflectionObject, intXCordinate, intYCordinate, intLength):
    return ReflectionObject.GetDisplayText(intXCordinate, intYCordinate, intLength)


def find_Text(ReflectionObject, inputText, intXCordinate, intYCordinate):
    return ReflectionObject.FindText(inputText, intXCordinate, intYCordinate)




