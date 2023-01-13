import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
result = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
lst = [{}] * 20 # len(movies_list)
dic = {}

for i in movies_list: # i 
    for j in result:
        if j in i:
            dic[j] = i[j]
    lst = dic
    pprint(lst, sort_dicts=False)