member1 = {'name': 'Lydia', 'dob': 'June 20 1984'}
member2 = {'name': 'Justin', 'dob': 'May 13 1984'}

print(f"The first family member is {member1['name']}, and her date of birth is {member1['dob']}")
print(f"Next family mamber is {member2['name']}, and his date of birth is {member2['dob']}")

member2['name'] = 'Kenzy'
member2['dob'] = 'Jan 03 2019'
print(f"Next family mamber is {member2['name']}, and his date of birth is {member2['dob']}")

member1['nationality']='China'
member2['nationality']='The United States'
print(f"The first family member is {member1['name']}, she is from {member1['nationality']}, and her date of birth is {member1['dob']}")
print(f"Next family mamber is {member2['name']}, he is from {member2['nationality']},and his date of birth is {member2['dob']}")

print(sorted(member1))

del member1['nationality']
print(member1)