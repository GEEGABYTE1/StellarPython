from stellar_sdk import Keypair
import requests 
import time
from stellar_sdk import Server
from termcolor import colored
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://BlindCelery:stellar@stellar.hibrh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Accounts']['Stellar']

class Account:
    server = None
    keys = []
    signed_in = False
    
    def create_account(self):
        if len(self.keys) > 0:
            self.keys = []
        pair = Keypair.random()
        secret_pair = pair.secret
        public_pair = pair.public_key
        self.keys.append(public_pair)
        self.keys.append(secret_pair)
        print(colored("Public key created", 'green'))
        print(time.sleep(0.2))
        print("Here is your public key: {}".format(public_pair))
        print("You can fetch this using /fetch_pk command when needed")
        return public_pair
        

    def sign_up(self):
        try:
            time.sleep(0.2)
            print("\n")
            print(colored("If you don't have a public key, please type /create or /fetch_pk to fetch your public key", 'blue'))
            public_key = str(input("Please print your public key: "))
            if public_key == '/quit':
                return 
            username = str(input("Please type in a username: "))
            if username == '/quit':
                return
            public_key = public_key.strip(" ")
            public_key = public_key.lower()
            if public_key == '/create':
                public_key = self.create_account()
                acc = {'Username': username, 'Pkey': public_key, 'Transactions': [], 'Paging_Token': None, 'Skey': self.keys[-1]}
                db.insert_one(acc)
            elif public_key == '/fetch_pk':
                try:
                    public_key = self.keys[-1]
                except:
                    print(colored("There is no key saved ", 'red'))

        
            response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
            if response.status_code == 200:
                print(colored("Success, you have successfully created an account! ", 'green'))
                time.sleep(0.2)
                print('You can now sign in! ')
            else:
                print(colored("Oops, there seems to be an error creating your account ", 'red'))

        except:
            print(colored("Oops, there seems to be an error creating your account ", 'red'))

    def sign_in(self, public_key):
        try:
            server_new = Server("https://horizon-testnet.stellar.org")
            self.server = server_new
            account = server.accounts().account_id(public_key).call()
            try:
                for balance in account['balances']:
                    print("Type: {}".format(balance['asset_type']))
                    time.sleep(0.1)
                    print("Balance: {}".format(balance['balance']))
                    return True
            except:
                print(colored("That public key seems to be invalid", 'red'))
                return False
        except:
            print(colored("Oops, something went wrong", 'red'))

    def return_s_p_key(self, user_key):
        all_accounts = db.find({})
        for account in all_accounts:
            if account['Pkey'] == user_key:
                self.keys.append(account['Pkey'])
                self.keys.append(account['Skey'])
        
    
    def __init__(self):
        self.signed_in = False
        user_key = None
        print('\n')
        print('-'*25)
        print("/sign_up: To create a new Stellar account")
        time.sleep(0.2)
        print('-'*25)
        print("/sign_in: To sign into Stellar")
        time.sleep(0.2)
        

        while True:
            print("\n")
            prompt = str(input(': '))
            if prompt == '/sign_up':
                self.sign_up()
            elif prompt == '/sign_in':
                print(colored("You can use /fetch_pk to fetch your public key if needed! ", 'blue'))
                user_key = str(input("Please type in your public key: "))
                if user_key == '/quit':
                    continue 
                if user_key == '/fetch_pk':
                    if len(self.keys) == 0:
                        print(colored('There is no key saved', 'red'))
                        continue
                    else:
                        print("Public Key: {}".format(self.keys[-1]))
                        user_key = self.keys[-1]
                
                    
                result = self.sign_in(user_key)
                if result == False or result == None:
                    continue 
                else:
                    print(colored("You have successfully signed in! ", 'green'))
                    self.signed_in = True
                    self.user_key = user_key
                    self.return_s_p_key(self.user_key)
                    
                    return 
            else:
                print(colored("That command does not seem to be valid", 'red'))
                    

                
                      

testnet_acc = Account()

