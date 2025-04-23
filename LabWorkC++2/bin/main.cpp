#include <lib/number.h>
#include <iostream>

int main() {

    setlocale(LC_ALL, "Russian");
    // �������� �� ������
    uint2022_t a = from_string("90");
    uint2022_t b = from_string("45");

    // ����������
    uint2022_t sum = a + b;
    uint2022_t diff = b - a;
    uint2022_t prod = a * b;

    // ������� 
    uint2022_t quot = b / a;

    // �����
    std::cout << "a:     " << a << std::endl;
    std::cout << "b:     " << b << std::endl;
    std::cout << "a + b: " << sum << std::endl;
    std::cout << "b - a: " << diff << std::endl;
    std::cout << "a * b: " << prod << std::endl;
    std::cout << "b / a: " << quot << std::endl;

    // ���������
    if (a == b)
        std::cout << "a ����� b" << std::endl;
    else
        std::cout << "a �� ����� b" << std::endl;

    return 0;
}
