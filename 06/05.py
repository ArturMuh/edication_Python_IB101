n = int(input())
res = -1
while True:
    s = input()
    n += 1
    if s == "СТОП":
        break
    if res == -1 and ("кот" in s or "Кот" in s):
        res = n
        break
    print(res)
