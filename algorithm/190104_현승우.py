# 문제 1
def solution(A, k):
    output = 0
    ls = sorted(A)
    for i, num in enumerate(ls):
        if num + k > ls[-1]:
            break
        elif num + k == ls[i+k]:
            output += 1
    return output

A = [1, 5, 3, 4, 2]
k = 2

print(solution(A, k))

# 문제 2
def solution(A):
    hello_num = 0
    for i in range(len(A)):
        if A[i] == 0:
            hello_num += sum(A[i+1:])
    return hello_num

A = [0, 1, 0, 1, 1]

print(solution(A))
