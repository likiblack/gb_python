# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
the_sum = 0
print('----- Для выхода из программы исользуйте символ q -----')

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    for num in numbers:
        if num == 'q':
            print('----- Досвидания! ------')
            exit(0)
        else:
            try:
                the_sum = the_sum + int(num)
            except ValueError:
                pass
    print(f'- Сумма всех введеных значений равна: {the_sum}')



