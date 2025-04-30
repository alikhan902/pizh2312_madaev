cmake_minimum_required(VERSION 3.10)
project(MyProject)

# Установка стандарта C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Список исходных файлов
set(SOURCES
    bmpTest.cpp
    Grid.cpp
    main.cpp
)

# Список заголовочных файлов
set(HEADERS
    header.h
)

# Создание исполняемого файла
add_executable(MyProject ${SOURCES} ${HEADERS})

# Для Windows: установка кодировки UTF-8
if (WIN32)
    add_compile_options("$<$<C_COMPILER_ID:MSVC>:/utf-8>")
    add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>")
endif()

# Дополнительные настройки (если нужны)
# target_compile_options(MyProject PRIVATE ...)
# target_link_libraries(MyProject PRIVATE ...)