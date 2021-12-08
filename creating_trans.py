from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError


class Contract:
    
    server = server = Server("https://horizon-testnet.stellar.org")

    def __init__(self, server=self.server):
        target_source_key = str(input("Please enter the name of the user you would like to send a transactiont to: "))
        