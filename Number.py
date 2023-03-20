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
    for x in range(10):
        print(x)
time = f'Greetings {name}. It is now {time_now}'
print(time)