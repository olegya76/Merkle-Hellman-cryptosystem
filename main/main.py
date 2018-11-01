from random import randint, shuffle

def toBin(number):
    """
    Input number or string of number
    output binary number
    """
    return '{0:08b}'.format(int(number))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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

def n_generate(in_lst):
    sum = 0
    for i in in_lst:
        sum += i
    return sum + randint(2, 100)

def m_generate(n):
    pot_m = list(range(2, 11))
    shuffle(pot_m)
    for i  in pot_m:
        if(gcd(n, i) == 1):
            return i
    return -1

#ord(' ') - symbol to ascii code
#chr(int) - ascii code to symbol

if __name__ == '__main__':
    num = input('Input numper: ')
    print('In binary u num is', toBin(num))
    lst = knapsack_generate()
    print('close key list', lst)
    n = n_generate(lst)
    print('n', n)
    m = m_generate(n)
    print('m', m)
    print('gcd(n, m)=', gcd(n,m))
