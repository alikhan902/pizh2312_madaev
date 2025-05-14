#pragma once
#include <array>
#include <memory>
#include <string>
#include <vector>
#include <unordered_map>

uint32_t calculateFrameSize(const std::array<uint8_t, 4>& bytes);

struct MetadataBlock {
    std::string id;
    uint32_t size;
    uint16_t flags;
    std::vector<uint8_t> data;

    MetadataBlock(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content);
    virtual void display() const;
    virtual ~MetadataBlock() = default;
};

struct TextFrame : MetadataBlock {
    TextFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content);
    void display() const override;
};

struct URLFrame : MetadataBlock {
    URLFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content);
    void display() const override;
};

struct CommentFrame : MetadataBlock {
    CommentFrame(const std::string& id, uint32_t sz, uint16_t fl, const std::vector<uint8_t>& content);
    void display() const override;
};

struct GenericFrame : MetadataBlock {
    using MetadataBlock::MetadataBlock;
};

std::string describeFrame(const std::string& id);
std::unique_ptr<MetadataBlock> buildFrame(const std::string& id, uint32_t size, uint16_t flags, const std::vector<uint8_t>& content);
void parseMetadataBlocks(std::ifstream& stream, uint32_t tagSize);
