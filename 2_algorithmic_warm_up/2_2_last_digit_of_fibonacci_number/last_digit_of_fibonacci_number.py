# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    def fibonacci_number(n):
        if n <= 1:
            return n
        else:
            f = [0, 1]
            for i in range(2, n+1):
                f.append(f[i-1] + f[i-2])
            return f[-1]

    f_n = fibonacci_number(n)
    # print('f_{}={}, last={}'.format(n, f_n, int(str(f_n)[-1])))
    return int(str(f_n)[-1])




if __name__ == '__main__':
    input_n = 9
    print(last_digit_of_fibonacci_number(input_n))
