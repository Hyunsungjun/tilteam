import random
number = random.randint(1,999)
print(number)

while 1:
    try:
        guess = int(input('숫자를 입력해 : '))
        if guess == number:
            print('정답')
            break
        elif guess > number:
            print('작다')
        else:
            print('더큰 수라고!')
    except:
        print('숫자라고')
        QQ = input('종료 하쉴?(Q): ')
        if str(QQ.upper()) == "Q": #드디어 종료문 만들었다.. 예외처리를 해버리니까 끌수가없다..
            break