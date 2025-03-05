Мадаев Алихан Ахьядович
ПИЖ-б-о-23-1

Задание 1. Банк

main.py

from module import *

# Ввод значений
amount: float = float(input("Введите сумму вклада: "))
term: int = int(input("Введите срок (лет): "))

best: Deposit = DepositManager.choose_best_deposit(amount, term) # Выбор лучшего депозита

print(f"Лучший вклад: {best.__class__.__name__}, Итоговая сумма: {best.get_final_amount()}")
# Результат


deposit.py


class Deposit:
    """
    Базовый класс для вкладов.
    """
    def __init__(self, amount: float, term: int, rate: float):
        """
        :param amount: float - Сумма вклада
        :param term: int - Срок вклада (в годах)
        :param rate: float - Годовая процентная ставка
        """
        self.amount: float = amount
        self.term: int = term
        self.rate: float = rate

    def calculate_profit(self) -> float:
        """
        Метод расчёта прибыли (должен быть переопределён в наследниках).
        :return: float - Прибыль от вклада
        """
        pass

    def get_final_amount(self) -> float:
        """
        Рассчитывает итоговую сумму вклада.
        :return: float - Итоговая сумма (вклад + прибыль)
        """
        return self.amount + self.calculate_profit()


deposits.py


class FixedDeposit(Deposit):
    """
    Вклад с фиксированным начислением процентов.
    """
    def calculate_profit(self) -> float:
        """
        Расчёт прибыли по формуле простых процентов.
        :return: float - Прибыль от вклада
        """
        return self.amount * self.rate * self.term / 100


class BonusDeposit(Deposit):
    """
    Вклад с бонусной системой для крупных сумм.
    """
    BONUS_THRESHOLD: float = 100000  # Порог для начисления бонуса
    BONUS_RATE: float = 5  # Дополнительный процент от прибыли

    def calculate_profit(self) -> float:
        """
        Расчёт прибыли с учётом бонусов для крупных вкладов.
        :return: float - Прибыль от вклада
        """
        profit: float = self.amount * self.rate * self.term / 100
        if self.amount > self.BONUS_THRESHOLD:
            profit += profit * self.BONUS_RATE / 100
        return profit


class CapitalizedDeposit(Deposit):
    """
    Вклад с капитализацией процентов.
    """
    def calculate_profit(self) -> float:
        """
        Расчёт прибыли по формуле сложных процентов.
        :return: float - Прибыль от вклада
        """
        return self.amount * ((1 + self.rate / 100) ** self.term - 1)

depositManager

class DepositManager:
    """
    Класс для управления вкладами.
    """
    @staticmethod
    def choose_best_deposit(amount: float, term: int) -> Deposit:
        """
        Выбирает вклад с наибольшей прибылью.
        :param amount: float - Сумма вклада
        :param term: int - Срок вклада (в годах)
        :return: Deposit - Экземпляр лучшего вклада
        """
        deposits = [
            FixedDeposit(amount, term, 10),
            BonusDeposit(amount, term, 10),
            CapitalizedDeposit(amount, term, 10)
        ]
        best_deposit = max(deposits, key=lambda d: d.calculate_profit())
        return best_deposit


Задание 2. Money

main.py

from module import *
# Тестирование функционала
if __name__ == "__main__":
    m1 = Money(100.75)
    m2 = Money.from_string("200.50")
    print(m1)  # 100.75 USD
    print(m2)  # 200.50 USD
    
    m3 = m1 + m2
    print(m3)  # 301.25 USD
    
    m4 = m3 - Money(50)
    print(m4)  # 251.25 USD
    
    m5 = m4 * 1.1
    print(m5)  # 276.38 USD
    
    m5.save("money.json")
    loaded_money = Money.load("money.json")
    print(loaded_money)  # 276.38 USD


module.py

import json

class Money:
    """
    Класс Money представляет денежную сумму с возможностью арифметических операций
    и сохранения/загрузки из JSON-файла.
    """
    def __init__(self, amount: float):
        """
        Инициализация объекта Money.
        :param amount: Сумма денег в виде float.
        """
        self._amount = round(amount, 2)
    
    @property
    def amount(self):
        """Геттер для получения суммы денег."""
        return self._amount
    
    @amount.setter
    def amount(self, value):
        """Сеттер для установки суммы денег."""
        if value < 0:
            raise ValueError("Сумма денег не может быть отрицательной")
        self._amount = round(value, 2)
    
    def __str__(self):
        """Возвращает строковое представление объекта Money."""
        return f"{self.amount} USD"
    
    @classmethod
    def from_string(cls, str_value: str):
        """Создает объект Money из строки."""
        return cls(float(str_value))
    
    def save(self, filename):
        """Сохраняет объект Money в JSON-файл."""
        with open(filename, 'w') as file:
            json.dump({'amount': self.amount}, file)
    
    @classmethod
    def load(cls, filename):
        """Загружает объект Money из JSON-файла."""
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data['amount'])
    
    def __add__(self, other):
        """Позволяет складывать два объекта Money."""
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        """Позволяет вычитать один объект Money из другого."""
        return Money(self.amount - other.amount)
    
    def __mul__(self, factor: float):
        """Позволяет умножать объект Money на число."""
        return Money(self.amount * factor)
    
