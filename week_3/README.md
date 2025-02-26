Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1

Задание 4.3.1 Римское число

main.py

from module import *
# Создание объектов римских чисел
num1 = Roman("X")   # 10
num2 = Roman("V")   # 5
num3 = Roman("III") # 3

# Вывод значений
print(num1)  # X
print(num2)  # V
print(num3)  # III

# Арифметические операции
sum_result = num1 + num2  # 10 + 5 = XV
sub_result = num1 - num3  # 10 - 3 = VII
mul_result = num2 * num3  # 5 * 3 = XV
div_result = num1 // num3 # 10 // 3 = III

# Вывод результатов
print(sum_result)  # XV
print(sub_result)  # VII
print(mul_result)  # XV
print(div_result)  # III

# Вызов объекта (__call__)
print(num1())  # 10 (получение числового значения)


# Преобразование в int
print(int(num1))  # 10
print(int(num2))  # 5

module.py

from abc import ABC, abstractmethod

class AbstractRomanNumber(ABC):
    """
    Абстрактный класс для работы с римскими числами.
    Определяет интерфейс для реализации арифметических операций и преобразований.
    """
    @abstractmethod
    def __init__(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __floordiv__(self, other):
        pass
    
    @abstractmethod
    def __call__(self):
        pass


class RomanConverter:
    """
    Класс для преобразования римских чисел в арабские и обратно.
    Содержит методы для конвертации римских чисел в целые и наоборот.
    """
    ROMAN_TO_INT = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    INT_TO_ROMAN = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    @staticmethod
    def roman_to_int(roman):
        """
        Преобразует римское число в арабское.
        :param roman: Строка римского числа.
        :return: Целое число.
        """
        result, prev_value = 0, 0
        for char in reversed(roman):
            current_value = RomanConverter.ROMAN_TO_INT[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
        return result

    @staticmethod
    def int_to_roman(num):
        """
        Преобразует арабское число в римское.
        :param num: Целое число.
        :return: Строка римского числа.
        """
        result = ""
        for arabic, roman in RomanConverter.INT_TO_ROMAN:
            while num >= arabic:
                result += roman
                num -= arabic
        return result


class Roman(AbstractRomanNumber):
    """
    Класс для работы с римскими числами с использованием композиции.
    Позволяет выполнять арифметические операции и преобразования между римскими и арабскими числами.
    """
    
    def __init__(self, value):
        """
        Инициализация римского числа.
        :param value: Либо строка римского числа, либо целое число.
        :raises TypeError: Если переданный аргумент не является строкой или целым числом.
        """
        self.converter = RomanConverter()  # Создаем объект-конвертер
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, str):
            self.value = self.converter.roman_to_int(value)
        else:
            raise TypeError("Допустимы только строки римских чисел или целые числа")
    
    def __str__(self):
        """
        Возвращает строковое представление числа в римском формате.
        """
        return self.converter.int_to_roman(self.value)
    
    def __int__(self):
        """
        Возвращает целочисленное представление числа.
        """
        return self.value
    
    def __add__(self, other):
        """
        Складывает два римских числа.
        """
        return Roman(self.value + int(other))
    
    def __sub__(self, other):
        """
        Вычитает одно римское число из другого.
        """
        return Roman(self.value - int(other))
    
    def __mul__(self, other):
        """
        Умножает два римских числа.
        """
        return Roman(self.value * int(other))
    
    def __floordiv__(self, other):
        """
        Делит одно римское число на другое с округлением вниз.
        """
        return Roman(self.value // int(other))
    
    def __call__(self):
        """
        Возвращает целочисленное значение при вызове объекта.
        """
        return self.value

Задание 4.3.2 Пиццерия

main.py

from module import *

# Пример использования терминала
terminal = Terminal()

# Отображаем меню
terminal.show_menu()

# Обрабатываем команды (добавляем пиццы в заказ)
terminal.process_command(1)  # Добавляем Pepperoni
terminal.process_command(3)  # Добавляем Seafood

# Принимаем оплату и завершаем заказ
terminal.accept_payment()

module.py

class Pizza:
    """
    Класс Pizza представляет пиццу с различными аттрибутами, такими как имя, тесто, соус, начинка и цена.
    
    Атрибуты:
        __name (str): Имя пиццы.
        __dough (str): Тип теста.
        __sauce (str): Тип соуса.
        __filling (list): Список начинок.
        __price (float): Цена пиццы.
    """
    def __init__(self, name, dough, sauce, filling, price):
        """
        Инициализирует пиццу с заданными аттрибутами.

        Параметры:
            name (str): Имя пиццы.
            dough (str): Тип теста.
            sauce (str): Тип соуса.
            filling (list): Список начинок.
            price (float): Цена пиццы.
        """
        self.__name = name
        self.__dough = dough
        self.__sauce = sauce
        self.__filling = filling
        self.__price = price
    
    def __str__(self):
        """Возвращает строковое представление пиццы."""
        return f"Имя: {self.name}, тесто: {self.dough}, соус: {self.sauce}, начинка: {self.filling}, цена: {self.price}₽"

    @property
    def name(self):
        """Возвращает имя пиццы."""
        return self.__name

    @name.setter
    def name(self, value):
        """Устанавливает имя пиццы."""
        self.__name = value
        
    @property
    def dough(self):
        """Возвращает тесто."""
        return self.__dough

    @dough.setter
    def dough(self, value):
        """Устанавливает тесто."""
        self.__dough = value
     
    @property
    def sauce(self):
        """Возвращает соус."""
        return self.__sauce

    @sauce.setter
    def sauce(self, value):
        """Устанавливает соус."""
        self.__sauce = value
    
    @property
    def filling(self):
        """Возвращает начинку."""
        return self.__filling

    @filling.setter
    def filling(self, value):
        """Устанавливает начинку."""
        self.__filling = value
    
    @property
    def price(self):
        """Возвращает цену."""
        return self.__price

    @price.setter
    def price(self, value):
        """Устанавливает цену."""
        self.__price = value
    
    def prepare(self):
        """Подготовка пиццы."""
        print(f"Готовим {self.name} с тестом {self.dough}, соусом {self.sauce} и начинкой {', '.join(self.filling)}.")

    def bake(self):
        """Выпечка пиццы."""
        print(f"Выпекаем {self.name}...")

    def cut(self):
        """Нарезка пиццы."""
        print(f"Нарезаем {self.name} на кусочки.")

    def box(self):
        """Упаковка пиццы."""
        print(f"Упаковываем {self.name}.")
        
    
class PizzaPepperoni(Pizza):
    """Класс PizzaPepperoni наследует Pizza и представляет пиццу Пепперони."""
    def __init__(self):
        """Инициализирует пиццу Пепперони с конкретными аттрибутами."""
        super().__init__("Пепперони", "Тонкое тесто", "Томатный соус", ["Пепперони", "Сыр"], 300)

class PizzaBarbecue(Pizza):
    """Класс PizzaBarbecue наследует Pizza и представляет пиццу Барбекю."""
    def __init__(self):
        """Инициализирует пиццу Барбекю с конкретными аттрибутами."""
        super().__init__("Барбекю", "Толстое тесто", "Соус барбекю", ["Курица", "Лук", "Соус барбекю"], 350)

class PizzaSeafood(Pizza):
    """Класс PizzaSeafood наследует Pizza и представляет пиццу с морепродуктами."""
    def __init__(self):
        """Инициализирует пиццу с морепродуктами с конкретными аттрибутами."""
        super().__init__("Морепродукты", "Тонкое тесто", "Белый соус", ["Креветки", "Кальмары", "Мидии"], 450)

class Order:
    """
    Класс Order представляет заказ пользователя, включающий список заказанных пицц и их количество.

    Атрибуты:
        __ord_pizzas (list): Список заказанных пицц.
        __ord_counter (int): Количество заказанных пицц.
    """
    def __init__(self, ord_pizzas = [], ord_counter = 0):
        """
        Инициализирует заказ с пустым списком пицц и нулевым счетчиком.

        Параметры:
            ord_pizzas (list): Список заказанных пицц.
            ord_counter (int): Количество заказанных пицц.
        """
        self.__ord_pizzas = ord_pizzas
        self.__ord_counter = ord_counter
        
    def __str__(self):
        """Возвращает строковое представление заказа."""
        pizzList = [i.name for i in self.ord_pizzas]
        return f"Заказанные пиццы: {pizzList}, количество: {self.ord_counter}"
        
    @property
    def ord_pizzas(self):
        """Возвращает список заказанных пицц."""
        return self.__ord_pizzas

    @ord_pizzas.setter
    def ord_pizzas(self, value):
        """Устанавливает список заказанных пицц."""
        self.__ord_pizzas = value
    
    @property
    def ord_counter(self):
        """Возвращает количество заказанных пицц."""
        return self.__ord_counter

    @ord_counter.setter
    def ord_counter(self, value):
        """Устанавливает количество заказанных пицц."""
        self.__ord_counter = value


    def add_pizza(self, pizza):
        """
        Добавляет пиццу в заказ.

        Параметры:
            pizza (Pizza): Пицца, которую нужно добавить в заказ.
        """
        self.ord_pizzas.append(pizza)  
        self.ord_counter += 1
    
    def calculate_total(self):
        """Возвращает общую сумму заказа."""
        return sum(pizza.price for pizza in self.ord_pizzas)
    
    def execute(self):
        """Готовит, выпекает, нарезает и упаковывает все пиццы в заказе, а затем завершает заказ."""
        for pizza in self.ord_pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        print(f"Заказ готов. Общая сумма: {self.calculate_total():.2f}₽")

class Terminal:
    """
    Класс Terminal представляет интерфейс для заказа пиццы через терминал.

    Атрибуты:
        __menu (list): Список доступных пицц.
        __current_order (Order): Текущий заказ пользователя.
        __show_menu (bool): Флаг, определяющий, отображается ли меню.
    """
    def __init__(self):
        """
        Инициализирует терминал с предопределенным меню и пустым заказом.
        """
        self.__menu = [PizzaPepperoni(), PizzaBarbecue(), PizzaSeafood()]  # Меню с доступными пиццами
        self.__current_order = Order()  # Текущий заказ
        self.__show_menu = True  # Флаг для отображения меню
        
    @property
    def menu(self):
        """Возвращает список доступных пицц."""
        return self.__menu

    @menu.setter
    def menu(self, value):
        """Устанавливает список доступных пицц."""
        self.__menu = value
        
    @property
    def current_order(self):
        """Возвращает текущий заказ."""
        return self.__current_order

    @current_order.setter
    def current_order(self, value):
        """Устанавливает текущий заказ."""
        self.__current_order = value
        
    @property
    def show_menu(self):
        """Возвращает состояние отображения меню."""
        return self.__show_menu

    @show_menu.setter
    def show_menu(self, value):
        """Устанавливает состояние отображения меню."""
        self.__show_menu = value
             
    def __str__(self):
        """Возвращает строковое представление терминала."""
        return "Терминал для заказа пицц"

    def show_menu(self):
        """
        Отображает меню с доступными пиццами, если флаг show_menu установлен в True.
        """
        if self.show_menu:
            print("Добро пожаловать! Вот наше меню:")
            for i in self.menu:
                print(f"{i.name}")
    
    def process_command(self, menu_item):
        """
        Обрабатывает выбор пользователя и добавляет выбранную пиццу в заказ.

        Параметры:
            menu_item (int): Номер выбранной пиццы из меню.
        """
        if 1 <= menu_item <= len(self.menu):
            if menu_item == 1:
                self.current_order.add_pizza(PizzaPepperoni())
            elif menu_item == 2:
                self.current_order.add_pizza(PizzaBarbecue())
            elif menu_item == 3:
                self.current_order.add_pizza(PizzaSeafood())
        else:
            print("Неверный выбор. Пожалуйста, выберите пиццу из меню.")

    def accept_payment(self):
        """
        Принимает оплату и завершает заказ, если он есть.
        """
        if self.current_order:
            total = self.current_order.calculate_total()
            print(f"Общая сумма к оплате: {total}₽")
            # Симуляция оплаты
            print("Оплата принята. Спасибо за ваш заказ!")
            self.current_order.execute()
            self.current_order.ord_counter = 0
            self.current_order.ord_pizzas = []
        else:
            print("У вас нет активного заказа.")

