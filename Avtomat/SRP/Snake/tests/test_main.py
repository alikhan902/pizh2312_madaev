import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Добавляем корень проекта в sys.path

# Теперь импортируем классы из их соответствующих файлов
from Snake.renderers import GameObject  # Класс GameObject из файла game.py
from Snake.apple import Apple      # Класс Apple из файла apple.py
from Snake.snake import Snake      # Класс Snake из файла snake.py

# Тесты на наличие классов
def test_gameobject_class_exists():
    assert GameObject, "Класс `GameObject` не найден в модуле `game.py`."


def test_apple_class_exists():
    assert Apple, "Класс `Apple` не найден в модуле `apple.py`."


def test_snake_class_exists():
    assert Snake, "Класс `Snake` не найден в модуле `snake.py`."


# Пример дополнительных тестов
def test_apple_inherits_from_gameobject():
    assert issubclass(Apple, GameObject), "Класс `Apple` должен наследоваться от `GameObject`."


def test_snake_inherits_from_gameobject():
    assert issubclass(Snake, GameObject), "Класс `Snake` должен наследоваться от `GameObject`."
