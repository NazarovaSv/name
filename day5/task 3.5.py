
train = [15, 155, 165, 12, 1, 85, 45]
for x in train:
    print(filter(lambda x: x % 15 == 0, train))


