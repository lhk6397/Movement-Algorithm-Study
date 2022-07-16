def solution(strings, n):
    answer = []

    answer=sorted(sorted(strings), key=lambda strings: strings[n])

    return answer