def number_classifier(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter a number: "))
result = number_classifier(num)
print(f"The number {num} is {result}.")

even = []

for i in range(1, 51):
    if i % 2 == 0:
        even.append(i)
print(even)

i = 10

while i > 0:
    print(f"Count Down:{i}")
    i-=1
