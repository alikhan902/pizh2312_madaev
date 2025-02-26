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
