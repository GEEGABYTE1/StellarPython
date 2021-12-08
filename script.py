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
            print(testnet_acc)
        else:
            print(colored("Welcome to Stellar", 'blue'))
            time.sleep(0.2)
            print("/create_trans: ")

            
