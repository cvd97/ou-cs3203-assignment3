numbers = [2,3,4,5,5]

def reverse(numbers):
    list = numbers[::-1]
    return list

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

def main():
    
    s = input()
    
    n = list(map(int,s.split()))
    
    print(sum(n))
    print(multiply(n))
    print(reverse(n))
    
main()