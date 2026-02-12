from pandas import ExcelWriter

from .CU_ReusableLibraries_HomeScreen import *
from .mainFrame_Utility import *
from .IBMReflectionConfiguration import *

import datetime
import traceback
import pandas as pd
import json
from datetime import timedelta


def validatePovaTasks(lstCred, strenv, intOrderID, dictTask_Stat_Mapping, validationByType):
    app.logger.info(str(session['requestID']) + " : " + "pova task klarm validation scenario started")
    resultDict = {}
    pova_Screen = []
    ExceptionMessage = ""
    OrderNumber = ""
    ExceptionScreenPath = ""
    try:
        ReflectionObject = launchReflection()
        app.logger.info(str(session['requestID']) + " : " + "Reflection Launched")
        logintoColumbus(ReflectionObject, lstCred[0], lstCred[1])
        app.logger.info(str(session['requestID']) + " : " + "Login to CU completed successfully")
        selectEnvironment(ReflectionObject, strenv)
        app.logger.info(str(session['requestID']) + " : " + "Environment chosen")
        gotoCUScreen(ReflectionObject)
        performOBRUOpertaion(ReflectionObject)
        gotoPova_withOrderId(ReflectionObject, str(intOrderID))
        app.logger.info(str(session['requestID']) + " : " + "POVA screen operation started")
        tempTaskList = list(dictTask_Stat_Mapping.keys())
        inputTaskList = [x.lower() for x in tempTaskList]
        taskPresentList, taskNotPresentList, pova_Screen, OrderNumber = klarmVlidation_By_taskName(ReflectionObject,
                                                                                                   inputTaskList,
                                                                                                   validationByType)

        app.logger.info(str(session['requestID']) + " : " + "POVA screen operation completed")
        taskPresentFinalList = []
        inputTaskDict = dictTask_Stat_Mapping
        for key in inputTaskDict:
            for dict in taskPresentList:
                if key.lower() in dict:
                    tempList = []
                    tempDict = {}
                    if len(inputTaskDict[key]) != 0:
                        if inputTaskDict[key][0].lower() == dict[key.lower()][0].lower():
                            tempList.append('True')
                        elif inputTaskDict[key][0].lower() != "":
                            tempList.append('False')
                        if inputTaskDict[key][1].lower() == dict[key.lower()][1].lower():
                            tempList.append('True')
                        elif inputTaskDict[key][1].lower() != "":
                            tempList.append('False')

                    tempDict[key] = tempList
                    taskPresentFinalList.append(tempDict)
        resultDict = {'Task Present': taskPresentFinalList, 'Task Not Present': taskNotPresentList}
        logoutFromColumbus(ReflectionObject)
        app.logger.info(
            str(session['requestID']) + " : " + "pova task klarm validation scenario completed successfully")

    except Exception as e:
        print(str(e))
        ExceptionScreenPath = printException(ReflectionObject, str(e), str(traceback.print_exc()),
                                             sys._getframe(1).f_code.co_name, str(inspect.stack()))
        ExceptionMessage = "Fails in  RouteHandler library " + str(e) + ": With Error Code " + str(
            traceback.print_exc())
        logoutFromColumbus(ReflectionObject)

    return resultDict, pova_Screen, OrderNumber, ExceptionMessage, ExceptionScreenPath, lstCred[
        0], dictTask_Stat_Mapping

