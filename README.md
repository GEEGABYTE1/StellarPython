# Stellar 🪐
 
 A Fully-Functional Python program to interact with the Stellar Network. 

Users can send, receive and create assets while interacting with the Stellar Chain.


# Creating an Account 

It should be first noted that this program is ran on a testnet for safety reasons. However, if users want to connect to the real chain. 

In order to access the full program, users must have an account for *Stellar Python*. In order to do so, users can first type in `/sign_up`, where they will be prompted to type their public key. If they don't have one, for example, on a testnet server, users can type `/create` to obtain a testnet account with a fake amount of lumen. 

*Note*: Each account of the testnet will be created with 10000 lumen with base transaction fees of 100 lumen. See more on *Creating Transactions*. 

Only if the user is using the real Stellar Network can they only use `/fetch_pk`. Moreover, on the public network, the users' next step would be to acquire XLM, which they can do by consulting their lumen buying guide (Link under the *Resources* Section). Though, by default, StellarPython runs on a testnet, which is why each user gets 10000 lumen by Stellar's account funding tool. 

During the process of signing up, Stellar will create a public key, private, an empty array of transactions, and a paging token. For now, the array of transactions and pagaing token are not important, however it should be read about on either on Stellar's website, or under the *Creating Transactions* and *Receiving Transactions* part of the documentation. Stellar uses public key cryptography to ensure that every transaction is secure, and hence, every Stellar account has a keypair consisting of a *public key* and a *secret key*. 

The public key is always safe to share - other people need it to identify your account and verify that you authorized a transaciton (users can read more about this under the *Creating Transactions*). The secret key, however, is private information that proves your own - and gives you acess to your account. *It should never be shared with anyone*.

## Signing in

After users have created an account, users can sign in by typing their public key. It is always good to save both your public and secret key for reference when using this program. Though, it the user is using StellarPython on the real network, users are also obliged to use `/fetch_pk`. 

There are times where the user may run into an error. This is due to the fact that either their public key does not match or that the server is not connected. If the public key does not match, users should make sure that they are using the right key, which has been prompted out when originally creating an account with `/sign_up`. If the public key does not work, the testnet account may have expired, which will require the user to create another account. 

However, if the user is on a *real Stellar network*, they should make sure that the program has connected to the server. In order to make sure, users must set:
- `server_new = Server("https://horizon-testnet.stellar.org") to server_new = Server("https://horizon.stellar.org")` 

The actual server link can be found on Stellar's Website, which is linked below under *Resources*. When the user changes the server, it is necessary that they change all transaction classes to follow suit. Users can read more about this under *Creating Transactions*.

Once the user has successfully signed in, they should receieve a successful message and their lumen balance. They will then shortly be prompted with a set of commands to interact with StellarPython.


# Creating Transactions 
Transactions on Stellar a little different. Transactions on stellar are very sensible. If any operation in a transaction fails, they all fail. For example, if a user has 100 lumens and the user makes two payment operations of 60 lumens each. If the user makes two transactions (each with one operation), the first will succeed and the second will fail because the user doesn't have enough lumens. The user will be left with 40 lumens. However, if the user groups the two payments into a single transaction, they will both fail and the user will be left with the full 100 lumens still in your account. 

Every transaction also incurs a small fee. Like the minimum balance on accounts, this fee deters spam and prevents people from overloading the system. This base fee is 100 stroops per operations where a stroop equals *1 * 10^-7 XLM* - and it's charged for each operation. This may differ if the user is only the real Stellar Chain. Thus, if a transaction consists of two operations, for example, would cost 200 stroops. 

When creating a transaction or sending lumens, it is necessary that the user knows who they want to send it to. When they first type the command, `/create_trans`, they will be prompted with a list of users on the testnet, which they need to choose a user. However, should the user be running on a real network, there may not be all the users, but StellarPython will locate the account by the user typing in their desired account's private key.

*Note*: If user is running on a live network, the `network_passphrase` of the `TransactionBuilder()` class should change:
- `network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE`


Once the user has been located, the user will be faced with a  prompt for the number of lumens and a message. Users can type `/skip`, to skip the message if needed, and the program will continue to sign the transaction. Users can also specify their the type of asset they are sending (read more under *Receiving Transactions*). Stellar's network currency is the *Lumen*, but the user can send any asset issued on the network (both live or testnet, more info under *Receiving Transactions*).

- `.append_payment_op(destination=destination_id, asset=Asset.native(), amount="10")`

Users should also note that the amount is a string rather than a number. When working with extremely small fractions or large values, floating point math can introduce small inaccuracies. Since not all systems have a native way to accurately represent extremely small or large decimals, Stellar uses strings as a reliable way to represent the exact amount across any system.

If the transaction is successful, the user will receieve a success message with the transaction details. If there is any problem however, users will get an error message, which may be in red, and the transaction will be canceled. 

## Errors

When a transaction fails, there are multiple reasons. One, if the desired account's private key does not actually match with an account on either the real chain or on the testnet. In this case, users must double check their public key's and if they are using the right keys. For users on testnet, it should be double checked that they are typing in the user's correct username. 

The second possible error is if the amount of lumens the user wants to send exceeds the amount of lumen the sender user actually has. In this case, StellarPython will cancel the transaction, and the user may need to evalute their amounts of lumen. This may also interrupt the signing transaction process, which can also interrupt the transaction creation.

The third possible error is not having the correct `network_passphrase`, in which, the user may or need to use the testnet passphrases:
  - Testnet: `Network.TESTNET_NETWORK_PASSPHRASE`
  - Live: `Network.PUBLIC_NETWORK_PASSPHRASE`

# Receiving Transactions 

Stellar automatically sends and receieves different assets. Users don't have to run this part of the program, but it is good practice to watch out for incoming payments. 

There are two main parts of the program. First, the user creates a query for payments involving a given account. Like most queries in Stellar, this could return a huge number of items, so the API returns paging tokens, which you can use later to start your query from the same point where you previusly left off. In StellarPython, the functions to save and load pagain tokens are left blank, but when working with a real netowrk, the user would want to save the paging tokens to a file or a database so the program can pick up where it had left off when closed. Luckily, StellarPython does save the paging token for each transaction under a database for the user. 

The second part of the program is where the results of the query are streamed. This is the easiest way to watch for payments or other transactions. Each existing payment is sent through the stream, one by one. Once all existing payments have been sent, the stream says open and new payments are sent as they are made.

In order to run this, the user must run StellarPython as two different processes, of which one will be having the `/track` command ran. When the command is typed, the user will be faced with a prompt to type in a user they want to see incoming transactions from. After that, the query process starts, and which the user can track transactions related to their account.


# Stellar-Network Tokens

Assets are created with a payment operation: an issuing acccount makes a payment using the asset it's issuing, and that payment actually creates the asset on the network. On StellarPython, the asset issued will become the native transaction saved for the program. It is also recommended that the user creates issuing and distribution accounts. Distributing assets through a distribution account is a design pattern. Functionally, the user can do away with the distribution account and distribute directly from the issuer account. Moreover, the two main reasons to use a distribution account is for Security and Auditing. 

The account you use to distribute your asset from is going to be a *hot* account, meaning that some web service out there has direct access to sign its transactions. Additionally, if the account you use to distribute your asset is *is also the issuing account* and is compromised by a malicious actor, that actor can now issue as much of your asset they want. If the malicous actor redeems these newly issued tokens with the anchor service, the anchor may not have the liquidity to support customers' withdrawls. 

If the account you use to distribute your asset is not the issuing account, then the stakes are lower. Once discovered, the issuer account can effectively freeze the comporimised account's asset balance and start fresh with a new distribution account. This is possible without changing the issuing account.

The second reason is bookkeeping or auditability. The issuing account can't actually hold a balance of its own asset. If you have standing inventory of your own asset in a separate account, it is easier to track. This is a common pattern in various ledgering solutions. 

On StellarPython, as long as the issuer account remains *unlocked*, it can continue to create new tokens by making payments to the distribution account, or to any other account with the requisite trustline. 

If users are planning to do anything with their asset, their next step is to complete a `stellar.toml` file to provide wallets, exchanges, market listing services, and potential token holders with the information they need to understand what it represent. There is a sample stellar.toml file located in the repository called `sample.toml`. More parameters can be added by using Stellar's Doc, which is linked under *Resources*. 

StellarPython uses AstroDollar as the asset, however, it can be changed between different assets including Lumen. 


# Resources

Lumen Buying Guide: https://www.stellar.org/lumens/exchanges

