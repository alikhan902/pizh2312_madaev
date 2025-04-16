#include "number.h"
#include <cstring>
#include <string>
#include <algorithm>
#include <stdexcept>

// ========================== Конвертации ==========================

uint2022_t from_uint(uint32_t i) {
    uint2022_t result = {};
    result.data[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);
    std::string str(buff);

    for (char c : str) {
        if (c < '0' || c > '9') throw std::invalid_argument("Invalid digit in string");
        result = result * from_uint(10);
        result = result + from_uint(c - '0');
    }

    return result;
}

// ========================== Арифметика ==========================

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result = {};
    uint64_t carry = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t sum = uint64_t(lhs.data[i]) + rhs.data[i] + carry;
        result.data[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;
    }

    if (carry != 0) {
        throw std::overflow_error("Overflow in uint2022_t addition");
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (lhs < rhs) {
        throw std::overflow_error("Overflow in uint2022_t subtraction (negative result)");
    }

    uint2022_t result = {};
    int64_t borrow = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        int64_t diff = int64_t(lhs.data[i]) - rhs.data[i] - borrow;
        if (diff < 0) {
            diff += (1LL << 32);
            borrow = 1;
        } else {
            borrow = 0;
        }
        result.data[i] = static_cast<uint32_t>(diff);
    }

    // Проверка переполнения: если результат больше левого операнда, это ошибка
    if (borrow != 0) {
        throw std::overflow_error("Overflow in uint2022_t subtraction");
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint64_t temp[2 * LIMBS] = {};
    bool nonZeroLhs = false, nonZeroRhs = false;

    // Проверка на ненулевые множители
    for (size_t i = 0; i < LIMBS; ++i) {
        if (lhs.data[i] != 0) nonZeroLhs = true;
        if (rhs.data[i] != 0) nonZeroRhs = true;
    }

    // Умножение
    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < LIMBS; ++j) {
            size_t k = i + j;
            if (k >= 2 * LIMBS) continue;
            uint64_t mul = uint64_t(lhs.data[i]) * rhs.data[j];
            uint64_t sum = temp[k] + mul + carry;
            carry = sum >> 32;
            temp[k] = static_cast<uint32_t>(sum);
        }
        // Сохраняем остаточный перенос
        size_t carry_index = i + LIMBS;
        if (carry_index < 2 * LIMBS) {
            temp[carry_index] += carry;
        }
        else if (carry != 0) {
            std::cerr << "Overflow in uint2022_t multiplication (carry overflow)" << std::endl;
            throw std::overflow_error("Overflow in uint2022_t multiplication");
        }
    }

    // Проверка переполнения: старшие LIMBS должны быть нулевые
    for (size_t i = LIMBS; i < 2 * LIMBS; ++i) {
        if (temp[i] != 0) {
            std::cerr << "Overflow in uint2022_t multiplication (higher limbs non-zero)" << std::endl;
            throw std::overflow_error("Overflow in uint2022_t multiplication");
        }
    }

    uint2022_t result;
    for (size_t i = 0; i < LIMBS; ++i) {
        result.data[i] = static_cast<uint32_t>(temp[i]);
    }

    // Проверка переполнения: если результат стал нулевым, но множители не нули
    if (result == from_uint(0) && (nonZeroLhs && nonZeroRhs)) {
        std::cerr << "Overflow in uint2022_t multiplication (unexpected zero result)" << std::endl;
        throw std::overflow_error("Overflow in uint2022_t multiplication (unexpected zero result)");
    }

    return result;
}


uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) {
        throw std::domain_error("Division by zero in uint2022_t");
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

// ========================== Сравнения ==========================

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

// ========================== Вывод ==========================

std::pair<uint2022_t, uint8_t> divmod10(const uint2022_t& value) {
    uint2022_t quotient = from_uint(0);
    uint64_t remainder = 0;

    // Используем деление на 10 по 32-битным частям
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

    // Пока число не равно нулю
    while (!(temp == from_uint(0))) {
        auto [quotient, remainder] = divmod10(temp);
        result += char('0' + remainder);  // Добавляем цифру к строке
        temp = quotient;  // Обновляем число
    }

    // Если результат пуст, значит число 0
    if (result.empty()) {
        result = "0";
    }

    // Переворачиваем строку для правильного отображения
    std::reverse(result.begin(), result.end());
    stream << result;
    return stream;
}
