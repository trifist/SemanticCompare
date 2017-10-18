#include "stdafx.h"
#include "SpeechRecognizer.h"

int main()
{
    SpeechRecognizer* pSr = new SpeechRecognizer;
    pSr->init();
    pSr->startRecognise("ฤใบร");
}

