def count_bits(n):
    if n > -1:
        count_one = bin(n)
        result = count_one.count('1')
        return result
    else:
        print('try again')
