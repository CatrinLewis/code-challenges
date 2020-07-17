start = input('At what number would you like fizzbuzz to start?')
try:
    s = int(start)
except:
    print('I asked for a number!')

top = input('Up to what number would you like fizzbuzz to go?')
try:
    t = int(top)+1
except:
    print('I asked for a number!')

inc = input('By how many numbers would you like to go up each time?')
try:
    i = int(inc)
except:
    print('I asked for a number!')

x = range(s,t,i)
for n in x:
    if n%3 == 0 and n%5 == 0:
        print('FizzBuzz')
    elif n%3 == 0:
        print('Fizz')
    elif n%5 == 0:
        print('Buzz')
    else:
        print(n)
