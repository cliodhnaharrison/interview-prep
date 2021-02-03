n, m = map(int, input().split())
l = [int(x) for x in input().split()]
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
happiness = 0

for i in l:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print (happiness)
