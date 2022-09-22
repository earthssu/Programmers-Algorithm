import math

def solution(n, k):
    answer = []
    people = [i for i in range(1, n+1)]
    while True:
        factorial = math.factorial(n)
        div, mod = divmod(k, factorial // n)
        if mod == 0:
            answer.append(people[div-1])
            people.remove(people[div-1])
            answer.extend(sorted(people, reverse=True))
            break
        elif mod == 1:
            answer.append(people[div])
            people.remove(people[div])
            answer.extend(sorted(people))
            break
        else:
            answer.append(people[div])
            people.remove(people[div])
            n = n - 1
            k = mod

    return answer