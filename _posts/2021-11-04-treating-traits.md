---
title: Treating Traits in Clarity
subheadline: Protecting escrows
categories: blockstack
image:
  title: treating-traits.png
---

The smart contract language Clarity comes with the concept of traits. Traits are properties of a contract that can be observed from the outside but have a specific meaning to the inside. Like with NFTs, a blue hat in an NFT image can be recognized by all but the advantages for the owner e.g. in a blogging app becomes clear only after studying the app.


![Blue Hat](https://github.com/openintents/openintents.github.io/raw/master/images/treating-traits-blue-hat.png)
(artist: Quentin Saubadu, copyright: friedger)

The same holds for smart contracts and their traits. Common traits are SIP-009 trait for NFTs or SIP-010 traits for fungible tokens. There is a node api to easily verify whether a contract has a given trait. For example, the api states that Friedger Pool NFT indeed has the NFT trait.

[https://stacks-node-api.mainnet.stacks.co/v2/traits/SP1K1A1PMGW2ZJCNF46NWZWHG8TS1D23EGH1KNK60/friedger-pool-nft/SP1JSH2FPE8BWNTP228YZ1AZZ0HE0064PS6RXRAY4/nft-trait/nft-trait](https://stacks-node-api.mainnet.stacks.co/v2/traits/SP1K1A1PMGW2ZJCNF46NWZWHG8TS1D23EGH1KNK60/friedger-pool-nft/SP1JSH2FPE8BWNTP228YZ1AZZ0HE0064PS6RXRAY4/nft-trait/nft-trait)

Looking at the Friedger Pool NFT contract we can verify that the NFT functions correctly transfer ownership and provide metadata.

Traits are helpful when a contract needs to manage other contracts that have different implementation of the same functions. Good examples are marketplaces, vaults or swap contracts. These are general contracts that can be applied to any NFT or token as long as the managing contract can call e.g. the transfer function of the NFT or token.

## Danger

The calling contract cannot inspect the NFT or token like we can do from the outside. Therefore, the contract must expect the NFT or token to do things as bad as possible. The transfer function could not transfer ownership, the get-balance function could return different values at different block heights. These functions could set some flags that don't affect the current transaction and wouldn't violate any post-conditions set by the user but that could move assets in a second transaction in the future.

This means that users of these general contracts must be very careful. The swap contract (btc-ft-v1) of catamaranswaps.org called the transfer of any fungible token to move user's assets into escrow and then later out of the contract. For the latter, the contract contained the following code:

```
(as-contract (contract-call? ft-trait transfer amount tx-sender new-owner))
```

While the trait suggests that the token contract would move just the given amount of tokens from the contract to the new owner, in fact, the token contract could do a lot more, in particular it could move any assets currently hold by the swap contract. For that reason, catamaranswap.org was disabled the generic btc-ft and btc-nft swap for now.

## Protection

First, general contracts should use traits carefully, in particular, when they switch the tx sender context with as-contract. It could give malicious contracts access to "protected" function if they don't handle tx-sender and contract-caller correctly. While using contract-caller is more secure it prevents bulk transactions. A smart trick for protected functions would be to send 1 micro STX during that function. This would require the user to specify a post-condition (credits to lnow for this).

Second, Clarity requires that traits are provided directly by the user. Traits can't be wrapped or stored. Therefore, the user is in control when using these general contracts. The burden is now on the UI to help users to understand the impact. Apps should inform the users that only vetted contracts can be passed to the general contracts or the apps should warn the user that they are using a potentially malicious contract as a trait. This leads to bigger question about governance. Who can verify contract? Who can blacklist them or who can whitelist them? How can protocol still be permissionless? How can the authenticator support users?

I am looking forward to a healthy discussion about these questions.

A big thank you to lnow for his restless work on this vulnerability and his professional communication with affected projects including catamaranswap. 