# coding: utf-8 
# created by wpcheng 
# Sept. 14th, 2017
from SemanticEntity import *

entities = []
correctEntities = []
errorEntities = []

def readActualResult():
    #read actual results
    actualResultFile = open("./ActualResults.txt", "r", encoding="utf8")
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
            elif(line == "Label_SpeechError:\n"):
                entities.append(entity)
        i=i+1
    return

def readExpectText():
    file = open("./ExpectText.txt", "r", encoding="utf8")
    results = file.readlines()
    file.close()
    if(len(entities) != len(results)):
        print("ExpectText Error, not match!")
        return
    for i in range(0, len(entities)):
        entities[i].expectText = results[i]
    return

def readExpectJson():
    file = open("./ExpectJson.txt", "r", encoding="utf8")
    results = file.readlines()
    file.close()
    if(len(entities) != len(results)):
        print("ExpectJson Error, not match!")
        return
    for i in range(0, len(entities)):
        entities[i].expectJson = results[i]
    return

def writeResults():
    file = open("./ErrorResults.txt", "w", encoding="utf8")
    for entity in errorEntities:
        file.write("Label_Start:-----------------------------------------------------------\n")
        file.write("Is Local: ")
        file.write(entity.isLocalResult)
        file.write("\n")
        file.write("Expect Text: ")
        file.write(entity.expectText)
        file.write("\n")
        file.write("Actual Text: ")
        file.write(entity.actualText)
        file.write("\n")
        file.write("Expect Semantic:\n")
        file.write(entity.expectJson)
        file.write("\n")
        file.write("Actual Semantic:\n")
        file.write(entity.actualJson)
        file.write("\n")
        file.write("Label_End--------------------------------------------------------------\n")
        file.write("\n\n\n")
    file.close()
    

def main():
    readActualResult()
    readExpectText()
    readExpectJson()

    for entity in entities:
        result = entity.compare()
        if(result[0] and result[1]):
            correctEntities.append(entity)
        else:
            errorEntities.append(entity)

    print("correct count = %s" % len(correctEntities))
    print("error count = %s" % len(errorEntities))

    writeResults()
    input("Done! press Enter to exit")

if __name__ == "__main__":
    main()