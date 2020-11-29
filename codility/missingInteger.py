# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A:
        return 1
    elif len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    elif 1 not in A:
        return 1

    A = sorted(set(A)) + [None]

    for i in range(len(A)):
        if A[i] == None:
            if A[i-1] <= 0:
                return 1
            else:
                return A[i-1] + 1
        if A[i] > 0:
            if A[i+1]:
                if A[i+1] > (A[i] + 1):
                    return A[i] + 1

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print(solution(x))
