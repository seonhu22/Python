# file i/o(Input/Output)

import os

f = open('lorem.txt', 'r')
lines = f.readlines()       #   중간 엔터키가 '\n'으로 출력
f.close()

print(lines)
print(len(lines))

contents = []
for line in lines:
    sentence = line.strip()
    if len(sentence) > 0:
        contents.append(sentence)           #   중간 엔터기 '\n'이 사라짐

print(contents)
print(len(contents))

#    key = 문자, value = 숫자(line 37과 비교)
words = {}
for line in contents:
    tokens = line.split()
    for word in tokens:
        if word not in words:
            words[word] = 0
        words[word] += 1

print(words)

f = open('words.txt', 'w')
for word, count in words.items():
    f.write(f'{word} {count}\n')
f.close()

restored = {}
#   with = close를 자동으로 이행해줌
#   key = 문자, value = 문자(line 19와 비교)
#   key = 문자, value = 숫자로 하려면
#   line44를 resotred[word] = int(count)로 변경
with open('words.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        word, count = line.split()
        restored[word] = count
print(restored)

if os.path.isfile('words.txt'):
    print('file: words.txt is exist')
    os.mkdir('text')    #   폴더 이름
    #   os.makedirs(os.path.join('text', '1', '2'), exist_ok = True or False)
    #   exist_ok = True일시 pass, False일시 오류
    os.rename('words.txt', os.path.join('text', 'words.txt'))
    #   os.path.join = os간 다른 파일 디렉토리 표시법을 알아서 맞춰줌
    #   linus, mac, unix계열 = /
    #   windows 계열 = \
else:
    print('file: words.txt is not exist')