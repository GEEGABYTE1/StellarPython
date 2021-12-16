from account import testnet_acc # Creating Account
from creating_trans import Contract # Creating/Sending Transaction
from account import db # Database
from asset import asset #AstroDollar and Tokenizing
from receiving_trans import running


import time
from termcolor import colored

all_accounts = db.find({})

class Script:

    def __init__(self):
        print('\n')
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
        print("/view_trans: to view the amount of lumen and transactions you have currently")
        print("-"*24)
        time.sleep(0.2)
        print("/issue_asset: To send and initialize an asset 'AstroDollar'")
        print("-"*24)
        time.sleep(0.2)
        print("/issue_casset: Initialize and send controlled assets, 'AstroDollar'")
        print("-"*24)
        time.sleep(0.2)
        print("/quit: to quit Stellar")
        print("-"*24)
        time.sleep(0.2)
        self.user_prompt()


    
    def user_prompt(self):
        while True:
            print("\n")
            prompt = str(input("Please enter a command: "))
            
            if prompt == '/create_trans':
                time.sleep(0.1)
                for account in all_accounts:
                    print('\n')
                    print('-'*24)
                    print(account)
                time.sleep(0.2)
                print("-"*24)
                print("\n Here are all the users currently on the platform")
                time.sleep(0.2)
                print("\n")
                print(colored('Directing you to creating a transaction ', 'blue'))
                user_trans = Contract()
                print(user_trans)
            
            elif prompt == '/view_trans':
                user_key = testnet_acc.user_key
                for account in all_accounts:
                    if account['PKey'] == user_key:
                        transactions = account['Transactions']
                        if len(transactions) != 0:
                            for transaction in transactions:
                                print('-'*24)
                                print("\n")
                                print(transaction)
                        else:
                            print("You have made no transactions yet!")
            
                    for balance in account['balances']:
                        print("Type: {}".format(balance['asset_type']))
                        time.sleep(0.1)
                        print("Balance: {}".format(balance['balance']))
            
            elif prompt == '/issue_asset':
                time.sleep(0.1)
                asset.make_payment()
            
            elif prompt == '/issue_casset':
                time.sleep(0.1)
                asset.control_asset_payment()
            
            elif prompt == '/receieve_trans':
                time.sleep(0.1)
                running()
            elif prompt == '/quit':
                break
            else:
                print("Command not found!")
        
        print(colored("You have successfully quitted Stellar! ", 'blue'))
    

                

        
                                
                            


        
        
        


test = Script()

print(test)
