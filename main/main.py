from random import randint

def toBin(number):
    """
    Input number or string of number
    output binary number
    """
    return '{0:08b}'.format(int(number))

def knapsack_generate():
    """return list - overgrowth knapsack"""
    lst = [1]
    sum = 1
    random_int = randint(1,10)
    sum += random_int
    lst.append(1 + random_int)
    for i in range(6):
        random_int = randint(1,10)
        next_int = sum + random_int
        sum += next_int
        lst.append(next_int)

    return lst

#ord(' ') - symbol to ascii code
#chr(int) - ascii code to symbol

if __name__ == '__main__':
    num = input('Input numper: ')
    print('In binary u num is', toBin(num))
    print(knapsack_generate())
