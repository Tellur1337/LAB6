
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

#task2
spisok1 = input("Введите список строк через пробел: ").split()
number = int(input("Введите номер позиции для новой строки: "))
newline = input("Введите новую строку: ")


def secondtaskmethod(spisok: list, number: int, line: str):
    for x in range(len(spisok)):
        if x == number:
            spisok[x] = line
            return spisok
    return "paste operation is not possible"


print({secondtaskmethod(spisok1, number, newline)})
