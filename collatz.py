print("enter the number")
num = int(input())

def collatz(nbr):
    if nbr % 2 == 0:
        return num / 2
    else:
        return nbr * 3 + 1

result = collatz(num)



print(result)
