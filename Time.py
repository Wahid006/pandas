import time
time_now = time.ctime()
print('Greetings')
name = input("What is your name? :  ")
if name == 'Rehab':
    for x in range(10):
        if x % 2 != 0:
        
            print(x)
elif name == 'Alif':
    for x in range(10):
        if x % 2 == 0:
    
         print(x)
    
else:
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
time = f'Greetings {name}. It is now {time_now}'
print(time)