num = int(input("Enter a positive integer to find its sum from 0: "))

sum = 0
for i in range(1, num+1):
    sum = sum + i
    print("\nSum:", sum)