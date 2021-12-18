from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError
from account import db,  cluster
from termcolor import colored
from account import testnet_acc
import time




class Contract:

    server = testnet_acc.server
    all_accounts = db.find({})
    saved_acc = None


    def __init__(self):
        server = self.server
     
        result = self.fetch_users()
        if result[-1] == False:
            print(colored('Account was not found', 'red'))
        else:
            print(colored('{} was found successfully! '.format(result[1]), 'green'))
            source_key = Keypair.from_secret(testnet_acc.keys[-1])
            user_prompt = str(input('Are you sending lumen on the real chain? (Type y/n)'))
            user_prompt = user_prompt.strip(" ")
            if user_promt == 'n':
                destination_id = result[1]
            else:
                destination_id = str(input("Please type in the desired account's private key: "))
                destination_id = destination_id.strip(" ")

            #### FINDING USER ENDS 

            ### CREATING TRANS STARTS

            try:
                self.server.load_account(destination_id)
            except NotFoundError:
                print(colored("This account does not exist", 'red'))
        
            source_account = server.load_account(source_key.public_key)
            
            base_fee = server.fetch_base_fee()
            lumen_amount = str(int(input("Please enter the amount of lumen you would like to send: ")))
            user_message = str(input("Please type in a message for the user (type /skip to skip this step): "))
            if user_message == '/skip':
                user_message = " " 
            
            ## Transaction Block
            transaction = (
                TransactionBuilder(
                    source_account = source_account,
                    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                    base_fee=base_fee,
                     
                )
                .append_payment_op(destination=destination_id, asset=Asset.native(), amount=lumen_amount)
                .add_text_memo(user_message)
                #.set_timeout(2)
                .build()
                
                
                
            )

            transaction.sign(source_key)

            # Sending to Stellar

            try:
                response = self.server.submit_transaction(transaction)
                print(colored("Transaction Successful", 'green'))
                time.sleep(0.2)
                print('\n')
                print('-'*24)
                print(colored("Response: {}".format(response), 'blue'))            
                print('-'*24)
                
                       
            except (BadRequestError, BadResponseError) as err:
                print(colored('Something went wrong! ', 'red'))
                time.sleep(0.2)
                


    def fetch_users(self, fetched=False):
    
        try:
            user = str(input("Please enter the name of the user you would like to send a transaction to: "))
            print("Finding user...")
            time.sleep(0.2)
            
            for account in self.all_accounts:
                if account['Username'] == user:
                    self.saved_acc = account
                    fetched = True
                    return account['Skey'], account['Pkey'], account['Transactions'], fetched 
                else:
                    pass 

            return [fetched]
        except:
            print(colored("User not found", 'red'))
        
                