from random import randint, shuffle
from tkinter import *

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

def mainWindow():
    main_window = Tk()
    main_window.title('Криптосистема Меркля-Хеллмана')
    main_window.geometry('640x380')

    #Закрытый ключ: подпись и поле
    close_key_label = Label(None, text = 'Супервозрастающий рюкзак: ', font = 14)
    close_key_label.place(x=10, y=10)
    close_key_text = StringVar()
    close_key_entry = Entry(None, textvariable = close_key_text, width = 25)
    close_key_entry.configure(state = 'readonly')
    close_key_entry.place(x=270, y=10)
    close_key_text.set(lst)

    #N подпись и поле
    n_label = Label(None, text = 'N: ', font = 14)
    n_label.place(x=10, y=40)
    n_text = StringVar()
    n_entry = Entry(None, textvariable = n_text, width = 5)
    n_entry.configure(state = 'readonly')
    n_entry.place(x=40, y=40)
    n_text.set(n)

    #M подпись и поле
    m_label = Label(None, text = 'M: ', font = 14)
    m_label.place(x=10, y=70)
    m_text = StringVar()
    m_entry = Entry(None, textvariable = m_text,  width = 5)
    m_entry.configure(state = 'readonly')
    m_entry.place(x=40, y=70)
    m_text.set(m)

    #gcd(n,m) подпись и поле
    gcd_n_m_label = Label(None, text = 'gcd(n, m): ', font = 14)
    gcd_n_m_label.place(x=10, y=100)
    gcd_n_m_text = StringVar()
    gcd_n_m_entry = Entry(None, textvariable = gcd_n_m_text,  width = 5)
    gcd_n_m_entry.configure(state = 'readonly')
    gcd_n_m_entry.place(x=100, y=100)
    gcd_n_m_text.set(gcd(n,m))

    #Открытый ключ: подпись и поле
    open_key_label = Label(None, text = 'Открытый ключ: ', font = 14)
    open_key_label.place(x=10, y=130)
    open_key_text = StringVar()
    open_key_entry = Entry(None, textvariable = open_key_text, width = 25)
    open_key_entry.configure(state = 'readonly')
    open_key_entry.place(x=160, y=130)
    open_key_text.set(open_key)

    #Символ: подпись и поле
    symbol_label = Label(None, text = 'Введите символ, который будем передавать: ', font = 14)
    symbol_label.place(x=10, y=160)
    symbol_text = StringVar()
    symbol_entry = Entry(None, textvariable = symbol_text,  width = 5)
    # symbol_entry.configure(state = 'readonly')
    symbol_entry.place(x=400, y=160)
    #symbol_text.set(m)

    #Символ в бонарном видк: подпись и поле
    symbol_bin_label = Label(None, text = 'Символ в бинарном виде: ', font = 14)
    symbol_bin_label.place(x=10, y=190)
    symbol_bin_text = StringVar()
    symbol_bin_entry = Entry(None, textvariable = symbol_bin_text, width = 18)
    symbol_bin_entry.configure(state = 'readonly')
    symbol_bin_entry.place(x=240, y=190)
    symbol_bin_text.set(list(map(int, list(toBin(ord(symb_ctypt))))))

    #Криптограма: подпись и поле
    crypt_label = Label(None, text = 'Зашифрованный символ: ', font = 14)
    crypt_label.place(x=10, y=220)
    crypt_text = StringVar()
    crypt_entry = Entry(None, textvariable = crypt_text,  width = 5)
    crypt_entry.configure(state = 'readonly')
    crypt_entry.place(x=240, y=220)
    crypt_text.set(crypt)

    #Мультипликативно обратное m по модулю n: подпись и поле
    opposite_label = Label(None, text = 'Мультипликативное обратное m по модулю n: ', font = 14)
    opposite_label.place(x=10, y=250)
    opposite_text = StringVar()
    opposite_entry = Entry(None, textvariable = opposite_text,  width = 5)
    opposite_entry.configure(state = 'readonly')
    opposite_entry.place(x=410, y=250)
    opposite_text.set(crypt)

    #Преобразованая криптограма: подпись и поле
    new_crypt_label = Label(None, text = 'Преобразованый полученный символ (C*m^-l(mod n)): ', font = 14)
    new_crypt_label.place(x=10, y=280)
    new_crypt_text = StringVar()
    new_crypt_entry = Entry(None, textvariable = new_crypt_text,  width = 5)
    new_crypt_entry.configure(state = 'readonly')
    new_crypt_entry.place(x=480, y=280)
    m_inverse = multiplicative_inverse(m, n)
    new_crypt_text.set((crypt * m_inverse) % n)

    #Решение задачи о рюкзаках с криптограммой: подпись и поле
    new_bin_label = Label(None, text = 'Решение задачи о рюкзаках: ', font = 14)
    new_bin_label.place(x=10, y=310)
    new_bin_text = StringVar()
    new_bin_entry = Entry(None, textvariable = new_bin_text, width = 18)
    new_bin_entry.configure(state = 'readonly')
    new_bin_entry.place(x=270, y=310)
    m_inverse = multiplicative_inverse(m, n)
    new_crypt = (crypt * m_inverse) % n
    b_code = [None] * 8
    k = 7
    for i in range(8):
        if(new_crypt >= lst[k]):
            new_crypt -= lst[k]
            b_code[k] = '1'
        else:
            b_code[k] = '0'
        k -= 1
    byte = ''.join(b_code)
    new_bin_text.set(b_code)

    #Разшифрованый символ: подпись и поле
    new_symbol_label = Label(None, text = 'Разшифрованый символ: ', font = 14)
    new_symbol_label.place(x=10, y=340)
    new_symbol_text = StringVar()
    new_symbol_entry = Entry(None, textvariable = new_symbol_text,  width = 5)
    new_symbol_entry.configure(state = 'readonly')
    new_symbol_entry.place(x=240, y=340)
    new_symbol_text.set(symbol)


    main_window.mainloop()

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
    mainWindow()
