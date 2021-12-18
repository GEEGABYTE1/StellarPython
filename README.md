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

However, if the user is on a real Stellar network, they should make sure that the program has connected to the server. In order to make sure, users must set:
- `server_new = Server("https://horizon-testnet.stellar.org") to server_new = Server("RealServerLink")` 

The actual server link can be found on Stellar's Website, which is linked below under *Resources*. When the user changes the server, it is necessary that they change all transaction classes to follow suit. Users can read more about this under *Creating Transactions*.


# Creating Transactions 


# Receiving Transactions 


# Stellar-Network Tokens


# Resources

Lumen Buying Guide: https://www.stellar.org/lumens/exchanges

