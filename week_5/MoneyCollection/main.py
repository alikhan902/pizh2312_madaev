from moneyCollection import *
# Пример использования
money1 = Money(100.5)
money2 = Money(200.75)

# Создаем коллекцию
collection = MoneyCollection(money1, money2)

# Добавляем новый объект
collection.add(Money(50))

# Выводим коллекцию
print(collection)

# Сохраняем в файл
collection.save("money_collection.json")

# Загружаем из файла
loaded_collection = MoneyCollection.load("money_collection.json")
print(loaded_collection)
