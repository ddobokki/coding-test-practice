import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def convert2(num,d):
    str_n = ''
    while True:
        n_digit = num % d
        if n_digit == 10:
            n_digit = 'A'
        elif n_digit == 11:
            n_digit = 'B'
        elif n_digit == 12:
            n_digit = 'C'
        elif n_digit == 13:
            n_digit = 'D'
        elif n_digit == 14:
            n_digit = 'E'
        elif n_digit == 15:
            n_digit = 'F'
        else:
            n_digit = str(n_digit)

        str_n += n_digit
        num = num // d
        print(num)
        if num < d:
            break
    if num != 0:
        if num == 10:
            num = 'A'
        elif num == 11:
            num = 'B'
        elif num == 12:
            num = 'C'
        elif num == 13:
            num = 'D'
        elif num == 14:
            num = 'E'
        elif num == 15:
            num = 'F'
        else:
            num = str(num)
        str_n += str(num)
    str_n = str_n[::-1]
    return str_n
def n_nums(nn,kk):
    s = ''
    i = 0
    while len(s) < nn:
        s += convert2(i,kk)
        i += 1
    return s

def solution(n, t, m, p):

    s = n_nums(t*m,n)
    return s[p-1::m][:t].upper()
# for j in range(2,17):
#     for i in range(200):
#         a = convert(i,j)
#         b = convert2(i,j)
#         a= a.upper()
#         if a != b:
#             print(i,j, a, b )
print(convert(110,11))
print(convert2(110,11))