import itertools
import operator

# def lt_2(n):
#     if n < 2:
#         return True
#     else:
#         return False

numbers = [0, 1, 2, 3, 2, 1, 0]
numbers_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ['Corey', 'Nicole']

letters = ['a', 'b', 'c', 'd']

# selectors = [True, True, False, True]

# result = itertools.compress(letters, selectors)
# result = filter(lt_2, numbers_2)
# result = itertools.dropwhile(lt_2, numbers)
# result = itertools.takewhile(lt_2, numbers)
# result = itertools.accumulate(numbers)  # Fibonacci?
# result = itertools.accumulate(numbers, operator.mul)

for item in result:
    print(item)

# combined = itertools.chain(letters, numbers, names)  #Combining lists for iteration

# results = itertools.islice(range(10), 2, 5, 2)  #Slicing iterables with startingpoint, stoppingpoint, stepping

# with open('testlog.log', 'r') as f_hand:
#     # print(f_hand.read())
#     header = itertools.islice(f_hand.read(), )
#     # print(header)
#     for line in header:
#          print(line, end='')



