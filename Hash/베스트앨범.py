def solution(genres, plays):
    answer = []
    genres_dic = {}
    total_dic = {}
    for i in range(len(genres)):
        if genres[i] in genres_dic:
            genres_dic[genres[i]].append((plays[i], i))
            total_dic[genres[i]] += plays[i]
        else:
            genres_dic[genres[i]] = [(plays[i], i)]
            total_dic[genres[i]] = plays[i]

    for gd in genres_dic:
        genres_dic[gd].sort(key=lambda x: (-x[0], x[1]))
    total_dic = sorted(total_dic.items(), key=lambda item: item[1], reverse=True)

    for g, t in total_dic:
        answer.append(genres_dic[g][0][1])
        if len(genres_dic[g]) >= 2:
            answer.append(genres_dic[g][1][1])

    return answer

