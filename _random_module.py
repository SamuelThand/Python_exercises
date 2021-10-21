import random

# val = random.random()
# print(val)

# uval = random.uniform(1, 10)

# print(uval)

# rval = random.randint(0, 1)

# print(rval)

# greetings = ['hello', 'hej', 'halloj', 'hejhejhej', 'hejhejhejhej']

# val = random.choice(greetings)
# print(f'{val}, mannen')

# roulette_colors = ['green', 'black', 'red']


# roulette_results = random.choices(roulette_colors, weights=[2, 18, 18], k=10)
# print(roulette_results)

deck = list(range(1, 53))

random.shuffle(deck)  #Choice kan ta samma kort flera ganger. Shuffle battre.

hand = random.sample(deck, k=5)

print(hand)