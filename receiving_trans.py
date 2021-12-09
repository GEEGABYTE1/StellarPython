from stellar_skd import Server 
from account import*
from termcolor import colored

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
     


    

    
    