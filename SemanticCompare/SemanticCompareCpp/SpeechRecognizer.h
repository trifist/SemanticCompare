#pragma once
#pragma comment(lib, "./libs/libisssr.lib")
#include <string>
#include "iss_sr.h"

class SpeechRecognizer
{
private:
    std::string szResourceDir = "./resource/SRRes/";
    HISSSR * pHISSSRObj = NULL;

public:
    SpeechRecognizer();
    ~SpeechRecognizer();

    void init();
    void showInfo();
};

