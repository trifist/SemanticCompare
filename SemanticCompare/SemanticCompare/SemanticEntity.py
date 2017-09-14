#created by wpcheng 
#Sept. 14th, 2017
import json
import re

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
		
	def cutText(self):
		self.actualText.strip()
		self.expectText.strip()
		self.actualText = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "", self.actualText)
		self.expectText = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "", self.expectText)

	def compare(self):
		self.cutText()
		if(self.expectText == self.actualText):
			return True
		else:
			return False
		
		

