#created by wpcheng 
#Sept. 14th, 2017
from SemanticEntity import *

entities = []

def main():
	#read actual results
	actualResultFile = open("./ActualResults.txt", "r")
	actualResult = actualResultFile.readlines()
	actualResultFile.close()

	i = 0;
	while(i < len(actualResult)):
		if(actualResult[i] == "Label_SpeechStart:\n"):
			entity = SemanticEntity()

			if(i+1<len(actualResult)):
				line = actualResult[i+1]
			else:
				break

			if(not line.startswith("Label")):
				param = line.split("\t")
				entity.actualText = param[0]
				entity.actualJson = param[2]
				entity.isLocalResult = param[1]

			entities.append(entity)
		i=i+1

	print(entities[0].actualText)
	print(entities[0].actualJson)
	print(len(entities))

if __name__ == "__main__":
	main()