from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError
from account import db,  cluster
from termcolor import colored


all_accounts = db.find({})

class Contract:
    
    server = server = Server("https://horizon-testnet.stellar.org")

    def __init__(self, server=self.server):
        self.print_users()
        time.sleep(0.2)
        print("-"*24)
        print("\n Here are all the users currently on the platform")
        time.sleep(0.2)
        print("\n")
        target_source_key = str(input("Please enter the name of the user you would like to send a transactiont to: "))
        print("Finding user...")
        time.sleep(0.2)
        result = self.fetch_users(target_source_key)
        if fetched == False:
            print(colored('{} was not found'.format(target_source_key), 'red'))
        else:
            print(colored('{} was found successfully! '.format(target_source_key), 'green'))

    

    def print_users(self):
        for account in all_accounts:
            print('\n')
            print('-'*24)
            print(account)

    def fetch_users(self, user):
        fetched = False 
        for account in all_accounts:
            if account['Username'] == user:
                fetched = True
                return account['Skey'], fetched 
            else:
                pass 
    
        return fetched
                