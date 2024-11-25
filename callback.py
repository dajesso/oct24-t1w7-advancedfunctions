import time

def greet(name, cb):
    print(f'Hello, {name}!')
    #time.sleep(3)
    cb()

def say_bye():
    print('Bye!!')

def shout():
    for i in range(5):
        print('FELICIS ON THE LOOSE!!!!!')

# Msin

greet("Felicis", say_bye)

greet('jessica', shout)

print('Continuing main....')



# more statements

