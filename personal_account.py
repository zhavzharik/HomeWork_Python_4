personal_account = 0   # переменная для учета средств на личном счете пользователя
sum_history = []       # здесь будет храниться история названия покупок
name_history = []      # здесь будет храниться история суммы покупок
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        refill = float(input('Введите сумму для пополнения счета '))
        personal_account += refill

    elif choice == '2':
        sum_buy = float(input('Введите сумму покупки '))
        if sum_buy > personal_account:
            print('Денег на счете недостаточно')

        else:
            name_buy = input('Введите название покупки ')
            personal_account -= sum_buy
            sum_history.append(sum_buy)
            name_history.append(name_buy)

    elif choice == '3':
        if len(sum_history) == 0:
            print('Покупок не было')
        else:
            print('*'*39)
            print('История покупок:')
            for i in range(len(name_history)):
                print(f" {name_history[i]} {'_' * (25-len(name_history[i]))} {sum_history[i]} руб.")
            print('*' * 39)
            # print(list(zip(name_history, sum_history))) второй вариант вывода истории покупок списком
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
