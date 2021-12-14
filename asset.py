from stellar_sdk import Asset
from account import testnet_acc


class Asset:
    time.sleep(0.2)
    print("Type /fetch_pk if you do not have your public key else, type your public key")
    prompt = str(input(": "))
    prompt = prompt.strip(" ")
    if prompt == '/fetch_pk':
        prompt = testnet_acc.keys[-1]
    
    try:
        astro_dollar = Asset("AstroDollar", prompt)


