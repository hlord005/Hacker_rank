n = int(input())
ph_book = {}
for i in range(0, n):
    book = str(input()).split(' ')
    friend_name = book[0]
    ph_num = book[1]
    ph_book[friend_name] = ph_num
for i in range(0, n):
    name = input()
    if name in ph_book.keys():
        print(name + '=' + ph_book[name])
    else:
        print('Not found')
