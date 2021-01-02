# 조건문

# if [bool로 표현되는 expression]

"""
s = input()
if s == "hello":
    print("world!")
elif len(s) == 5:
    print(5)
else:
    print("np")
"""

# C언어 삼항 연산자

# a < b ? a : b
# 조건식 ? 참일때의 식 : 거짓일떄의 식

# s = a < b ? a : b

'''
word = "apple"

word = 'yes' if len(word) == 5 else 'no'
print(word)
'''

# true if condition else false

#반복문

#while은 조건을 만족하는 동안 반복
'''
c = input('>>> ')
while len(c) == 0:
    c = input('>>> ')

print(c)

while True:
    c = input('>>> ')
    print(f'Your message: "{c}"')
'''

# list, tuple, dict, set, str, ... -> iterable(반복가능)
# for은 iterable을 순회하는 반복
'''
numbers = [3, 5, 6, 7, 2, 1, 9]
for item in numbers:
    print(item)
'''
# 안에 있는 요소를 한바퀴 순회
'''
for ch in 'hello world!':
    print(ch)
'''
# 문자열도 한개씩 순회
'''
for i in range(100):
    print(i)
# 0부터 100까지
for i in range(1, 100):
    print(i)
# 1부터 100까지
for i in range(1, 100, 2):
    print(i)
#시작 기준(홀수, 짝수)만
'''

# for i in range(10000):
#     if '8' in str(i):
#         print(i)

# numbers = list(range(1, 101))
# for x in numbers:
#     if x % 3 == 0 or x % 5 == 0:
#         numbers.remove(x)
# print(numbers)
# #오류, 리스트에서 삭제는 위험
# i = 0
# while i < len(numbers):
#     x = numbers[i]
#     if x % 3 == 0 or x % 5 == 0:
#         numbers.remove(x)
#     else:
#         i += 1
# print(numbers)
#
# numbers = list(range(1, 101))
# filtered = []
# for x in numbers:
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     filtered.append(x)
# print(filtered)

# numbers = list(range(1, 101))
# filtered = [x for x in numbers if not(x % 3 == 0 or x % 5 == 0)]
# #numbers의 숫자를 순차적으로 불러와 filtered에 입력
# amazing = [x if x % 3 != 0 else 0 for x in numbers]
# #list comprehension
#
# print(numbers)
# print(filtered)
# print(amazing)

# words = ['hello', 'world', 'apple', 'banana', 'kiwi']
# types = [int, str, list, dict, bool]
# # 두개를 묶어서 출력
# # for i in range(len(words)):
# #     word = words[i]
# #     t = types[i]
# #     print(word, t)
# # 묶을게 많다면?(두 리스트의 길이가 같을때만 가능)
# # zip()함수
# for word, t in zip(words, types):
#     print(word, t)
# for word in enumerate(words):
#     print(word)
# for문시 인덱스 위치 가져오는 법(enumerate)

# a = 12345
# b = 67890
# a, b = b, a
# # 길이가 안맞을시 안됨
# print(a, b)
#
# trans_pair = [
#     ('hello', '안녕', '123'),
#     ('world', '세상', '456'),
#     ('apple', '사과', '789'),
# ]
#
# for eng, kor in trans_pair:
#     print(eng, kor)
# 받아오는 인자와 요청하는 인자의 갯수가 같아야함
# for end, kor & print(eng, kor) == trans_pair('...','...')
# 2개 == 2개, 3개 == 3개

# 함수

# def add(x, y):
#     return x + y
#
# def print_awesome(text):
#     print('============')
#     print(f'>>> {text} <<<')
#     print('============')
#
# print_awesome('hello word!')

# def clap():
#     print('clap clap clap')
#
# clap()

# def gen_ran_num():
#     import random
#     num = random.randint(0, 100)
#     return num
#
# print(gen_ran_num())

# def dice(n=6):
#     import random
#     number = random.randint(1, n)
#     return number

# print(dice())
# print(dice)
# # dice의 함수 주소를 표시함
#
# ex = dice
# print(ex())
# # ex에 dice함수 주소를 가져옴
# print(ex)
# # ex에 dicd함수 주소를 표시함
# print(ex(100))
# # dice함수에 100인자를 입력
#
# ex = dice(100)
# print(ex())
# 오류
# 위 상황처럼 하고싶으면

# def exx(func):
#     return func(100)
#
# print(exx(dice))
# # 함수를 인자로 넘겨서 해결

# def make_dice(n=6):
#     #1부터 n사이의 값이 나오는 주사위를 굴리는 함수를 반환
#     # def roll_dice_n():
#     #     import random
#     #     return random.randint(1, n)
#     #
#     # return roll_dice_n
#     import random
#     return lambda: random.randint(1, n)
# #
# dice20 = make_dice(20)
# print(dice20())

# 위 roll_dice_n()함수는 굳이 이름이 필요 없음
# 익명으로 잠시만 쓸수 있게도 가능(이름 구상 필요 X) -> lambda()함수

# def add(x, y):
#     return x + y
#
# add_lambda = lambda x, y: x + y
# print(add_lambda(1, 3))
#둘이 같은 함수

# def add(x,y):
#     return x+y
#
# numbers = [1,2,3,4,5,6]
# repeat_func = [lambda x: str(x) * n for n in numbers]
#
# print(repeat_func[3]('hello'))

# map()함수
# map(func, iterable)
# c = input()     # 1 2 3 4 5
# inputs = c.split()
# print(inputs)
# 문자열로 나옴, 숫자로 나오기 위해선
# c = input()
# inputs = c.split()
# inputs = map(int, inputs)
# # inputs에 있는걸 int로 모두변환
# print(inputs)
# 이렇게 하면 주소만 표기해줌
# map()함수는 list 반환x, iterable 반환 O
# 리스트로 표현하기 위해서는 map()함수를 list()로 한번 감싸줘야함
# c = input()
# inputs = c.split()
# inputs = list(map(int, inputs))
# print(inputs)