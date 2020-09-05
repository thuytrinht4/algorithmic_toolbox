# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    else:
        if numbers[0] > numbers[1]:
            big1 = numbers[0]
            big2 = numbers[1]
        else:
            big1 = numbers[1]
            big2 = numbers[0]

        for i in range(2, len(numbers)):
            if numbers[i] > big1:
                big2 = big1
                big1 = numbers[i]
            elif numbers[i] > big2:
                big2 = numbers[i]

        return big1 * big2


if __name__ == '__main__':
    # n = int(input())
    # input_numbers = list(map(int, input().split()))
    # assert len(input_numbers) == n
    # print(max_pairwise_product(input_numbers))

    # print(max_pairwise_product([1, 2, 3]))

    n = 10
    n = 10**5
    A = [0] * n
    # print(max_pairwise_product_naive(A))
    print(max_pairwise_product(A))
