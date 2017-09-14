from SemanticEntity import *

entities = []

def main():
	#read actual results
	actualResultFile = open("./ActualResults.txt", "r")
	line = actualResultFile.readline()
	while(line != ""):
		if(line == "Label_SpeechStart:\n"):
			entity = SemanticEntity()
			line = actualResultFile.readline()
			if(not line.startwith("Label")):
				param = line.split("\t")
				entity.actualText = param[0]
				entity.actualJson = param[2]
				entity.isLocalResult = param[1]
			entities.append(entity)
		line = actualResultFile.readline()

	print(entities[0].rawText)
	print("\n")
	print(entities[0].actualJson)

if __name__ == "__main__":
	main()