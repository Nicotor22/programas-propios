def collatz(number):
    dec=int(number%2)
    if(dec==0):
        return number//2
    else:
        return (3*number+1)

print("escriba un numero para empezar la secuencia")
try:
    num=int(input(">"))
    print(num, end=' ')
    while (num!=1):
        print(collatz(num), end=' ')
        num=collatz(num)

except ValueError:
    print("escriba un numero natural")