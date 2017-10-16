#pragma once
#pragma comment(lib, "./libs/libisssr.lib")
#include <string>
#include "iss_sr.h"

class SpeechRecognizer
{
private:
    std::string szResourceDir = "D:\\repository_git\\SemanticCompare\\SemanticCompare\\SemanticCompareCpp\\resource\\SRRes";
    HISSSR srHandle = NULL;

public:
    SpeechRecognizer();
    ~SpeechRecognizer();

    void init();
    void showInfo();
};

