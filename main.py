e = int(input(
    "Введите количество вещественных чисел, которые хотите упаковать в список: "))  # Получаем количество элементов в
# будущем списке
a = list()  # Создаем новый список для элементов с вещественным типом
for i in range(e): # Записываем элементы в список с вещественным типом
    a.append(float(input(f"Введите число, которое хотите поместить на позицию {i} (float): "))) # Записываем в список элементы
print(f"Получившейся список - {a}. Выполняю преобразование...")  # Выводим получившийся список
b = list()  # Создаем новый список для целого типа
for c in a:  # Для c в списке с числами вещественного типа
    b.append(int(c)) # Добавить в список целого типа целую часть числа из списка вещественных чисел
print(f"Преобразованный список - {b}")  # Выводим получившийся список
