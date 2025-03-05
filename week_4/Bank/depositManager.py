from deposits import *

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