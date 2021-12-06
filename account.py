from stellar_sdk import Keypair
import requests 
import time
from termcolor import colored

class Account:
    keys = []
    
    def create_account(self):
        pair = Keypair.random()
        secret_pair = pair.secret
        public_pair = pair.public_key
        self.keys.append(secret_pair)
        self.keys.append(public_pair)
        print(colored("Public keyc created"), 'green')

    def sign_up(self):
        time.sleep(0.2)
        print("\n")
        print(colored("If you don't have a public key, please type /create" 'blue'))
        user_public_key = str(input("Please print your public key: "))
        user_public_key = user_public_key.strip(" ")
        user_public_key = user_public_key.lower()
        if user_public_key == '/create':
            self.create_account()
        
        response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
        if response.status_code == 200:
            print(colored("Success, you have successfully created an account! ", 'green'))
            time.sleep(0.2)
            print('You can now sign in! ')
        else:
            print(colored("Oops, there seems to be an error creating your account ", 'red'))



    
    def __init__(self):
        print('\n')
        print('-'*25)
        print("/sign_up: To create a new Stellar account")
        time.sleep(0.2)
        print('-'*25)
        print("\n")
        print("/sign_in: To sign into Stellar")
        time.sleep(0.2)
        

        while True:
            print("\n")
            prompt = str(input(': '))
            if prompt == '/sign_up':
                self.sign_up()
            elif prompt == '/sign_in':
                pass
                      

