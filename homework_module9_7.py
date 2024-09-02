import math

# Функция, которая складывает три числа
def sum_three(a, b, c):
    return a + b + c

# Декоратор для проверки на простое число
def is_prime(func):
    def wrapper(*args, **kwargs):
        # Вызываем исходную функцию и сохраняем результат
        result = func(*args, **kwargs)
        
        # Проверка, является ли число простым
        if result > 1:
            for i in range(2, int(math.sqrt(result)) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        
        return result
    
    return wrapper

# Применение декоратора к функции sum_three
@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)
