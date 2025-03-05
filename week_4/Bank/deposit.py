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
