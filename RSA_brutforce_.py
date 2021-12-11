import time

def dcmpsnumprdcng2fctr():
    def check(to_check):
        check = 0
        if to_check == 2 or to_check == 3 or to_check == 5 or to_check == 7:
            check = 1
        else:
            for check_num in range(2, to_check//2):
                if to_check%check_num != 0:
                    check = 1
                else:
                    check = 0
                    break
        return(check)

    number = int(input("Введите простое число для разложения: \n"))
    ans = 0
    ans_dict = 0
    for devider in range(2, number//2):
        print("checked devider", devider, "False")
        if ans == 1:
            break
        else:
            if number%devider == 0:
                checked = check(devider)
                if checked == 1:
                    scnd_num = int(number/devider)
                    checked = check(scnd_num)
                    if checked == 1:
                        ans == 1
                        ans_dict = {"Первое число": devider, "Второе число": scnd_num}
                    else:
                        ans == 1
                        ans_dict = "Это число не может быть открытым числом" 
    if ans_dict == 0:
        ans_dict = "Это число простое!"
    return(ans_dict)

what_to_do = int(input("Привет, я шфировальшик по шифру RSA! Чем я могу быть полезен? 1 - Разложить число на производение двух множителей\n"))
if what_to_do == 1:
    time_start=time.time()
    ans = dcmpsnumprdcng2fctr()
    time_fin=time.time()
    gone_time = time_fin - time_start
    print("Ответ: ", ans)
    if gone_time >= 60:
        gone_time = gone_time / 60
        ntrv = "минут."
    else:
        ntrv = "секунд."
    print("Время выполнения программы: ", gone_time," ", ntrv)
else:
    print("Упс, я такого ещё не умею:)")