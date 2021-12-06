from stellar_sdk import Keypair
import requests 
import time
from stellar_sdk import Server
from termcolor import colored

class Account:
    keys = []
    
    def create_account(self):
        pair = Keypair.random()
        secret_pair = pair.secret
        public_pair = pair.public_key
        self.keys.append(secret_pair)
        self.keys.append(public_pair)
        print(colored("Public key created", 'green'))
        print(time.sleep(0.2))
        print("Here is your public key: {}".format(public_pair))
        print("You can fetch this using /fetch_pk command when needed")
        return public_pair
        

    def sign_up(self):
        time.sleep(0.2)
        print("\n")
        print(colored("If you don't have a public key, please type /create or /fetch_pk to fetch your public key", 'blue'))
        public_key = str(input("Please print your public key: "))
        public_key = public_key.strip(" ")
        public_key = public_key.lower()
        if public_key == '/create':
            public_key = self.create_account()
        elif public_key == '/fetch_pk':
            public_key = self.keys[-1]
            
        
        response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
        if response.status_code == 200:
            print(colored("Success, you have successfully created an account! ", 'green'))
            time.sleep(0.2)
            print('You can now sign in! ')
        else:
            print(colored("Oops, there seems to be an error creating your account ", 'red'))

    def sign_in(self, public_key):
        server = Server("https://horizon-testnet.stellar.org")
        account = server.accounts().account_id(public_key).call()
        try:
            for balance in account['balances']:
                print("Type: {}".format(balance['asset_type']))
                time.sleep(0.1)
                print("Balance: {}".format(balance['balance']))
        except:
            print(colored("That public key seems to be invalid", 'red'))
            return False
    
    def __init__(self):
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
                if user_key == '/fetch_pk':
                    print("Public Key: {}".format(self.keys[-1]))
                    user_key = self.keys[-1]
                result = self.sign_in(user_key)
                if result == False:
                    pass 
                else:
                    print(colored("You have successfully signed in! ", 'green'))

                
                      

testnet_acc = Account()

print(testnet_acc)