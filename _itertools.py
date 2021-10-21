import itertools

# counter = itertools.count()
# counter = itertools.cycle((1, 0))
# counter = itertools.repeat(2, times=3)

# squares = map(pow, range(10), itertools.repeat(2))  # takes function, passes iterables from values as arguments to the function, until shortest list of arguments have run out

squares = itertools.starmap(pow, [(0, 2), (2, 6), (4, 5), (7, 4), (3, 3)])  # takes function, passes iterables from lsits of tuples to the function

print(list(squares))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# print(itertools.count)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# data = [100, 200, 300, 400]
#
# daily_data = list(itertools.zip_longest(range(10), data))
#
# print(daily_data)
#
# for count, data in daily_data:
#     print(count, data)
