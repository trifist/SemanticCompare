#created by wpcheng 
#Sept. 14th, 2017
import json

class SemanticEntity(object):
	actualText = ""
	actualJson = ""
	isLocalResult = -1
	expectText = ""
	expectJson = ""
	
	def __init__(self, actualText="", actualJson="", isLocalResult=-1):
		self.actualText = actualText
		self.actualJson = actualJson
		self.isLocalResult = isLocalResult
		return

	def compare(expect, actual):
		print(expect.keys())
		print('\n')
		print(actual.keys())
		return
		
		

