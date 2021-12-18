from account import testnet_acc
from account import*
from termcolor import colored
from creating_trans import Contract
from account import db


def running():
    #paging_token_update = save_paging_token(load_last_paging_token())
    receieve_payment()


def load_last_paging_token():
    return "now"

def save_paging_token(paging_token):
    pass
    
server = testnet_acc.server
account_chosen = None

def fetch_users(fetched=False):
    
    account_server = db.find({})
    try:
        user = str(input("Please enter the sender you want track transitions from: "))
        print("Finding user...")
        time.sleep(0.2)
        
        for account in account_server:
            if account['Username'] == user:
                account_chosen = account
                fetched = True
                return account['Pkey'], account['Skey']
            else:
                pass 

        return fetched
    except:
        print(colored("User not found", 'red'))

def receieve_payment():
        try:
            while True:
                fetched_user = fetch_users()
                if type(fetched_user) != tuple:
                    continue
                else:
                    break
            
                
            user_id = fetched_user[0]
            payments = server.payments().for_account(user_id)
            
            last_token = load_last_paging_token()
            
            if last_token:
                payments.cursor(last_token)
                
                for payment in payments.stream():
                    save_paging_token(payment['paging_token'])
                    acccount_chosen['Paging_Token'] = payment['paging_token']


                    if payment['type'] != 'payment':
                        continue 
                    if payment['to'] != user_id:
                        continue
                    if payment['asset_type'] == 'native':
                        asset = 'Lumens'
                    else:
                        asset = f"{payment['asset_code']}:{payment['asset_issuer']}"
                    print("Payment: {amount} from payment from {sender}".format(amount=asset, sender=payment['from']))
        except:
            print(colored('The account could not be found ', 'red'))



    

    
    