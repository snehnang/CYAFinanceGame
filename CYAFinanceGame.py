choice = -1
account = 50

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
    global account
    change = account - 50
    if(change > 0):
        print('You made ' + str(change) + ' dollars today.')
    else:
        print('You lost ' + str(abs(change)) + ' dollars today.')
    print('Would you like to play again?')
    print('1. Yes')
    print('2. No')

    choice = getInput(2)

    if(choice == 1):
        start()
    else:
        print('Thanks for playing!')

def start():
    print('Welcome to Choose Your Own Adventure Finance Game!\n')
    print('You are a broke college student who just started working part time at a movie theater for $15 an hour. \nThis is a day in your life. You must make wise decisions and manage your finances well.')
    updateAccount(0);
    print('You just woke up at 8:00 and you have a class at 8:30 but you are really tired.')
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
        elif(choice == 2):
            updateAccount(-5)
        elif(choice == 3):
            updateAccount(0)
            scam()
        
        atSchool()
        
    elif(choice == 2):
        updateAccount(0)
        print('Your roommate wakes you up at 10:00 and asks you if you want to get brunch. What do you say?')
        print('1. Sure, we can get Korean Barbecue for $20.')
        print('2. Let\'s get a McDonald\'s Happy Meal for $6.')
        print('3. No, I will make something here.')
        
        choice = getInput(3)
        
        if(choice == 1):
            updateAccount(-20)
        elif(choice == 2):
            updateAccount(-6)
        elif(choice == 3):
            updateAccount(0)
            scam()
            
        print('After having brunch, you get a call to take some surveys for $1 each. How many surveys would you like to take?')
        print('1. Get $20 for 20 surveys')
        print('2. Get $10 for 10 surveys')
        print('3. Get $0 for 0 surveys')
        
        choice = getInput(3)
        
        if(choice == 1):
            updateAccount(20)
        elif(choice == 2):
            updateAccount(10)
        elif(choice == 3):
            updateAccount(0)

    elif(choice == 3):
        updateAccount(-3)
        print('You find a $5 bill on the ground with no one around.')
        print('1. Pocket it.')
        print('2. Leave it there.')
        
        choice = getInput(2)
        
        if(choice == 1):
            updateAccount(5)
        elif(choice == 2):
            updateAccount(0)
        
        atSchool()
    
    work()

def updateAccount(x):
    global account
    account = account + x
    print('\nBank Account: $' + str(account) + "\n")

def atSchool():
    print('At school, your teacher mentions an opportunity to develop a simple app for him in Python and will pay $30.')
    print('1. Take it because you\'re desperate.')
    print('2. Say I have better things to do.')

    choice = getInput(2)

    if(choice == 1):
        updateAccount(30)
        print('As you are coding away, you run into some technical difficulties.')
        print('1. You pay $15 for a Chegg subscription to solve your problems.')
        print('2. You get your friend to solve your problems for $9.')
        print('3. You stick with it until you figure it out yourself.')
        
        choice = getInput(3)
        
        if(choice == 1):
            updateAccount(-15)
        elif(choice == 2):
            updateAccount(-9)
        elif(choice == 3):
            updateAccount(0)
        
    elif(choice == 2):
        updateAccount(0)
        
def scam():
    print('The concert ticket you tried to purchase last week turned out to be a scam. You lost $20.')
    print('Press 1 to continue...')
    
    choice = getInput(1)
    
    if(choice == 1):
        updateAccount(-20)
    
    
def work():
    print('It\'s 6pm and your 4-hour shift at work is about to start. Do you go or not?')
    print('1. Call out sick.')
    print('2. Drag yourself to work.')
    
    choice = getInput(2)
    
    if(choice == 1):
            updateAccount(0)
    elif(choice == 2):
            updateAccount(24)
    
    playAgain()

start()
