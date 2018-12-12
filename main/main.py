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
    print('lst', 'n', 'm', lst, n, m)
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
    print('decryption')
    m_inverse = multiplicative_inverse(m, n)
    print('m_inverse', m_inverse)
    new_crypt = (crypt * m_inverse) % n
    print('new_crypt', new_crypt)
    b_code = [None] * 8
    k = 7
    for i in range(8):
        if(new_crypt >= c_key[k]):
            new_crypt -= c_key[k]
            b_code[k] = '1'
        else:
            b_code[k] = '0'
        k -= 1
    print('b_code', b_code)
    byte = ''.join(b_code)
    ascii_code = int(byte, 2)
    symbol =  chr(ascii_code)
    print('symbol', symbol)
    return symbol

def close_key_button_click():
    lst = knapsack_generate()
    close_key_text.set(lst)

def n_button_click(close_key_entry):
    lst = list(map(int, close_key_entry.get().split()))
    n = n_generate(lst)
    n_text.set(n)

def m_button_click(n_entry):
    n = int(n_entry.get())
    m = m_generate(n)
    m_text.set(m)

def gcd_n_m_button_click(n_entry, m_entry):
    print(type(n_entry))
    n = n_entry.get()
    m = m_entry.get()
    print('n', 'm', n, m)
    try:
        n = int(n)
        m = int(m)
        gcd_n_m_text.set(gcd(int(n),int(m)))
    except:
        gcd_n_m_text.set(-1)


def open_key_button_click(close_key_entry, n_entry, m_entry):
    lst = list(map(int, close_key_entry.get().split()))
    n = int(n_entry.get())
    m = int(m_entry.get())
    open_key = open_key_generate(lst, n, m)
    open_key_text.set(open_key)

def symbol_button_click(symbol_entry, open_key_entry):
    symbol = symbol_entry.get()
    b_symb = list(map(int, list(toBin(ord(symbol)))))
    symbol_bin_text.set(b_symb)
    open_key = list(map(int, open_key_entry.get().split()))
    crypt = encryption(symbol, open_key)
    crypt_text.set(crypt)

def symbol_bin_button_click():
    n_text.set(n)

def crypt_button_click(crypt_entry ,n_entry, m_entry, close_key_entry):
    crypt = int(crypt_entry.get())
    n = int(n_entry.get())
    m = int(m_entry.get())
    print('on button')
    print('n', 'm', n, m)
    m_inverse = multiplicative_inverse(m, n)
    print('m_inverse', m_inverse)
    opposite_text.set(m_inverse)
    new_crypt = (crypt * m_inverse) % n
    new_crypt_text.set(new_crypt)
    lst = list(map(int, close_key_entry.get().split()))
    b_code = [None] * 8
    k = 7
    for i in range(8):
        if(new_crypt >= lst[k]):
            new_crypt -= lst[k]
            b_code[k] = '1'
        else:
            b_code[k] = '0'
        k -= 1
    print('b_code', b_code)
    new_bin_text.set(b_code)
    byte = ''.join(b_code)
    ascii_code = int(byte, 2)
    symbol =  chr(ascii_code)
    print('symbol', symbol)
    symbol = decryption(crypt, m, n, lst)
    print('symbol', symbol)
    new_symbol_text.set(symbol)


def opposite_button_click():
    n_text.set(n)

def new_crypt_button_click():
    n_text.set(n)

def new_bin_button_click():
    n_text.set(n)

def mainWindow():

    main_window.title('Криптосистема Меркля-Хеллмана')
    main_window.geometry('660x380')

    #Закрытый ключ: подпись и поле
    close_key_label = Label(None, text = 'Супервозрастающий рюкзак: ', font = 14)
    close_key_label.place(x=10, y=10)
    # close_key_text = StringVar()
    close_key_entry = Entry(None, textvariable = close_key_text, width = 25)
    close_key_entry.configure(state = 'readonly')
    close_key_entry.place(x=270, y=10)
    #close_key_text.set(lst) #Сгенерировать
    close_key_button = Button(None, text='Сгенерировать', width=15, height= 1, command = close_key_button_click)
    close_key_button.place(x=500, y=5)

    #N подпись и поле
    n_label = Label(None, text = 'N = ', font = 14)
    n_label.place(x=10, y=40)
    # n_text = StringVar()
    n_entry = Entry(None, textvariable = n_text, width = 5)
    n_entry.configure(state = 'readonly')
    n_entry.place(x=45, y=40)
    #n_text.set(n)
    n_button = Button(None, text='Сгенерировать', width=15, height= 1, command = ( lambda:  n_button_click(close_key_entry)))
    n_button.place(x=500, y=35)

    #M подпись и поле
    m_label = Label(None, text = 'M = ', font = 14)
    m_label.place(x=10, y=70)
    # m_text = StringVar()
    m_entry = Entry(None, textvariable = m_text,  width = 5)
    m_entry.configure(state = 'readonly')
    m_entry.place(x=45, y=70)
    # m_text.set(m)
    m_button = Button(None, text='Сгенерировать', width=15, height= 1, command = ( lambda:  m_button_click(n_entry)))
    m_button.place(x=500, y=65)

    #gcd(n,m) подпись и поле
    gcd_n_m_label = Label(None, text = 'gcd(n, m) = ', font = 14)
    gcd_n_m_label.place(x=10, y=100)
    # gcd_n_m_text = StringVar()
    gcd_n_m_entry = Entry(None, textvariable = gcd_n_m_text,  width = 5)
    gcd_n_m_entry.configure(state = 'readonly')
    gcd_n_m_entry.place(x=100, y=100)
    # gcd_n_m_text.set(gcd(n,m))
    gcd_n_m_button = Button(None, text='Проверить n и m', width=15, height= 1, command = ( lambda: gcd_n_m_button_click(n_entry, m_entry)))
    gcd_n_m_button.place(x=500, y=95)

    #Открытый ключ: подпись и поле
    open_key_label = Label(None, text = 'Открытый ключ: ', font = 14)
    open_key_label.place(x=10, y=130)
    # open_key_text = StringVar()
    open_key_entry = Entry(None, textvariable = open_key_text, width = 27)
    open_key_entry.configure(state = 'readonly')
    open_key_entry.place(x=160, y=130)
    # open_key_text.set(open_key)
    open_key_button = Button(None, text='Сгенерировать', width=15, height= 1, command = ( lambda: open_key_button_click(close_key_entry, n_entry, m_entry)))
    open_key_button.place(x=500, y=125)

    #Символ: подпись и поле
    symbol_label = Label(None, text = 'Введите символ, который будем передавать: ', font = 14)
    symbol_label.place(x=10, y=160)
    # symbol_text = StringVar()
    symbol_entry = Entry(None, textvariable = symbol_text,  width = 5)
    # symbol_entry.configure(state = 'readonly')
    symbol_entry.place(x=400, y=160)
    #symbol_text.set(m)
    symbol_button = Button(None, text='Зашифровать', width=15, height= 1, command = ( lambda: symbol_button_click(symbol_entry, open_key_entry)))
    symbol_button.place(x=500, y=155)

    #Символ в бонарном видк: подпись и поле
    symbol_bin_label = Label(None, text = 'Символ в бинарном виде: ', font = 14)
    symbol_bin_label.place(x=10, y=190)
    # symbol_bin_text = StringVar()
    symbol_bin_entry = Entry(None, textvariable = symbol_bin_text, width = 18)
    symbol_bin_entry.configure(state = 'readonly')
    symbol_bin_entry.place(x=240, y=190)
    # symbol_bin_text.set(list(map(int, list(toBin(ord(symb_ctypt))))))
    # symbol_bin_button = Button(None, text='Преобразовать: ', width=15, height= 1, command = symbol_bin_button_click)
    # symbol_bin_button.place(x=500, y=185)

    #Криптограма: подпись и поле
    crypt_label = Label(None, text = 'Зашифрованный символ: ', font = 14)
    crypt_label.place(x=10, y=220)
    # crypt_text = StringVar()
    crypt_entry = Entry(None, textvariable = crypt_text,  width = 5)
    crypt_entry.configure(state = 'readonly')
    crypt_entry.place(x=240, y=220)
    # crypt_text.set(crypt)
    crypt_button = Button(None, text='Разшифровать', width=15, height= 1, command = ( lambda: crypt_button_click(crypt_entry, n_entry, m_entry, close_key_entry)))
    crypt_button.place(x=500, y=215)

    #Мультипликативно обратное m по модулю n: подпись и поле
    opposite_label = Label(None, text = 'Мультипликативное обратное m по модулю n: ', font = 14)
    opposite_label.place(x=10, y=250)
    # opposite_text = StringVar()
    opposite_entry = Entry(None, textvariable = opposite_text,  width = 5)
    opposite_entry.configure(state = 'readonly')
    opposite_entry.place(x=410, y=250)
    # opposite_text.set(crypt)
    # opposite_button = Button(None, text='Преобразовать: ', width=15, height= 1, command = opposite_button_click)
    # opposite_button.place(x=500, y=245)


    #Преобразованая криптограма: подпись и поле
    new_crypt_label = Label(None, text = 'Преобразованый полученный символ (C*m^-l(mod n)): ', font = 14)
    new_crypt_label.place(x=10, y=280)
    # new_crypt_text = StringVar()
    new_crypt_entry = Entry(None, textvariable = new_crypt_text,  width = 5)
    new_crypt_entry.configure(state = 'readonly')
    new_crypt_entry.place(x=480, y=280)
    m_inverse = multiplicative_inverse(m, n)
    # new_crypt_text.set((crypt * m_inverse) % n)
    # new_crypt_button = Button(None, text='Преобразовать: ', width=15, height= 1, command = new_crypt_button_click)
    # new_crypt_button.place(x=500, y=275)

    #Решение задачи о рюкзаках с криптограмой: подпись и поле
    new_bin_label = Label(None, text = 'Решение задачи о рюкзаках: ', font = 14)
    new_bin_label.place(x=10, y=310)
    # new_bin_text = StringVar()
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
    # new_bin_text.set(b_code)
    # new_bin_button = Button(None, text='Решить: ', width=15, height= 1, command = new_bin_button_click)
    # new_bin_button.place(x=500, y=305)

    #Разшифрованый символ: подпись и поле
    new_symbol_label = Label(None, text = 'Разшифрованый символ: ', font = 14)
    new_symbol_label.place(x=10, y=340)
    # new_symbol_text = StringVar()
    new_symbol_entry = Entry(None, textvariable = new_symbol_text,  width = 5)
    new_symbol_entry.configure(state = 'readonly')
    new_symbol_entry.place(x=240, y=340)
    # new_symbol_text.set(symbol)
    # new_bin_button = Button(None, text='Символ', width=15, height= 1, command = new_bin_button_click)
    # new_bin_button.place(x=500, y=335)

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

    main_window = Tk()
    close_key_text = StringVar()
    n_text = StringVar()
    m_text = StringVar()
    gcd_n_m_text = StringVar()
    open_key_text = StringVar()
    symbol_text = StringVar()
    symbol_bin_text = StringVar()
    crypt_text = StringVar()
    opposite_text = StringVar()
    new_crypt_text = StringVar()
    new_bin_text = StringVar()
    new_symbol_text = StringVar()

    mainWindow()
