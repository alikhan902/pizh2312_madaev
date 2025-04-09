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

class Options {
public:
    bool lines = false;
    bool words = false;
    bool bytes = false;
    bool chars = false;

    void parseArgs(const string& arg) {
        if (arg == "--lines") lines = true;
        else if (arg == "--words") words = true;
        else if (arg == "--bytes") bytes = true;
        else if (arg == "--chars") chars = true;
        else {
            // краткая запись -lcw
            for (size_t j = 1; j < arg.size(); ++j) {
                switch (arg[j]) {
                case 'l': lines = true; break;
                case 'w': words = true; break;
                case 'c': bytes = true; break;
                case 'm': chars = true; break;
                }
            }
        }
    }
};

class FileProcessor {
public:
    static void processFile(const string& filename, const Options& opts) {
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
};

class WordCount {
public:
    void run(int argc, char* argv[]) {
        Options opts;
        vector<string> filenames;

        // Парсим аргументы
        for (int i = 1; i < argc; ++i) {
            string arg = argv[i];
            if (arg[0] == '-') {
                opts.parseArgs(arg);
            }
            else {
                filenames.push_back(arg);
            }
        }

        // Обрабатываем каждый файл
        for (const auto& fname : filenames) {
            FileProcessor::processFile(fname, opts);
        }
    }
};

int main(int argc, char* argv[]) {
    WordCount wc;
    wc.run(argc, argv);
    return 0;
}
