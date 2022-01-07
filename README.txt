Here is an outline of my idea. I figure maybe someone wanted to go through the BIP39 wordlist to create their own 12 word phrase from it and get the corresponding address, public key, and priavte key from that....

So, what this script does is generates a 12 word phrase from a custom wordlist that I created thats smaller. I picked sexual words and words that have to do with business from the BIP39 worldlist.

I have two wordlists...

swordlist.txt - sexual words
wordlist.txt - sexual and business words.

This script chooses random 12 words from my wordlists and generates the corresponding address, public key, and priavte key from that.

It takes the info and checks it using blockchain.com checking for transactions. Loops until it finds an address that doesnt have 0 transactions.

Its slow... I have to set a time.sleep on it or I get "Too many requests". But it does stay running. I want to use proxies or something to speed it up. I'm working on that now.

In the future I would like to add users to a pool. They give their email with BTC address and if anyone hits it will split it between everyone. Turn into an android app that constantly runs in bg.

I went to college for programming for 3 years. Didn't finish but I think I'm ok at it... I want to be a developer but coming up with ideas for things to actually build is hard. Help? I do have this one thing I've been working on.



