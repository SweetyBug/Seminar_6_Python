def create_arr(data, sn):
    arr = [i for i in data.replace(' ', '')]
    s = arr[0]
    mas = []
    for i in range(1, len(arr)):
        if arr[i] not in sn and arr[i] != '(' and arr[i] != ')':
            mas.append(s)
            s = ''
            mas.append(arr[i])
        elif arr[i] == '(':
            mas.append(arr[i])
        elif arr[i] == ')':
            mas.append()
        else:
            s += arr[i]
    mas.append(s)
    print(mas)


user = '-45+21*(97 + 11)'
slovar_nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
slovar_op = ('+', '-', '/', '*', '^')
create_arr(user, slovar_nums)