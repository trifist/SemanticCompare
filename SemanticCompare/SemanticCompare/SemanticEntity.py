#created by wpcheng
#Sept.  14th, 2017
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

    def compare(self):
        if(self.compareText() and self.compareSemantic()):
            return True
        else:
            return False

    def compareText(self):
        self.actualText.strip()
        self.expectText.strip()
        self.actualText = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "", self.actualText)
        self.expectText = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+", "", self.expectText)
        if(self.expectText == self.actualText):
            return True
        else:
            return False

    def compareSemantic(self):
        expect = json.loads(self.expectJson)
        rawActual = json.loads(self.actualJson)
        actual = {}
        for key in expect.keys():
            if(key in rawActual):
                actual[key] = rawActual[key]
            else:
                return False
        return actual == expect
