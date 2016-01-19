cache = []

with open("cache.txt") as f:
    cache = f.readlines()

for index in range(len(cache)):
    print(cache[index])
