# Требуется найти в списке целых чисел самый близкий по величине элемент к 
# заданному числу X. Пользователь вводит это число с клавиатуры, список можно 
# считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

my_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
number = int(input("Введите число: "))
sort_list = sorted(my_list)
max_num = max(my_list)
if number >= max_num:
    print(max_num)
else:
    for i in sort_list:
        if i >= number:
            print(i)
            break
    else:
        print(sort_list[0])
    
    