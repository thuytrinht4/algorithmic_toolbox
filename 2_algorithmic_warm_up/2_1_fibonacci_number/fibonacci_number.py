# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n
    else:
        f = [0, 1]
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
            # print('n = {}, f= {}, f(n)={}'.format(i, f, f[-1]))
        return f[-1]




if __name__ == '__main__':
    input_n = 5
    fibonacci_number(input_n)
