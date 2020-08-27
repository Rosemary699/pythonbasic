# member1 = {'name': 'Lydia', 'dob': 'June 20 1984', 'last name': 'Chen'}
# member2 = {'name': 'Justin', 'dob': 'May 13 1984', 'last name': 'Ma'}
#
# for x in member1:
#     print(x)
#
# for x in sorted(member1.keys()):
#     print(x)
#
# for x in member1.values():
#     print(x)
#
# for x in member1:
#     print(member1[x])
#
# for x in member1.items():
#     print(x)
#
# for key, value in member1.items():
#     print('key is: ',key)
#     print('value is: ',value)

names = ['justin', 'lydia', 'kenzy']

new_name = ('tim')

name = set(names)
print(name)
if new_name not in name:
    names.append(new_name)

print(names)








