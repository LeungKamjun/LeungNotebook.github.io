import random

numbers = []
for i in range(8):
    numbers.append(random.randint(0, 100))
print(numbers)

for i in range(len(numbers)-1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)