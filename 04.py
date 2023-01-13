cnt = 0
word = 'berry'
dic = {}
with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    fruits = f.readlines()
    for fruit in fruits:        
        if fruit not in dic:
            dic[fruit] = 1
        else:
            dic[fruit] += 1

with open('04.txt', 'w', encoding = 'UTF8') as f:
    for fruit, cnt in dic.items():
        f.write(f'{fruit.strip()} {cnt}\n')