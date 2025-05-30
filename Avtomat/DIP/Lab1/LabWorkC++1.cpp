#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory>

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

// Абстракция — интерфейс обработки файлов
class IFileProcessor {
public:
    virtual void processFile(const string& filename, const Options& opts) = 0;
    virtual ~IFileProcessor() = default;
};

// Конкретная реализация
class FileProcessor : public IFileProcessor {
public:
    static size_t countUtf8Chars(const string& str) {
        size_t count = 0;
        for (size_t i = 0; i < str.size(); ++i) {
            if ((str[i] & 0xC0) != 0x80) {
                count++;
            }
        }
        return count;
    }

    void processFile(const string& filename, const Options& opts) override {
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
            charCount += countUtf8Chars(line);
        }
        file.clear();
        file.seekg(0, ios::end);
        byteCount = file.tellg();

        bool noOption = !opts.lines && !opts.words && !opts.bytes && !opts.chars;
        if (opts.lines || noOption) cout << lineCount << " ";
        if (opts.words || noOption) cout << wordCount << " ";
        if (opts.bytes || noOption) cout << byteCount << " ";
        if (opts.chars || noOption) cout << charCount << " ";
        cout << filename << endl;
    }
};

class WordCount {
    unique_ptr<IFileProcessor> processor;
public:
    WordCount(unique_ptr<IFileProcessor> proc) : processor(move(proc)) {}

    void run(int argc, char* argv[]) {
        Options opts;
        vector<string> filenames;

        for (int i = 1; i < argc; ++i) {
            string arg = argv[i];
            if (arg[0] == '-') {
                opts.parseArgs(arg);
            }
            else {
                filenames.push_back(arg);
            }
        }

        for (const auto& fname : filenames) {
            processor->processFile(fname, opts);
        }
    }
};

int main(int argc, char* argv[]) {
    unique_ptr<IFileProcessor> processor = make_unique<FileProcessor>();
    WordCount wc(move(processor));
    wc.run(argc, argv);
    return 0;
}
