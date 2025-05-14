#include "MP3Parser.h"
#include <fstream>
#include <iostream>
#include <algorithm>

uint32_t calculateFrameSize(const std::array<uint8_t, 4>& bytes) {
    return (bytes[0] << 21) | (bytes[1] << 14) | (bytes[2] << 7) | bytes[3];
}

MetadataBlock::MetadataBlock(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content)
    : id(id), size(sz), flags(fl), data(content) {
}

void MetadataBlock::display() const {
    std::cout << id << " [" << size << " bytes]";
}

std::string describeFrame(const std::string& id) {
    static const std::unordered_map<std::string, std::string> frameMap = {
        {"TIT2", "Title"}, {"TPE1", "Artist"}, {"TALB", "Album"},
        {"TRCK", "Track No."}, {"TYER", "Year"}, {"TDRC", "Date"},
        {"TCON", "Genre"}, {"COMM", "Comment"}, {"TENC", "Encoder"},
        {"TCOM", "Composer"}, {"TBPM", "BPM"}, {"TSSE", "Settings"},
        {"TPOS", "Part of Set"}
    };
    auto it = frameMap.find(id);
    return it != frameMap.end() ? it->second : "";
}

TextFrame::TextFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content)
    : MetadataBlock(id, sz, fl, content) {
}

void TextFrame::display() const {
    std::string contentText;
    if (!data.empty()) {
        contentText.assign(data.begin() + 1, data.end());
    }
    std::cout << "[*] " << id;
    auto label = describeFrame(id);
    if (!label.empty()) std::cout << " (" << label << ")";
    std::cout << ": " << contentText;
}

URLFrame::URLFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content)
    : MetadataBlock(id, sz, fl, content) {
}

void URLFrame::display() const {
    std::string url(data.begin(), data.end());
    std::cout << "[*] " << id << " (URL): " << url;
}

CommentFrame::CommentFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content)
    : MetadataBlock(id, sz, fl, content) {
}

void CommentFrame::display() const {
    if (data.size() < 4) {
        std::cout << "[?] Invalid comment frame";
        return;
    }
    std::string language(data.begin() + 1, data.begin() + 4);
    auto textIt = std::find(data.begin() + 4, data.end(), 0);
    std::string commentText(textIt + 1, data.end());
    std::cout << "[*] " << id << " [" << language << "]: " << commentText;
}

std::unique_ptr<MetadataBlock> buildFrame(const std::string& id, uint32_t size, uint16_t flags, const std::vector<uint8_t>& content) {
    if (id.empty()) return std::make_unique<GenericFrame>(id, size, flags, content);

    switch (id[0]) {
    case 'T': return std::make_unique<TextFrame>(id, size, flags, content);
    case 'W': return std::make_unique<URLFrame>(id, size, flags, content);
    case 'C': return id == "COMM" ? std::make_unique<CommentFrame>(id, size, flags, content) : nullptr;
    default: return std::make_unique<GenericFrame>(id, size, flags, content);
    }
}

void parseMetadataBlocks(std::ifstream& stream, uint32_t tagSize) {
    uint32_t bytesRead = 0;

    while (bytesRead + 10 <= tagSize) {
        std::string frameId(4, '\0');
        stream.read(&frameId[0], 4);
        if (stream.gcount() != 4 || frameId == "\0\0\0\0") break;

        std::array<uint8_t, 4> sizeBuf{};
        stream.read(reinterpret_cast<char*>(sizeBuf.data()), 4);
        uint32_t frameSize = calculateFrameSize(sizeBuf);

        uint16_t frameFlags = 0;
        stream.read(reinterpret_cast<char*>(&frameFlags), 2);

        if (frameSize == 0) break;

        std::vector<uint8_t> payload(frameSize);
        stream.read(reinterpret_cast<char*>(payload.data()), frameSize);
        if (stream.gcount() != static_cast<int>(frameSize)) break;

        bytesRead += 10 + frameSize;
        auto frame = buildFrame(frameId, frameSize, frameFlags, payload);
        if (frame) {
            frame->display();
            std::cout << '\n';
        }
    }
}
