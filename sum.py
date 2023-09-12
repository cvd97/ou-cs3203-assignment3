numbers = [2,3,4,5,5]

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(numbers))

def multiply(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result
    print(result) 

print(multiply(numbers))