#include <fstream>
#include <iostream>
#include <vector>
#include "lib//MP3Parser.h"

constexpr int ID3_HEADER_SIZE = 10;

void reportError(const std::string& message) {
    std::cerr << "[!] " << message << '\n';
}

bool isHeaderValid(const std::string& header) {
    return header.size() == ID3_HEADER_SIZE && header.substr(0, 3) == "ID3";
}

struct ID3Tag {
    uint8_t major;
    uint8_t minor;
    uint8_t flags;
    uint32_t dataSize;
};

ID3Tag parseHeader(const std::string& header) {
    return {
        static_cast<uint8_t>(header[3]),
        static_cast<uint8_t>(header[4]),
        static_cast<uint8_t>(header[5]),
        calculateFrameSize({
            static_cast<uint8_t>(header[6]),
            static_cast<uint8_t>(header[7]),
            static_cast<uint8_t>(header[8]),
            static_cast<uint8_t>(header[9])
        })
    };
}

int handleAudioFile(const char* filePath) {
    std::ifstream input(filePath, std::ios::binary);
    if (!input.is_open()) {
        reportError("Unable to open the file");
        return 2;
    }

    std::string header(ID3_HEADER_SIZE, '\0');
    input.read(&header[0], ID3_HEADER_SIZE);

    if (!isHeaderValid(header)) {
        reportError("Unrecognized or missing ID3 metadata");
        return 3;
    }

    ID3Tag tagInfo = parseHeader(header);
    std::cout << "[*] Metadata v" << static_cast<int>(tagInfo.major)
        << "." << static_cast<int>(tagInfo.minor)
        << ", size: " << tagInfo.dataSize << " bytes\n";

    parseMetadataBlocks(input, tagInfo.dataSize);
    return 0;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        reportError("Audio file path not provided");
        return 1;
    }
    return handleAudioFile(argv[1]);
}
