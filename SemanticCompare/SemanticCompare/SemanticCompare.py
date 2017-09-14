#created by wpcheng 
#Sept. 14th, 2017
from SemanticEntity import *

entities = []

def main():
	#read actual results
	actualResultFile = open("./ActualResults.txt", "r")
	line = "a"
	while(line != ""):
		line = actualResultFile.readline()
		if(line == "Label_SpeechStart:\n"):
			entity = SemanticEntity()
			position = actualResultFile.tell()
			line = actualResultFile.readline()
			if(not line.startswith("Label")):
				param = line.split("\t")
				entity.actualText = param[0]
				entity.actualJson = param[2]
				entity.isLocalResult = param[1]
			else:
				actualResultFile.seek(position, 0)
			entities.append(entity)

	print(entities[0].actualText)
	print("\n")
	print(entities[0].actualJson)

if __name__ == "__main__":
	main()