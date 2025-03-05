from deposit import *

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