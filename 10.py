from collections import Counter

array = input('Введите текст: ')

def max_repeat(N=[]):
    c = Counter(N)
    M = c.most_common(1)[0][0]
    return M

print(max_repeat(array))
