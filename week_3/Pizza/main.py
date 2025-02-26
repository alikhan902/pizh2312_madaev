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