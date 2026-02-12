'''
Created on 8. aug. 2020
@author: Bikash
'''
from flask import Flask
from flask import request,jsonify
import pythoncom
from win32com.client import Dispatch
import traceback
import datetime
import time
from app import app,db,session
from .CU_ReusableLibraries_RouteHandler import *
from .CU_ReusableLibraries_HomeScreen import *
from .commonLibraries import *
import logging
import os




@app.route("/Validate/validatePovaTasks/<string:bytype>", methods = ['POST'])
def Validate_TaskStat_In_Pova(bytype):
	app.logger.info("Logging for the Validate_TaskStat_In_Pova started, Variable initialization is starting...")
	print("-----------------------------------------------------------------------------------------------")
	print (request.is_json)
	content = request.get_json()
	print (content)
	ExceptionMessage=""
	starttime = datetime.datetime.now()
	result=""
	povacontent=""
	orderNum=""
	ExceptionScreenPath=""
	CU_User=""
	RequestStatus='Submitted'
	orderID=""
	requestID=gerenrateRequestID()
	session['scenario'] = "Validate_TaskStat_In_Pova"
	session['requestID']=requestID
	print("session id is "+session['requestID'])
	InputDataRequest=""
	app.logger.info("Variable initialization is finished for the request ID -"+requestID)

	try:
		if request.is_json:
			credentialdetails=getCredentials(request.authorization)
			result,povacontent,orderNum,ExceptionMessage,ExceptionScreenPath,CU_User,InputDataRequest=validatePovaTasks(credentialdetails,content['environment'],content['orderid'],content['Validation'],bytype)
			orderID=str(content['orderid'])
			RequestStatus="Success"
			

		else:
			ExceptionMessage="Message not in Json format / Content-Type not set as application/json"
			RequestStatus="Exception"
			
	except Exception as e:
		print("Exception occured")
		ExceptionMessage=str(e)
		RequestStatus="Exception"
	response="Debugger-ID:"+requestID+",ExceptionMessage:"+ExceptionMessage+",ExceptionScreenShotPath:"+ExceptionScreenPath+",Validationresult:"+str(result)+",Povacontent:"+str(povacontent)+",CUOrderNo:"+orderNum
	endtime = datetime.datetime.now()
	
	db.session.commit()
	session.pop('requestID', None)

	return jsonify({"Debugger-ID":requestID,"ExceptionMessage":ExceptionMessage,"ExceptionScreenShotPath":ExceptionScreenPath,"Validationresult":result,"TotalTime":str(endtime-starttime),"Povacontent":povacontent,"CUOrderNo":orderNum})

