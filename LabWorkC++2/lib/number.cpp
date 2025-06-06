#include "number.h"
#include <cstring>
#include <string>
#include <algorithm>
#include <stdexcept>

// ========================== ����������� ==========================

uint2022_t from_uint(uint32_t i) {
    uint2022_t result = {};
    result.data[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);
    std::string str(buff);

    for (char c : str) {
        if (c < '0' || c > '9') throw std::invalid_argument("������������ ����� � ������");
        result = result * from_uint(10);
        result = result + from_uint(c - '0');
    }

    return result;
}

// ========================== ���������� ==========================

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result = {};
    uint64_t carry = 0;  // ������ ����� ������� �� ���� ��������

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t sum = uint64_t(lhs.data[i]) + rhs.data[i] + carry;
        result.data[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;  // ������� � ������� ������

        // �������� ������������ �� ���� �������
        if (carry != 0 && i == LIMBS - 1) {  // ���� ������� ������� �� ������� ���������� �������
            std::cerr << "��������������: ������������ ��� �������� uint2022_t!" << std::endl;
            throw std::overflow_error("������������ ��� �������� uint2022_t");
        }
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (lhs < rhs) {
        std::cerr << "��������������: ��������� ������������ ��� ��������� uint2022_t (������������� ���������). ������ ���������� (y/n)? ";
        char choice;
        std::cin >> choice;
        if (choice != 'y' && choice != 'Y') {
            std::cerr << "�������� ��������." << std::endl;
            throw std::overflow_error("������������ ��� ��������� uint2022_t");
        }
    }

    uint2022_t result = {};
    int64_t borrow = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        int64_t diff = int64_t(lhs.data[i]) - rhs.data[i] - borrow;
        if (diff < 0) {
            diff += (1LL << 32);
            borrow = 1;
        }
        else {
            borrow = 0;
        }
        result.data[i] = static_cast<uint32_t>(diff);
    }

    if (borrow != 0) {
        std::cerr << "��������������: ��������� ������������ ��� ��������� uint2022_t. ������ ���������� (y/n)? ";
        char choice;
        std::cin >> choice;
        if (choice != 'y' && choice != 'Y') {
            std::cerr << "�������� ��������." << std::endl;
            throw std::overflow_error("������������ ��� ��������� uint2022_t");
        }
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result = {};  // ��������� ���������
    uint64_t temp[2 * LIMBS] = {};  // ��������� ������ ��� �������� ������������� ������

    for (size_t i = 0; i < LIMBS; ++i) {
        for (size_t j = 0; j < LIMBS; ++j) {
            uint64_t product = uint64_t(lhs.data[i]) * rhs.data[j];
            uint64_t sum = temp[i + j] + product;
            temp[i + j] = static_cast<uint32_t>(sum);  // ���������� ���������
            temp[i + j + 1] += sum >> 32;  // ������� � ��������� ������
        }
    }

    // �������� �� ������������: ���� ��������� ������� �� 70 ���������, ��� ������������
    bool overflow = false;
    for (size_t i = LIMBS; i < 2 * LIMBS; ++i) {
        if (temp[i] != 0) {
            overflow = true;  // ���� ������� ������ �� ������� � ������������
            break;
        }
    }

    if (overflow) {
        std::cerr << "��������������: ��������� ������������ ��� ��������� uint2022_t!" << std::endl;
        throw std::overflow_error("������������ ��� ��������� uint2022_t");
    }

    // ���������� ��������� � �������� ������
    for (size_t i = 0; i < LIMBS; ++i) {
        result.data[i] = static_cast<uint32_t>(temp[i]);
    }

    return result;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) {
        throw std::domain_error("������� �� ���� � uint2022_t");
    }

    uint2022_t result = from_uint(0);
    uint2022_t remainder = from_uint(0);

    for (int i = LIMBS * 32 - 1; i >= 0; --i) {
        for (int j = LIMBS - 1; j > 0; --j) {
            remainder.data[j] = (remainder.data[j] << 1) | (remainder.data[j - 1] >> 31);
        }
        remainder.data[0] = (remainder.data[0] << 1) | ((lhs.data[i / 32] >> (i % 32)) & 1);

        if (!(remainder < rhs)) {
            remainder = remainder - rhs;
            result.data[i / 32] |= (1u << (i % 32));
        }
    }

    return result;
}

// ========================== ��������� ==========================

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (size_t i = 0; i < LIMBS; ++i) {
        if (lhs.data[i] != rhs.data[i]) return false;
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = LIMBS - 1; i >= 0; --i) {
        if (lhs.data[i] < rhs.data[i]) return true;
        if (lhs.data[i] > rhs.data[i]) return false;
    }
    return false;
}

// ========================== ����� ==========================

std::pair<uint2022_t, uint8_t> divmod10(const uint2022_t& value) {
    uint2022_t quotient = from_uint(0);
    uint64_t remainder = 0;

    for (int i = LIMBS - 1; i >= 0; --i) {
        uint64_t part = (remainder << 32) | value.data[i];
        quotient.data[i] = static_cast<uint32_t>(part / 10);
        remainder = static_cast<uint8_t>(part % 10);
    }

    return { quotient, static_cast<uint8_t>(remainder) };
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    uint2022_t temp = value;
    std::string result;

    while (!(temp == from_uint(0))) {
        auto [quotient, remainder] = divmod10(temp);
        result += char('0' + remainder);
        temp = quotient;
    }

    if (result.empty()) {
        result = "0";
    }

    std::reverse(result.begin(), result.end());
    stream << result;
    return stream;
}
