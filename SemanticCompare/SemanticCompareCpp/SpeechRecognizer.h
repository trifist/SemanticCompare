#pragma once
#pragma comment(lib, "./libs/libisssr.lib")
#pragma comment(lib, "./libs/libissauth.lib")
#include <string>
#include "iss_sr.h"
#include "iss_auth.h"

class SpeechRecognizer
{
private:
    std::string szResourceDir = "D:\\repository_git\\SemanticCompare\\SemanticCompare\\SemanticCompareCpp\\resource\\SRRes";
    std::string machineCode = "ThisIsAFakeMachineIdWhichNotLongerThan1024";
    HISSSR srHandle = NULL;

public:
    SpeechRecognizer();
    ~SpeechRecognizer();


    void init();
    void showInfo();
    void startRecognise(std::string text);
};

