i = input('What number of the fibonacci sequence would you like to know?')
# could add try except here
num = int(i)

lst = [0,1]
x = 2

if num == 1:
    print('Fibonacci sequence number 1 is 0')
else:
    while x >= 2 and x <= num:
    #sum the elements of the list
        Sum = sum(lst)
    #append the sum to the list
        lst.append(Sum)
    #delete index [0] from the list
        del lst[0]
    #how many times do you do it
        x = x +1
    print('Fibonacci sequence number',num,'is',lst[0])
