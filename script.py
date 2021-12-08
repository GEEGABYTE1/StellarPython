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

        
        
        


test = Script()

print(test)
