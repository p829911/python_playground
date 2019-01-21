# main
def solution(data, queries):
    ls = []
    for i,j in queries:
        ls.append(sum(data[i-1:j]))

    return ls

# sub
def solution(n):
    total = 10
    
    if n == 1:
        return total
    
    for i in range(11, 10**n):
        ls = list(str(i))
        l = len(ls)
        if l % 2 == 1:
            a = int((l-1)/2)
        else:
            a = int(l/2)
      
        if ls[:a] == ls[-a:]:
            total += 1
            
    return total
