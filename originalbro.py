name = input("Enter your name:")

from random import randint

a = randint(1, 9)
# print(a)

# print("yor name has : ", len(name))
# print("characters")
#
cars = [ 
        '',
        '',
        '',
        '',
        'tata',
        'maruti',
        'honda',
        'jaguar',
        'mercedes',
        'suzuki',
        'ferrari',
        'bmw',
        'hyundai',
        'audi',
        'lamborghini',
        'toyota',
        'kia',
        'mahindra',
        'bugati'
        ]

print("Wow ! " + cars[len(name) + a].upper() + " is lucky brand for you")
