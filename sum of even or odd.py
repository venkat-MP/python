def sum_even_odd_numbers(n):
    even_sum = 0
    odd_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum

n = 10
even_sum, odd_sum = sum_even_odd_numbers(n)
print(f"Sum of even numbers from 1 to {n}: {even_sum}")
print(f"Sum of odd numbers from 1 to {n}: {odd_sum}")