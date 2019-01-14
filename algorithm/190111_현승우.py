# main
def solution(n, queries):    
    ls = [0] * n
    for query in queries:
        value = query[-1]
        keys = query[:-1]
        for key in keys:
            ls[key-1] += value
    return max(ls)
