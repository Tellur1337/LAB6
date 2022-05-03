#First task- Author - Bolnykh Sofia
s = input("Введите список строк через tab: ").split('\t')
nl = input("Введите новую строку: ")
def list(s):
    count = 1
    for x in s:
        print(count, x)
        count += 1
n = len(s)
i = n//2
if i%2==1:
    i=-1


s.insert(i, nl)

print(list(s))




