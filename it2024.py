z = input()
d = {
    '0': 'O',
    '1': 'I',
    '2': 'Z',
    '3': 'E',
    '4': '!',
    '5': 'S',
    '6': 'b',
    '7': 'J',
    '8': '#',
    '9': 'P',
}
try:
    z = str(int(z))
    if len(z) != 7:
        print('WRONG')
        exit()
    z += z[0]
    z = z[::-1]
    answer = ""
    for i in z:
        answer += d[i]
    print(answer)
except ValueError:
    print('WRONG')