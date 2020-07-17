n = input("Enter a number up to which you'd like a list of prime numbers")
try:
    n = int(n)
except:
    print('Please enter an integer as digits')

a_range = range(2,n)
lst = list(a_range)
prime_lst = []

while True:
    if len(lst) == 0:
        break
    else:
        p = lst[0]
        prime_lst.append(p)
        lst = list(i for i in lst if i % p)

print(prime_lst)
