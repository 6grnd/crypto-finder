#!usr/bin/python3
# This program scrapes coindesk.com and takes the data on every coin to make it
# more easy to acces it through a simple python terminal interface. 
import sys  # To exit program
from connectToCurrencies import currencyScraper  # Module with class 

options = """
\nOptions include but are not limited to bitcoin, xrp, ethereum,
stellar, chainlink, tether, litecoin, cardano, cosmos, etc... 

but remember you can try any coin you wish that's available in coindesk.\n"""


def choose_coin_to_manage(): 
    #Dedicated to collect input from user, what coin they want to manage
    chosen_coin = input("\n | choose crypto | (e) examples | (q) quit |\n\n ===> ").lower().strip() 
    return chosen_coin 

def instantiate_coin(): 
    #Instantiate the class with user input
    chosen_coin = choose_coin_to_manage()
    if chosen_coin not in ["e", "q", ""]:  
        try:  
            return currencyScraper(chosen_coin)
        except: 
            print("\nnot a valid choice\n") 
            control_flow()

    elif chosen_coin == "e": 
        print(options)
        control_flow()

    elif chosen_coin == "q": 
        sys.exit(0) 
    else: 
        print("Input is not an option")
        control_flow()


def control_flow(): 
    # Controls the main control flow of the program (like a tv remote)
    chosen_coin = instantiate_coin()
    where = int(input(

f"""
What do you want to do with {chosen_coin.getName()}\n
1) Get information on coin. 
2) Get current price
3) Get URL for complete coin information.\n
(1, 2, 3) 

====> """))

    # Control flow on where to proceed.
    if where == 1: 
        print(chosen_coin)
        print(chosen_coin.getInfo())
        do_another_task()
    elif where == 2: 
        print(chosen_coin.getPrice())
        do_another_task()
    elif where == 3: 
        print(chosen_coin.getURL())
        do_another_task()
    else: 
        print("Not an option, let's restart") 
        control_flow()


def do_another_task(): 
    # Dedicated to run after doing something to ask if users needs something else. 
    next_activity = input("Need something else? (y/n) => ").lower().strip() 
    if next_activity == "y":
        control_flow()
    elif next_activity == "n": 
        print("Ok, thanks for using.") 
        sys.exit(0)
    else: 
        print("Didn't quite understand input") 
        do_another_task()


    