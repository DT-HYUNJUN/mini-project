import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
result = ('id', 'title', 'vote_average', 'overview', 'genre_ids')

want = {} # 답을 적을 공간

for i in result:  # i = id
    for j in movie: # j = adult
        if i == j:
            want[i] = movie[i]
pprint(want, sort_dicts = False)