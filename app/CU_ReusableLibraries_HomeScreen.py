'''
Created on 3. sep. 2020

@author: 
'''
import time
from .mainFrame_Utility import *
from .IBMReflectionConfiguration import *
from .commonLibraries import takeScreenshot
import traceback

def logintoColumbus(ReflectionObject, strUsername, strpassword):
    try:

        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 21, 32)
        waitForDisplay_String(ReflectionObject, ":", MediumWait, 21, 30)
        putText(ReflectionObject, strUsername)
        sendKeys(ReflectionObject, TabKey)
        time.sleep(1)
        print(strUsername)
        print(strpassword)
        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 32)
        waitForDisplay_String(ReflectionObject, ":", MediumWait, 23, 30)
        putText(ReflectionObject, strpassword)
        sendKeys(ReflectionObject, EnterKey)
        time.sleep(1)

        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 15)
        #ReflectionObject.waitForEvent(Objreflectionobject, EnterPos, MediumWait, 23, 15)
        #ReflectionObject.waitForEvent(objReflection, strMaxWaitTime, strEnvName, strDuration, intXCordinate, intYCordinate)
        waitForDisplay_String(ReflectionObject, ">", MediumWait, 23, 13)
        putText(ReflectionObject, "logoff")
        sendKeys(ReflectionObject, EnterKey)

        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 21, 32)
        waitForDisplay_String(ReflectionObject, ":", MediumWait, 21, 30)
        putText(ReflectionObject, strUsername)
        sendKeys(ReflectionObject, TabKey)
        time.sleep(1)

        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 32)
        waitForDisplay_String(ReflectionObject, ":", MediumWait, 23, 30)
        putText(ReflectionObject, strpassword)
        sendKeys(ReflectionObject, EnterKey)

    except Exception as e:
        
        raise Exception("Fails to logged in : With Error Code "+str(traceback.print_exc()))

def selectEnvironment(ReflectionObject, strEnvName):
    try:
        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 15)
        waitForDisplay_String(ReflectionObject, ">", MediumWait, 23, 13)
        setMousePosition(ReflectionObject, 18, 8)
        putText(ReflectionObject, strEnvName)
        setMousePosition(ReflectionObject, 18, 8)
        sendKeys(ReflectionObject, EnterKey)

    except:
        raise Exception("Not able to choose the environment from main menu: With Error Code "+str(traceback.print_exc()))


def gotoCUScreen(ReflectionObject):
    try:
        waitForScreenEvent(ReflectionObject, KbdEnabled, MediumWait, "1", 1, 1)
        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 1, 1)
        putText(ReflectionObject, "cu")
        sendKeys(ReflectionObject, EnterKey)
        waitForScreenEvent(ReflectionObject, KbdEnabled, MediumWait, "1", 1, 1)
        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 1, 1)
        sendKeys(ReflectionObject, EnterKey)
    except:
        raise Exception("Moving to CU screen failes: With Error Code "+str(traceback.print_exc()))


def performOBRUOpertaion(ReflectionObject):
    try:
        gotoScreen(ReflectionObject, "OBRU", "")
        waitForScreenEvent(ReflectionObject, EnterPos, MediumWait, "0", 23, 15)
        sendKeys(ReflectionObject, F3Key)
    except:
        raise Exception("OBRU Operation failed: With Error Code "+str(traceback.print_exc()))








