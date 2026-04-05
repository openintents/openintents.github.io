---
title: "Working with Non-Fungible Tokens on Stacks"
categories: blockstack
image:
  title: working-with-non-fungible-tokens-on-stacks.jpg
---

While working with non-fungible tokens on the [Stacks blockchain](https://www.stacks.co/) I came across various names and terms that should be explained here:

Non-fungible tokens (NFT) are defined in Clarity contracts, smart contracts using the [Clarity language](https://clarity-lang.org/). The language provides the function `define-non-fungible-token` providing a name for the NFT. There can be many NFTs created by the contract. They are distinguished through an identifier. The type of identifier is part of the NFT definition. Usually, NFTs are identified by a positive integer (`uint` in Clarity). A typical definition looks like this:

`(define-non-fungible-token nft-name uint) `

Once the contract (named `nft-factory`) that contains the NFT definition is deployed to the blockchain we have all parts together to create and handle NFTs. Let's assume the contract was deployed using the stacks address `SP1K1A1PMGW2ZJCNF46NWZWHG8TS1D23EGH1KNK60`.

### Definitions

**Contract ID**
The contract ID is a globally unique string consisting of the **contract address** and **contract name** separated by a dot (".").
Example:`SP1K1A1PMGW2ZJCNF46NWZWHG8TS1D23EGH1KNK60.nft-factory`

**Digital Assets
**Digital assets represent some valuable data on the blockchain. On the Stacks blockchain, there are three types of digital assets that are supported natively: Stacks tokens, fungible tokens and non-fungible-tokens. Here we only consider NFTs.

**Asset Name
**The asset name is the name of the NFT within the contract. Note that a contract can define more than one NFT.
Example:`my-art`

**Asset Class**
The asset class is the combination of contract id and asset name separated by two colons ("::"). This is a globally unique string. Unfortunately, the Stacks Node Api using `asset_id` to describe asset class (issue [#432](https://github.com/blockstack/stacks-blockchain-api/issues/432)).
Example:`SP1K1A1PMGW2ZJCNF46NWZWHG8TS1D23EGH1KNK60.nft-factory::my-art`

**Asset ID
**The asset ids identify NFTs of a given NFT class. Depending on the NFT this could be an integer or a set of properties defined by a Clarity `tuple` or any other type. The asset id together with the asset class is globally unique. However, there can be the same asset ids for different NFT class.
Example: `u1 `(unsigned 1)

### Owned NFTs

The [Stacks Node API ](https://blockstack.github.io/stacks-blockchain-api/)provides a two endpoints to retrieve information about the NFTs that a user owns. Ownership means that the clarity function `nft-get-owner` returns the user when querying in the contract of the NFT with the asset name and the asset id.

At first, the endpoint [Get account balances](https://blockstack.github.io/stacks-blockchain-api/#operation/get_account_balance) returns a list of all asset classes that the user owns or has owned. For each asset class the number of owned, received and send NFTs is listed. Now, the endpoint [Get account assets](https://blockstack.github.io/stacks-blockchain-api/#operation/get_account_assets) can be used to retrieve more details, in particular the asset ids of the NFTs that the user owns. For further details about the NFT, the corresponding contract needs to be queried. 

For contract developers, it is suggested to define a function named `get-meta` that takes the asset id as a parameter and returns additional data like a name or a uri. Currently, there is no schema define how this data should look like.

****
