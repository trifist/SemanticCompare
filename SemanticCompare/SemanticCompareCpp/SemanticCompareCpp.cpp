#include "stdafx.h"
#include "SpeechRecognizer.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

static vector<char*> texts;

void readText()
{
    ifstream ifs;
    ifs.open("./text.txt");
    if (!ifs.is_open())
    {
        cout << "open file error!" << endl;
        return;
    }

    char buffer[400];
    while (!ifs.eof())
    {
        ifs.getline(buffer, 400, '\n');
        texts.push_back(&buffer);
    }

    ifs.close();
}

void writeResult()
{
    vector<char*>::const_iterator iterator = texts.begin();
    for (; iterator != texts.end(); iterator++)
    {
        cout << *iterator << endl;
    }
}

int main()
{
    system("chcp 65001"); //设置字符集
    
    readText();
    writeResult();

    //SpeechRecognizer* pSr = new SpeechRecognizer;
    //pSr->init();
    //pSr->startRecognise("打电话给张三");
}

