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

