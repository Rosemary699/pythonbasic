for i in range(3):
    num = int(input('Enter the number: '))
    if num % 3 == 0 and num % 5 == 0:
        print('FuzzBuzz')
    elif num % 3 == 0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')

