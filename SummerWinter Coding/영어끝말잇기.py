def solution(n, words):
    answer = [0, 0]
    exist = [words[0]]  # 나온 단어 저장
    last = words[0][-1]  # 앞 사람 마지막 알파벳

    for w in range(1, len(words)):
        if len(words[w]) > 1 and words[w] not in exist and words[w][0] == last:
            exist.append(words[w])
            last = words[w][-1]
        else:
            num, mod = divmod(w+1, n)
            person = mod if mod != 0 else n
            turn = num + 1 if mod != 0 else num
            answer = [person, turn]
            break

    return answer