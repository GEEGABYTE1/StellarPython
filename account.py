from stellar_sdk import Keypair 

pair = Keypair.random()

print("Secret: {}".format(pair.secret))

print("Public: {}".format(pair.public_key))