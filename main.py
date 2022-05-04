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
