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

def open_key_generate(lst, n, m):
    new_lst = []
    for i in lst:
        print('i', i, 'n', n, 'm', m)
        num = (i * m) % n
        new_lst.append(num)
    return new_lst

def encryption(symb, o_key):
    b_symb = list(map(int, list(toBin(ord(symb)))))
    print()
    crypt = 0
    list_crypt = [int(a*b) for a,b in zip(b_symb, o_key)]
    print('encrypt symbol' ,list_crypt)
    crypt = sum(list_crypt)
    return crypt

# TODO: переписать ф-ции Евклида и нахождения мультипликативно обратного по модулю и оъеденить их в одну


def bezout_recursive(a, b):
    '''A recursive implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a%b)
    return (x, y - (a // b) * x, g)

def multiplicative_inverse(a, b):
    ans = bezout_recursive(a, b)
    num = ans[0]
    if(num < 0):
        num += b
    if(num > b):
        num = num % b
    return num

def decryption(crypt, m, n, c_key):
    m_inverse = multiplicative_inverse(m, n)
    new_crypt = (crypt * m_inverse) % n
    b_code = [None] * 8
    k = 7
    for i in range(8):
        if(new_crypt >= c_key[k]):
            new_crypt -= c_key[k]
            b_code[k] = '1'
        else:
            b_code[k] = '0'
        k -= 1
    byte = ''.join(b_code)
    ascii_code = int(byte, 2)
    symbol =  chr(ascii_code)
    return symbol



#ord(' ') - symbol to ascii code
#chr(int) - ascii code to symbol

if __name__ == '__main__':
    symb_ctypt = input('Input symbol: ')
    print('In binary u symbol is', list(map(int, list(toBin(ord(symb_ctypt))))))
    lst = knapsack_generate()
    print('close key list', lst)
    n = n_generate(lst)
    print('n', n)
    m = m_generate(n)
    print('m', m)
    print('gcd(n, m)=', gcd(n,m))
    open_key = open_key_generate(lst, n, m)
    print('Open key:', open_key)
    crypt = encryption(symb_ctypt, open_key)
    print('crypt', crypt)
    print(bezout_recursive(41, 491))
    multiplicative_inverse_num = multiplicative_inverse(41, 491)
    print(multiplicative_inverse_num)
    symbol = decryption(crypt, m, n, lst)
    print('symbol which u send - ', symbol)
