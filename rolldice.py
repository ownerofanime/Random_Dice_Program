import random

while True:
    number = str(input('Would you like to roll your dice (yes/no?)  ')).lower()
    if number == 'yes':
        random_int = int(random.randint(1,6))
        if random_int == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif random_int == 2:
            print("[-----]")
            print("[  0  ]")
            print("[     ]")
            print("[  0  ]")
            print("[-----]")
        elif random_int == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif random_int == 4:
            print("[-----]")
            print("[ 0 0 ]")
            print("[     ]")
            print("[ 0 0 ]")
            print("[-----]")
        elif random_int == 5:
            print("[-----]")
            print("[ 0 0 ]")
            print("[  0  ]")
            print("[ 0 0 ]")
            print("[-----]")
        elif random_int == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
    elif number == 'no':
        print('thank you for playing!')
        break
    else:
        print('error')
