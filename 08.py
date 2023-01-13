import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
result = ('id', 'title', 'vote_average', 'overview', 'genre_names')
want = {}
lst = []
genid = movie['genre_ids']

sorted_genres_list = sorted(genres_list, key=lambda gen: (gen['id']))

for genre in sorted_genres_list:
    for id in genid:
        if id == genre['id']:
            lst.append(genre['name'])

movie['genre_names'] = lst

for i in result:
    for j in movie:
        if i == j:
            want[i] = movie[i]
pprint(want, indent = 2, sort_dicts = False)