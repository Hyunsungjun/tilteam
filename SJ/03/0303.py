# import random
# number = random.randint(1,999)

# while 1:
#     try:
#         guess = int(input('숫자를 입력해 : '))
#         if guess == number:
#             print('정답')
#             break
#         elif guess > number:
#             print('작다')
#         else:
#             print('더큰 수라고!')
#     except:
#         print('숫자라고')
#         QQ = input('종료 하쉴?(Q): ')
#         if str(QQ.upper()) == "Q": #드디어 종료문 만들었다.. 예외처리를 해버리니까 끌수가없다..
#             break
# 위 코드대로 실행 해보니까 내가 생각한 야구게임 맞긴한데 자세한 정보를 안주는게 단점
# 어제 오늘 포함해서 if문 while문 try ~ except문을 봤고 예외처리 해본거 처음이다

# import random
# number = str(random.randint(1,999)).zfill(3)
# # print(number)

# while True:
#     guess = input('숫자를 입력하겠니? : ')
#     if guess == number:
#         print('정답이디')
#         break
#     else:
#         strike = 0
#         ball = 0
#         for i in range(3):
#             if guess[i] == number[i]:
#                 strike += 1
#             elif guess[i] in number:
#                 ball += 1
#         print("스트라이크 : {} 볼:{}".format(strike,ball))

#스트라이크, 볼 구현 머리속에선 어려운 구현이라 생각 했는데 기본 기능 사용하니까 전부 되네

# import random
# number = str(random.randint(1,999)).zfill(3)

# while 1:
#     guess = input('숫자를 입력 : ')
#     if guess == number:
#         print('.. 정답 ')
#         break

#     strike = 0 
#     ball = 0 
#     answer = list(number) #임시변수에 값저장
#     for i in range(3):
#         if guess[i] == answer[i]:
#             strike += 1
#             answer[i] = 's' #스트라이크일 경우 해당 숫자를 s로 바꿔준다고? 
            
#     for i in range(3):
#         if guess[i] in answer:
#             ball += 1
#             answer[answer.index(guess[i])] = 'b'
#     print(strike,ball,answer)

    # .인덱스 부분이 이해가 잘안갔는데 지금도 이해가 안간다 
    # answer[] = 'b' 인거니까 answer에 index함수로 접근하여 guess[i]라는 값을 준다라고 해석하면 되겠다.


import random
number = str(random.randint(1,999)).zfill(3)
print(number)

while True:
    guess = input("숫자를 입력(Q:종료): ")
    # 종료문부터 만들어 볼까?
    if guess.upper() == "Q":
        break
    strike = 0
    ball = 0
    answer = list(number)
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
    print("strike : ", strike ,"ball")
    if guess == number:
        print("정답")
        break
    elif guess < number:
        print("어이 조금 더 써보지??")
    elif guess > number:
        print("어이 조금 덜 써보지?")