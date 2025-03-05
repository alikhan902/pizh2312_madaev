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
