import time
import math
import random

def defact(num):  #разложение числа на множители
    x = random.randint(1, num-2)
    y = 1 
    i = 0
    stage = 2
    while math.gcd(num, abs(x - y)) == 1: #код из википедии
        if i == stage:
            y = x
            stage = stage*2 
        x = (x*x + 1) % num
        i = i + 1
    ans = math.gcd(num, abs(x-y))
    devider = ans #Делитель
    scnd_num = num//ans # число : делитель
    print("Checking num to be plain...")
    if ans == num:       # проверка не простое ли число            
        ans = "Это простое число, оно не может быть открытым ключом"
        print("Plainless = True. Breaking...")
        return ans
    what_to_check = devider
    print("False. Continuing")
    print("Checking divisor to be plain...")
    if check_plainless_general(what_to_check) == 0: #проверка делителя на простоту
        ans = "Это число не может быть открытым ключом"
        print("Plainless = True. Breaking...")
        return ans
    print("False. Continuing")
    what_to_check = scnd_num
    print("Checking quotient to be plain...")
    if check_plainless_general(what_to_check) == 0: #проверка второго числа на простоту
        ans = "Это число не может быть открытым ключом"
        print("Plainless = True. Breaking...")
        return ans
    print("False. Continuing")
    ans = {"Первое число": devider, "Второе число": scnd_num}
    return ans

def check_plainless_general(what_to_check):  # функция проверки простоты числа
    def check_plainlesss_brutforce(e):
        check = 0
        if e == 2 or e == 3 or e == 5 or e == 7:
            check = 1
        else:
            for check_num in range(2, e//2):
                if e%check_num != 0:
                    print("e checked with number: ", check_num)
                    check = 1 #простое
                    break
        return(check)

    e = what_to_check
    check = 1
    if e < 100: # функция проверки простоты числа, работает также как и брутфорс функция разложения числ(check)
        if check_plainlesss_brutforce(e) == 0:
            check = 0
    else:      # функция проверки простоты числа, работает также как и основная функция разложения числа(defuct)
        num = e
        x = random.randint(1, num-2)
        y = 1 
        i = 0
        stage = 2
        while math.gcd(num, abs(x - y)) == 1:
            if i == stage:
                y = x
                stage = stage*2 
            x = (x*x + 1) % num
            i = i + 1
        ans = math.gcd(num, abs(x-y))
        if ans != num:
            check = 0
    return check

def encrypt_with_okey(open_key, message): #шифрование при помощи открытого ключа
    open_key_list = open_key.split()
    e = int(open_key_list.pop(0))
    n = int(open_key_list.pop(0))
    if message > n:
        encrypted_data ="Сообщение не может быть больше модуля: необходимы числа больше, вы дали в открытом ключе "
    frst_act = message ** e
    encrypted_data = frst_act % n
    return encrypted_data

def decrypt_with_ckey(closed_key, message): #дешифрование при помощи закрытого ключа
    open_key_list = closed_key.split()
    d = int(open_key_list.pop(0))
    n = int(open_key_list.pop(0))
    frst_act = message ** d
    decrypted_data = frst_act % n
    return decrypted_data

def creating_any_keys(p, q):
    def check_e_num(e, E_func):
        check_e = 1    
        if check_plainless_general(e) == 0: #проверка на простоту 0 - не простое 1 - простое 
            check_e = 0
        print("Plainless checked")
        if e >= E_func:
            check_e = 0
        if math.gcd(e, E_func) != 1:
            check_e = 0
        print("GCD found...")
        print("check_e: ", check_e)
        return check_e        
    
    what_to_check = p
    if check_plainless_general(what_to_check) != 1:
        ans = 'Первое число не простое'
        return ans
    what_to_check = q
    if check_plainless_general(what_to_check) != 1:
        ans = 'Второе число не простое'
        return ans

    d = 1
    e = 1
    n = p*q
    E_func = (p-1)*(q-1)
    while check_e_num(e, E_func) != 1:
        e += 1
        print("Число е", e)
    e_str = str(e)
    n_str = str(n)
    open_dict = "Открытый ключ: " + "Открытая экспонента: " + e_str + " Модуль: " + n_str
    
    while (d*e)%E_func != 1:
        d += 1
    d_str = str(d)
    close_dict = "Закрытый ключ: " + "Число d: " + d_str + " Модуль: " + n_str
    return open_dict, close_dict

def creating_keys_by_computer(from_to):
    from_to_list = from_to.split()
    frm = int(from_to_list.pop(0))
    to = int(from_to_list.pop(0))
    print(frm, to)
    p = random.randint(frm, to)
    q = random.randint(frm, to)
    print(p, q)
    what_to_check = p #превращаю e в p для удобства проверки
    while check_plainless_general(what_to_check) != 1:
        print("Trying to find p: ", p)
        print(check_plainless_general(what_to_check))
        p = random.randint(frm, to)
        what_to_check = p #превращаю p в e для удобства проверки
    print("p = ", p)
    what_to_check = q
    while check_plainless_general(what_to_check) != 1:
        print("Trying to find q: ", q)
        print(check_plainless_general(what_to_check))
        q = random.randint(frm, to)
        what_to_check = q #превращаю q в e для удобства проверки
    print("q = ", q)
    ans = creating_any_keys(p, q)
    return ans

while True:
    what_to_do = int(input("Привет, я шфировальшик по шифру RSA! Чем я могу быть полезен? 1 - Разложить число на производение двух множителей 2 - Шифровать данные при помощи вашего открытого ключа 3 - Дешифровать данные при поиощи вашего закрытого ключа 4 - Создать открытые и закрытые ключи\n"))
    if what_to_do == 1:
        num = int(input("Введите число для разложения на множители: \n"))
        time_start=time.time() # начало измерения времени выполнения функции
        ans = defact(num) 
        time_fin=time.time() #конец измерения времении выполнения функции
        gone_time = time_fin - time_start
        print("Ответ: ", ans)
        if gone_time >= 60:
            gone_time = gone_time // 60
            ntrv = "минут."
        else:
            ntrv = "секунд."
        print("Время выполнения программы: ", gone_time," ", ntrv)
    if what_to_do == 2:
        open_key = input("Для шифрование введите открытый ключ через пробел\n")
        message = int(input("Для шифрование введите ваше сообщение\n"))
        time_start=time.time() # начало измерения времени выполнения функции
        ans = encrypt_with_okey(open_key, message) 
        time_fin=time.time() #конец измерения времении выполнения функции
        gone_time = time_fin - time_start
        print("Ответ: ", ans)
        if gone_time >= 60:
            gone_time = gone_time // 60
            ntrv = "минут."
        else:
            ntrv = "секунд."
        print("Время выполнения программы: ", gone_time," ", ntrv)
    if what_to_do == 3:
        closed_key = input("Для дешифрования введите закрытый ключ через пробел\n")
        message = int(input("Для дешифрования введите ваше сообщение\n"))
        time_start=time.time() # начало измерения времени выполнения функции
        ans = decrypt_with_ckey(closed_key, message) 
        time_fin=time.time() #конец измерения времении выполнения функции
        gone_time = time_fin - time_start
        print("Ответ: ", ans)
        if gone_time >= 60:
            gone_time = gone_time // 60
            ntrv = "минут."
        else:
            ntrv = "секунд."
        print("Время выполнения программы: ", gone_time," ", ntrv)
    if what_to_do == 4:
        p = 0
        q = 0
        user_ask = int(input("Вы хотите сами ввести простые числа или чтобы их сгенерировал компьютер 1 - Сам(а) 2 - Компьютер\n"))
        if user_ask == 1:
            p = int(input("Введите первое простое число: \n"))
            q = int(input("Введите второе простое число: \n"))
            time_start=time.time() # начало измерения времени выполнения функции
            ans_list = creating_any_keys(p, q)
            time_fin=time.time() #конец измерения времении выполнения функции
            gone_time = time_fin - time_start  
        if user_ask == 2:
            from_to = input("Введите от какого и до какого хотите видеть простые числа?(через пробел)\n")
            time_start=time.time() # начало измерения времени выполнения функции
            ans_list = creating_keys_by_computer(from_to)
            time_fin=time.time() #конец измерения времении выполнения функции
        print(ans_list)
        gone_time = time_fin - time_start
        if gone_time >= 60:
            gone_time = gone_time // 60
            ntrv = "минут."
        else:
            ntrv = "секунд."
        print("Время выполнения программы: ", gone_time," ", ntrv)

    if what_to_do > 4:
        print("Упс, я такого ещё не умею:)")
#проверка работы репозитория