#include "stdafx.h"
#include "SpeechRecognizer.h"
#include <iostream>
using namespace std;

void onMsgProc(const void * pUsrArg, unsigned int uMsg, unsigned int wParam, const void* lParam)
{
    cout << "pUsrArg = " << pUsrArg << ", uMsg = " << uMsg << ", wParam = " << wParam << ", lParam = " << lParam << endl;
}

SpeechRecognizer::SpeechRecognizer()
{
}


SpeechRecognizer::~SpeechRecognizer()
{
}


void SpeechRecognizer::init()
{
    ISSErrID errId;

    cout << "Start initiation..." << endl;

    errId = ISSSetMachineCode(machineCode.c_str());
    cout << "ISSSetMachineCode, error id = " << errId << endl;

    errId = ISSSRCreateEx(&srHandle, ISS_SR_ACOUS_LANG_VALUE_MANDARIN, szResourceDir.c_str(), &onMsgProc, NULL);
    cout << "ISSSRCreateEx, error id = " << errId << endl;

    errId = ISSSRStart(srHandle, ISS_SR_SCENE_ALL, ISS_SR_MODE_LOCAL_REC, NULL);
    cout << "ISSSRStart, error id = " << errId << endl;

    cout << "Initiation finish" << endl;
}

void SpeechRecognizer::showInfo()
{
    cout << "szResourceDir = " << SpeechRecognizer::szResourceDir.c_str() << endl;
}

void SpeechRecognizer::startRecognise(std::string text)
{
    int errId = 0;
    const char * result = NULL;
    cout << "startRecognise..." << endl;
    result = ISSSRMspSearch(srHandle, text.c_str(), NULL, &errId);
    cout << "ISSSRMspSearch, errId = " << errId << endl;
    cout << "result = " << result << endl;
}

