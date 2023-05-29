def positive_sum():
    positives = 0
    for num in numbers:
        if num > 0:
            positives += num
    return positives


def negative_sum():
    negatives = 0
    for num in numbers:
        if num < 0:
            negatives += num
    return negatives


numbers = [int(x) for x in input().split()]


negative_numbers = negative_sum()
positive_numbers = positive_sum()

print(negative_numbers)
print(positive_numbers)
if positive_numbers > abs(negative_numbers):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")