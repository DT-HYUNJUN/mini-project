import json
from  pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json) # 딕셔너리

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json) # 리스트

# 이하 문제 해결을 위한 코드 작성
genid = movie['genre_ids']
lst = []

for genre in genres_list:
    for id in genid:
        if id == genre['id']:
            lst.append(genre['name'])
print(lst)