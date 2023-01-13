cnt = 0
word = 'berry'
fruits_list = []
with open('data/fruits.txt', 'r', encoding = 'UTF8') as f:
    fruits = f.readlines()
    for fruit in fruits:
        if word == fruit[-6:-1]:
            if fruit not in fruits_list:
                fruits_list.append(fruit)
                cnt += 1
    cnt_str = str(cnt) + '\n'

with open('03.txt', 'w', encoding = 'UTF8') as f:
    f.writelines(cnt_str)
    f.writelines(fruits_list)