import itertools

 # combinations - All the different combinations of the two iterables, order doesnt matter
 # permutations - All the different combinations of the two iterables, order matters


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ['Corey', 'Nicole']

# result = itertools.combinations(letters, 2)  # two values
# result = itertools.permutations(letters, 2)  # two values
# result = itertools.product(numbers, repeat=4)  # returns cartesian products of all elements in iterable, can repeat n times
# result = itertools.combinations_with_replacement(numbers_2, r=4)  #
# result = itertools.permutations(numbers_2, r=4)  #
# result = itertools.combinations(numbers, 2)  #
# result = itertools.combinations_with_replacement(numbers_2, 4)  # two values
# result = itertools.combinations(numbers, r=2)
# result = itertools.combinations_with_replacement(numbers, r=2)
# result = itertools.permutations(numbers, r=2)
# result = itertools.product(numbers, repeat=2)

# print(result)

count = 0
for item in result:
    count += 1
    print(item)
    print(count)