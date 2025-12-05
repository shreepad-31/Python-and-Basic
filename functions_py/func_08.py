i = 0
n = int(input("Enter number of variable: "))
num = []
while n > i:
    num.append(int(input()))
    i += 1

print(sum(num))