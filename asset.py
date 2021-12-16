from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from account import testnet_acc, db
from termcolor import colored




class Asset:
    server = Server(horizon_url="https://horizon-testnet.stellar.org")
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


    def receive_asset(self):
        distributor_keys = testnet_acc.keys
        distributor_secret_key = distributor_keys[-1]
        distributor_public_key = distributoer_keys[0]

        all_accounts = db.find({})
        dictionary = {}

        for account in all_accounts:
            username = account['Username']
            user_secret = account['Skey']
            dictionary[username] = user_secret 
            print('-'*24)
            print(username)
            print('\n')
            time.sleep(0.2)

        print('-'*24)
        time.sleep(0.1)
        user_des_user = str(input("Please type in a username you would like to send your asset to: "))
        result = dictionary.get(user_des_user, None)
        if result == None:
            print(colored('User not found', 'red'))
            time.sleep(0.1)
        else:
            issuing_keypair = Keypair.from_secret(dictionary[user_des_user])
            issuing_public = issuing_keypair.public_key 

            distributor_account = self.server.load_account(distributor_public_key)
            astro_dollar = Asset('AstroDollar', issuing_public)

            # Trusting Asset 

            trust_transaction = (
                TransactionBuilder(
                    source_account = distributor_account,
                    network_passphrase=network_passphrase,
                    base_fee = 100,
                )
                .append_change_trust_op(asset=astro_dollar, limit='1000')
                .set_timeout(100)
                .build() 

            )

            trust_transaction.sign(distributor_secret_key)
            trust_transaction_resp = self.server.submit_transaction(trust_transaction)
            print("Change Trust Transaction Resp: {}".format(trust_transaction_resp))

            issuing_account = self.server.load_account(issuing_public)

            payment_transaction = (
                TransactionBuilder(
                    source_account=issuing_account,
                    network_passphrase=network_passphrase,
                    base_fee=100,
                )
                .append_payment_op(
                    destination=distributor_public_key,
                    asset=Asset.native(),
                    amount="10",
                )
                .build()
            )

            payment_transaction.sign(issuing_keypair)
            payment_transaction_resp = self.server.submit_transaction(payment_transaction)
        
            print("Payment Transaction Resp: {}".format(payment_transaction_resp))
            
        
        



