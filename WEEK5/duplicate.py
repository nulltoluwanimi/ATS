from random import randint

numbers = {}
dup = []
for number in range(0, 20):
    values = randint(1, 99)
    if values not in dup:
        numbers[f'{number}'] = values
        dup.append(values)
print(numbers)

print([2000 + number for number in range(0, 20)])
# for number in range(0,20):
#     values = 2000 + number
#     id.append(values)
# print(id)
