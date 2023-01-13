cnt = 0
with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    fruits = f.readlines()
    for fruit in fruits:
        cnt += 1
print(cnt)