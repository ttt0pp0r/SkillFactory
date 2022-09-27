def search(array, element):

    mid = 0
    start = 0
    end = len(array)
    error1 = array[0]
    error2 = array[-1]
    step = 0

    while start <= end:

        step = step+1
        mid = (start + end) // 2
        try:
            if element == array[mid]:
                return mid
        except IndexError:
                return False
        if element == error2:
            return False
        if element < error1:
            return False
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if len(array) // 2:
        return array[end]
    else:
        return array[start]



class Error(Exception):
    pass
class net_probelov(Error):
    pass
class letters_(Error):
    pass


while True:
    try:
        numbers = input("Введите числа через пробел: ")
        for i in numbers:
            if i.isalpha():
                raise letters_
        if " " not in numbers:
            raise net_probelov
        break
    except net_probelov:
        print("Через пробел!")
    except letters_:
        print("Только числа!")
while True:
    try:
        number = int(input("Введите любое число: "))
        break
    except ValueError:
        print("Число КАРЛ!")

numbers = numbers.split()
numbers = list(map(int, numbers))
numbers.sort()
answer = (search(numbers, number))
if answer == False:
    print("Искомое число выходит за диапазон поиска")
    print(numbers)
else:
    print(numbers)
    print("номер позиции элемента, который меньше введенного пользователем числа " + str(numbers.index(answer)))
    print("Номер позиции элемента, который больше введенного пользователем числа или равен ему " + str(numbers.index(answer) + 1))