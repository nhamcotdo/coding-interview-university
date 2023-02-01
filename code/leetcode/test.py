arr = []
for _ in range(int(input())):
    arr.append(input().split())

d = dict()
for i, a in enumerate(arr):
    if not d.get(a[0]):
        d[a[0]] = int(a[1])
    else:
        d[a[0]] += int(a[1])

MAX = max(d.values())
for k, v in d.items():
    if v == MAX:
        print(k, v)