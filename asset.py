from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder, AuthorizationFlag
from stellar_sdk.exceptions import BaseHorizonError
from account import testnet_acc, db
from termcolor import colored
import time




class Asset_S:
    server = testnet_acc.server
    network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE
    

    def issue_asset(self):
        time.sleep(0.2)
        print("Type /fetch_pk if you do not have your public key else, type your public key")
        prompt = str(input(": "))
        prompt = prompt.strip(" ")
        if prompt == '/fetch_pk':
            prompt = testnet_acc.keys[-1]
        
        try:
            astro_dollar = Asset("AstroDollar", prompt)
            print(colored("Asset successfully created", 'green'))
        except:
            print("Tha public key is not found")
    
    def search_user(self):
        all_accounts = db.find({})
        dictionary = {}

        for account in all_accounts:
            username = account['Username']
            user_secret = account['Skey']
            dictionary[username] = user_secret 
            print('-'*24)
            print(colored(username, 'blue'))
            time.sleep(0.2)

        print('-'*24)
        time.sleep(0.1)
        user_des_user = str(input("Please type in a username you would like to send your asset to: "))
        result = dictionary.get(user_des_user, None)
        return result, dictionary, user_des_user


    def make_payment(self):
        try:
            distributor_keys = testnet_acc.keys
            distributor_secret_key = distributor_keys[-1]
            distributor_public_key = distributor_keys[0]

            iteration = self.search_user()
            result = iteration[0]
            dictionary = iteration[1]
            user_des_user = iteration[-1]
            
            issuing_keypair = Keypair.from_secret(dictionary[user_des_user])
            issuing_public = issuing_keypair.public_key 

            distributor_account = self.server.load_account(distributor_public_key)
            astro_dollar = Asset('AstroDollar', issuing_public)

            # Trusting Asset 

            trust_transaction = (
                TransactionBuilder(
                    source_account = distributor_account,
                    network_passphrase=self.network_passphrase,
                    base_fee = 100,
                )
                .append_change_trust_op(asset=astro_dollar, limit='10000')
                .set_timeout(100)
                .build() 

            )

            trust_transaction.sign(distributor_secret_key)
            trust_transaction_resp = self.server.submit_transaction(trust_transaction)
            print("Change Trust Transaction Resp: {}".format(trust_transaction_resp))
            print('\n')

            issuing_account = self.server.load_account(issuing_public)

            user_amount = str(input("Please type in an amount you would like to send: "))

            payment_transaction = (
                TransactionBuilder(
                    source_account=issuing_account,
                    network_passphrase=self.network_passphrase,
                    base_fee=100,
                )
                .append_payment_op(
                    destination=distributor_public_key,
                    asset=Asset.native(),
                    amount=user_amount,
                )
                .build()
            )

            payment_transaction.sign(issuing_keypair)
            payment_transaction_resp = self.server.submit_transaction(payment_transaction)

            print('\n')
            print(colored("Payment Transaction Resp: {}".format(payment_transaction_resp), 'blue'))
            print('-'*24)
            print('\n')
            
        except:
            print(colored('Something went wrong', 'red'))
            time.sleep(0.1)

    def control_asset_payment(self):
        distributor_keys = testnet_acc.keys
        distributor_secret_key = distributor_keys[-1]
        distributor_public_key = distributor_keys[0]
        try:
            
            iteration = self.search_user()
            result = iteration[0]
            dictionary = iteration[1]
            user_des_user = iteration[-1]

            issuing_keypair = Keypair.from_secret(dictionary[user_des_user])
            issuing_public = issuing_keypair.public_key
            issuing_account = self.server.load_account(issuing_public)
            
            prompt_transaction = (
                TransactionBuilder(
                    source_account=issuing_account,
                    network_passphrase=self.network_passphrase,
                    base_fee=100,
                )
                .append_set_options_op(
                    set_flags=AuthorizationFlag.AUTHORIZATION_REVOCABLE | AuthorizationFlag.AUTHORIZATION_REQUIRED
                )
                .build()
            )

            transaction.sign(issuing_keypair)
            try:
                transaction_resp = self.server.submit_transaction(transaction)
                print("Transaction Resp: {}".format(transaction_resp))
            except BaseHorizonError as e:
                print("Error: {}".format(e))
        
        except:
            print(colored('User not found', 'red'))
            time.sleep(0.1)

        
        

asset = Asset_S()
        
        



