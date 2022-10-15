choice = -1
account = 100

def getInput(choices):
    while True:
        num = input()

        try:
            num = int(num)
        except:
            print('Please enter a number')
        else:
            if(num > 0 and num < choices+1):
                return num
            else:
                print('Please enter a number between 1 and ' + str(choices))

def playAgain():
    print('Would you like to play again?')
    print('1. Yes')
    print('2. No')

    choice = getInput(2)

    if(choice == 1):
        start()

def start():
    print('You are a college student who has $10,000 in debt. \nYou work part time at a movie theater and you make $15 an hour. \nThis is a day in your life. \nYou must make wise decisions and manage your finances well.')
    updateAccount(0);
    print('\nYou just woke up at 8:00 and you have a class at 8:30.')
    print('1. Get a $7 coffee and be 10 minutes late to class.')
    print('2. Go back to sleep.')
    print('3. Take the bus $3 and arrive on time.')

    choice = getInput(3)

    if(choice == 1):
        updateAccount(-7);
        print('After you get coffee, someone stops you on the street and asks you to help raise money for a cancer treatment. How much money do you want to donate?')
        print('1. $10')
        print('2. $5')
        print('3. $0')

        choice = getInput(3)

        if(choice == 1):
            updateAccount(-10)
            print('You stumble around in the darkness but before long you are lost and begin to hear strange noises.')
            print('1. Try to find shelter for the night.')
            print('2. Move towards the noises.')

            choice = getInput(2)

            if(choice == 1):
                print()
        elif(choice == 2):
            updateAccount(-5)
            print()
        elif(choice == 3):
            updateAccount(0)
        
    elif(choice == 2):
        print('Your roommate wakes you up at 10:00 and asks you if you want to get brunch. What do you say?')
        print('1. Sure, we can get Korean Barbecue for $20.')
        print('2. Let\'s get a McDonald\'s Happy Meal for $6.')
        print('3. No, I will make something here.')
        
        choice = getInput(3)

    elif(choice == 3):
        updateAccount(-3)
        print('You find a $5 bill on the ground with no one around.')
        print('1. Pocket it.')
        print('2. Leave it there.')
        
        choice = getInput(2)

def updateAccount(x):
    global account
    account = account + x
    print('Bank Account: $' + str(account))

def atSchool():
    print('Your teacher mentions an opportunity to develop a simple app for him in Python and will pay $30')
    print('1. Take it because you\'re desperate.')
    print('2. Say I have better things to do.')

    choice = getInput(2)

    if(choice == 1):
        print()
    elif(choice == 2):
        print()


start()
