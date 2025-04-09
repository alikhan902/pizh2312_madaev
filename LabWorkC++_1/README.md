Мадаев Алихан 
ПИЖ-б-о-23-1

Лабораторная работа 1. Утилита WordCount

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>


using namespace std;

struct Options {
    bool lines = false;
    bool words = false;
    bool bytes = false;
    bool chars = false;
};

void processFile(const string& filename, const Options& opts) {
    ifstream file(filename, ios::binary);
    if (!file) {
        cerr << "Ошибка открытия файла: " << filename << endl;
        return;
    }

    size_t lineCount = 0, wordCount = 0, byteCount = 0, charCount = 0;
    string line;
    while (getline(file, line)) {
        lineCount++;
        wordCount += count_if(line.begin(), line.end(), [](char c) { return isspace((unsigned char)c); }) + 1;
        charCount += line.size();
    }
    file.clear();
    file.seekg(0, ios::end);
    byteCount = file.tellg();

    // Если опций нет — выводим всё
    bool noOption = !opts.lines && !opts.words && !opts.bytes && !opts.chars;
    if (opts.lines || noOption) cout << lineCount << " ";
    if (opts.words || noOption) cout << wordCount << " ";
    if (opts.bytes || noOption) cout << byteCount << " ";
    if (opts.chars || noOption) cout << charCount << " ";
    cout << filename << endl;
}

int main(int argc, char* argv[]) {
    Options opts;
    vector<string> filenames;

    for (int i = 1; i < argc; ++i) {
        string arg = argv[i];
        if (arg[0] == '-') {
            if (arg == "--lines") opts.lines = true;
            else if (arg == "--words") opts.words = true;
            else if (arg == "--bytes") opts.bytes = true;
            else if (arg == "--chars") opts.chars = true;
            else {
                // краткая запись -lcw
                for (size_t j = 1; j < arg.size(); ++j) {
                    switch (arg[j]) {
                    case 'l': opts.lines = true; break;
                    case 'w': opts.words = true; break;
                    case 'c': opts.bytes = true; break;
                    case 'm': opts.chars = true; break;
                    }
                }
            }
        }
        else {
            filenames.push_back(arg);
        }
    }

    for (const auto& fname : filenames) {
        processFile(fname, opts);
    }

    return 0;
}
