from account import testnet_acc
from account import*
from termcolor import colored

def running():
    paging_token_update = save_paging_token(load_last_paging_token())
    receieve_payment()


def load_last_paging_token():
    return "now"

def save_paging_token(paging_token):
    # Must be saved to token
    all_accounts = db.find({})
    user_user = str(input("For security reasons, please type in your username: "))
    checked = False
    for account in all_accounts:
        if account['Username'] == user_user:
            account['Paging_Token'] = paging_token
            checked = True
            break 
        else:
            continue
    
    if checked == False:
        print(colored("Account not found", 'red'))
    else:
        return checked
    
server = testnet_acc.server

def receieve_payment():
    try:
        user_id = testnet_acc.keys[0]
        payments = server.payments().for_account(user_id)
        
        last_token = load_last_paging_token()
        if last_token:
            payments.cursor(last_token)
            
            for payment in payments.stream():
                save_paging_token(payment['paging_token'])

                if payment['type'] != 'payment':
                    continue 
                if payment['to'] != account_id:
                    continue
                if payment['asset_type'] == 'native':
                    asset = 'Lumens'
                else:
                    asset = f"{payment['asset_code']}:{payment['asset_issuer']}"
                print("Payment: {amount} from payment from {sender}".format(amount=asset, sender=payment['from']))
    except:
        print(colored('The account {} could not be found '.format(user_id), 'red'))



    

    
    