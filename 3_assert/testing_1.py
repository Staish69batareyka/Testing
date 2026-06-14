def all_sum(data):
    result = ''
    for i in data:
        result += str(i)
    return result


mixed_numbers = [1, 2.5, 3]
result_numbers = '12.53'
assert all_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() некорректно обрабатывает смешанный список из int и float.'
)

mixed_numbers_strings = [1, 'cat', 2.5]
result_numbers_strings = '1cat2.5'
assert all_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() некорректно обрабатывает смешанный список из чисел и строк.'
)

empty = []
result_empty = ''
assert all_sum(empty) == result_empty, (
    'Функция series_sum() некорректно обрабатывает пустой список'
)