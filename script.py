from account import testnet_acc # Creating Account
from creating_trans import Contract # Creating/Sending Transaction

import time
from termcolor import colored


class Script:

    def __init__(self):
        print("-"*24)
        time.sleep(0.2)
        if testnet_acc.signed_in != True:
            print(colored("You have not signed in yet", 'red'))
            while testnet_acc.signed_in != True:
                print(testnet_acc)
        
        print(colored("Welcome to Stellar", 'blue'))
        time.sleep(0.2)
        print("/create_trans: to create a transaction")
        print("-"*24)
        time.sleep(0.2)
        print("/receive_trans: to check or receive transactions")
        print("-"*24)
        time.sleep(0.2)
        self.user_prompt()


    
    def user_prompt(self):
        while True:
            print("\n")
            prompt = str(input("Please enter a command"))
            
            if prompt == '/create_trans':
                time.sleep(0.1)
                print(colored('Directing you to creating a transaction ', 'blue'))
                user_trans = Contract()
                print(user_trans)
        
        
        


test = Script()

print(test)
