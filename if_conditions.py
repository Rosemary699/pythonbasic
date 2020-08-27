# names = ['cxy', 'justin', 'vivian', 'kenzy']
# for x in names:
#     if x == 'cxy':
#         print(x.upper())
#     elif x == 'kenzy':
#         print(x.upper())
#     else:
#         print(x.title())

# new_name = 'mike'
#
# for name in names:
#     if new_name != name:
#         print(f"{name} is not mike")
#     if new_name not in names:
#         names.append(new_name)
# print(names)


# for x in names:
#     if 'rose'!=x.lower()  :
#         print(f"{x} is not rose")
#     else:
#         names.append('rose')
# print(names)

# is_cxy_listed = ('cxy' in names)
# print(is_cxy_listed)
# print('cxy' in names)
for i in range(3):
    price = int(input('Enter your price: '))
    lanes = ['1', '2', '3']
    area = input('Enter your area: ').upper()
    if price >= 500 and area == "NYC":
        print('You can enjoy the express lane')
        for x in lanes[0]:
            print(f'{x}')

    elif 500 > price >= 400 and area == 'NJ':
        print('You can enjoy the express lane')
        for x in lanes[0]:
            print(f'{x}')
    else:
        diff = 400 - price
        print(f'Buy {diff} more, then you can enjoy the fast lane.')
        for x in lanes[1:]:
            print(f'{x}')

