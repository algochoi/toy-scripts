'''
Script to create an account and output relevant info into a txt file

Pre-requisite: Make sure you are running a node!
$ goal node start -d ~/node/testnetdata
$ goal node status -d ~/node/testnetdata
'''

from algosdk import account, encoding, mnemonic

private_key, address = account.generate_account()
print("Private key:", private_key)
print("Address:", address)
print("Mnemonic: ", mnemonic.from_private_key(private_key))