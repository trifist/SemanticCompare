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
    cout << "Start initiation..." << endl;
    ISSErrID errId = ISSSRCreateEx(&srHandle, ISS_SR_ACOUS_LANG_VALUE_MANDARIN, szResourceDir.c_str(), &onMsgProc, NULL);
    cout << "create sr, error id = " << errId << endl;
}

void SpeechRecognizer::showInfo()
{
    cout << "szResourceDir = " << SpeechRecognizer::szResourceDir.c_str() << endl;
}

