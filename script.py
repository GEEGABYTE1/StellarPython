from account import testnet_acc # Creating Account
from creating_trans import Contract # Creating/Sending Transaction
from account import db # Database
from asset import asset #AstroDollar and Tokenizing
from receiving_trans import running


import time
from termcolor import colored


all_accounts = db.find({})

class Script:
    #transactions = []
    balances = {}
    account_signed_in = testnet_acc.og_account

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
        print("/view_bal: to view the amount of lumen and transactions you have currently")
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
            time.sleep(0.3)
            #user_key = testnet_acc.user_key
        
            account_connection = testnet_acc.server.accounts().account_id(testnet_acc.keys[0]).call()
            for balance in account_connection['balances']:
                type_balance = balance['asset_type']
                num = balance['balance']
                self.balances[type_balance] = num
            print("\n")
            prompt = str(input(": "))
            
            if prompt == '/create_trans':
                time.sleep(0.1)
                print("\n")
                print(colored('Directing you to creating a transaction ', 'blue'))
                user_trans = Contract()
                
            elif prompt == '/view_bal':
                
                for type_bal, balance in self.balances.items():
                    print('\n')
                    print('Balance Asset: {type}: {value}'.format(type=type_bal, value=balance))
                    print('-'*24)
                
            
            elif prompt == '/issue_asset':
                time.sleep(0.1)
                asset.make_payment()
            
            elif prompt == '/issue_casset':
                time.sleep(0.1)
                asset.control_asset_payment()
            
            elif prompt == '/receive_trans':
                time.sleep(0.1)
                running()
            elif prompt == '/quit':
                break
            else:
                print("Command not found!")
        
        print(colored("You have successfully quitted Stellar! ", 'blue'))
    

                

        
                                
                            


        
        
        


test = Script()

print(test)
