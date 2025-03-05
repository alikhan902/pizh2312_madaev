from module import *

# Ввод значений
amount: float = float(input("Введите сумму вклада: "))
term: int = int(input("Введите срок (лет): "))

best: Deposit = DepositManager.choose_best_deposit(amount, term) # Выбор лучшего депозита

print(f"Лучший вклад: {best.__class__.__name__}, Итоговая сумма: {best.get_final_amount()}")
# Результат
