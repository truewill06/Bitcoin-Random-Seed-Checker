import random
import binascii
import mnemonic
import bip32utils
import urllib3
from bs4 import BeautifulSoup
import time
import os
import json
from os.path import dirname, join
swordlist = ['adult', 'affair', 'alien', 'amatuer', 'animal', 'artefact', 'baby', 'balance', 'barely', 'behave', 'behind', 'benefit', 'betray', 'beyond', 'black', 'bless', 'body', 'bone', 'boss ', 'bottom ', 'bounce', 'boy', 'brother', 'business', 'call', 'chase', 'choice', 'choose', 'control', 'cream', 'curious ', 'cute', 'daughter', 'deal', 'diamond', 'dog', 'doll', 'dress', 'dream', 'drive', 'drop', 'earn', 'edge', 'empty', 'enjoy', 'exchange', 'expire', 'expose', 'exotic', 'faith', 'fantasy', 'female', 'finger', 'finish', 'firm', 'fun', 'girl', 'goddess', 'hammer', 'have', 'head', 'hole', 'horn', 'honey', 'home', 'hungry', 'hurt', 'husband', 'inmate', 'job', 'kid', 'kiss', 'lady', 'live', 'love', 'loyal', 'man', 'manage', 'marriage', 'master', 'mean', 'member', 'more', 'mother', 'obey', 'okay', 'online', 'open', 'outside', 'owner', 'paddle', 'payment', 'phone', 'picture', 'pink', 'pizza', 'play', 'please', 'plunge', 'point', 'pole', 'position', 'power', 'price', 'private', 'real', 'ready', 'remember', 'remove', 'right', 'ring', 'romance', 'rough', 'run', 'satisfy', 'scissors', 'shaft', 'sister', 'six', 'skirt', 'skin', 'sleep', 'smile', 'special', 'spoil', 'squeeze', 'submit', 'text', 'that', 'there', 'they', 'thing', 'this', 'tip', 'together', 'tongue', 'tool', 'top', 'toy', 'trust', 'truth', 'truly', 'true', 'urge', 'use', 'wait', 'want', 'warm', 'way', 'wedding', 'welcome', 'wet', 'what', 'when ', 'where', 'whip', 'wife', 'will', 'win', 'wire', 'woman', 'work', 'write', 'you']


# I have a modified BIP39 wordlist I use... in case someone wanted to use their own words. I picked sexual words...
# Function creates 12 word key.

       

def generate_12_word_key(swordlist):
    
    counter = 1
    key = []
    new_word = key.append(random.choice(swordlist))
    while counter != 12 :
        for i in key:
            new_word = str(random.choice(swordlist))
            if (i != new_word) & (counter != 12):
                key.append(new_word)
                counter = counter + 1
                skey = " ".join(key)
    
    
    
    return skey

# Function takes 12 word key and gives the address, public key, and private key

def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)
    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)
    
    blockchain_address = str("https://www.blockchain.com/btc/address/" + str(bip32_child_key_obj.Address()))
    http = urllib3.PoolManager()
    response = http.request('GET', blockchain_address)
    soup = BeautifulSoup(response.data.decode('utf-8'), features="lxml")
    
    value = "".join(soup.findAll("span", text=True)[34])
    value = int(value[28])            
    
    return {
        'mnemonic_words': mnemonic_words,
        'addr': bip32_child_key_obj.Address(),
        'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
        'privatekey': bip32_child_key_obj.WalletImportFormat(),
        'coin': 'BTC',
        'blockchain_address': blockchain_address,
        'value': value
    }


def get_info(swordlist):
    return bip39(generate_12_word_key(swordlist))
    
def output(dict1):
    
    output = str(
                 "Trying address: " + dict1['addr'] +
                 os.linesep +
                 os.linesep +
                 "Keys: " +
                 os.linesep +
                 os.linesep +
                 dict1['publickey'] +
                 os.linesep +
                 dict1['privatekey'] +
                 os.linesep +
                 "Seed phrase: " + dict1['mnemonic_words'] +
                 os.linesep +
                 os.linesep +
                 "Value: " + str(dict1['value']) +
                 os.linesep +
                 os.linesep +
                 "Trying again...." +
                 os.linesep)

    
                 
    return output
    
 def working(get_info, swordlist, counter):
    
    counter = 0
    dict1  = get_info
    value = dict1['value']
    while value == 0:
        working(get_info(swordlist), swordlist)
        counter = counter + 1
        
        return counter

def main():

    while value !== 0:

    dict1 = get_info(swordlist)
    value = dict1['value']
    dict1 = get_info(swordlist)
    output1 = output(dict1)
    return output1
        

    

        

    
    


        
    
    
    


    
    
    
    
    
    
    
        
        

    
        

        

