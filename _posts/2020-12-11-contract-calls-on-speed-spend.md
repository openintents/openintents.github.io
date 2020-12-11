---
title: Contract Calls on Speed Spend
subheadline: Handling digital assets
categories: blockstack
image:
  title: contract-calls.jpg
---

In the [introduction of Speed Spend](2020-09-15-introduction-to-speed-spend), it was explained how to transfer Stacks between users and between users and app accounts. The next step is to interact with smart contracts. There is a [video series](https://github.com/friedger/clarity-demo) about developing smart contracts in Clarity, but that is not the topic of this article. We just assume that the contracts exist, are deployed and ready to use.

Contracts calls can be made with the [connect library](ttps://www.npmjs.com/package/@stacks/connect) of stacks.js, similar to stacks transactions. The library provides the `openContractCall` method (and `doContractCall` for react). Nearly every button on Speed Spend is such a contract call. On the Hodl token page, the user can interact with the [Hodl token contract](https://github.com/friedger/clarity-smart-contracts/blob/master/contracts/tokens/hodl-token.clar). The source code of the contract can be inspected directly on-chain, e.g. with the [testnet explorer](https://testnet-explorer.blockstack.org). There is a public method to buy tokens (`buy-tokens`) and then to set (`hodl`) and unset (`unhodl`) the tokens into hodl mode.

## Post-conditions

The function argument is always the amount of type `uint`. The more interesting part are the so-called [post-conditions](https://docs.blockstack.org/understand-stacks/transactions#post-conditions) for these calls. Post-conditions are defined by the user when making a contract call. They describe the expected behaviour of the contract call with respect to all the different assets that are moved during the contract call. This gives users a tool to prevent undesired actions by the contract like withdrawing more tokens from the user's account than expected.

Assets are all digital tokens that are represented in Clarity as `fungible-token`, `non-fungible-token` or Stacks (`stx`). Only these three types of assets are available on the Stacks chain.

If the user trusts the contract, the post-condition mode can be set to `allow`. That means that all assets can be moved unconditionally. If the user does not trust the contract, the user has to provide at least one post-condition for each asset that was moved. For fungible tokens, the condition is always about the amount of tokens that was transferred **from** the original owner. It is not possible to add conditions about the receiver. For non-fungible tokens, the condition is about ownership of the token **after** the transfer.

If the conditions are not met the contract call will fail. The user has paid the fees but all assets are still owned by the original owner.

In the case of Hodl tokens, there are the two assets: `spendable-token` and `hodl-token`. They are both defined in the same contract and together they define the Hodl token. Each public function moves both tokens around, therefore the post-conditions have to be specified for both.

### Fungible post-conditions

The app claims that 1 hodl token = 1 (micro)stacks. For buying Hodl tokens, the following condition enforces that only less or equal to the given parameter `amount` stacks are moved from the transaction sender. As the `spendable-tokens` and `hodl-tokens` are minted (and not transferred from a faucet) the user does specify any condition for these tokens, only for the stacks used for payment:

```
makeStandardSTXPostCondition(
  ownerStxAddress,
  FungibleConditionCode.LessEqual,
  new BigNum(amount)
)
```

There are condition codes for equal, less, greater and greater or equal.

For the `hodl` function, conditions for both tokens need to be specified because both are transferred. Hodl tokens are transferred from the contract to the user, and spendable tokens are transferred from the user to the contract:

```
[
  makeContractFungiblePostCondition(
    CONTRACT_ADDRESS,
    HODL_TOKEN_CONTRACT,
    FungibleConditionCode.LessEqual,
    new BigNum(amount),
    createAssetInfo(CONTRACT_ADDRESS, HODL_TOKEN_CONTRACT, 'hodl-token')
  ),
  makeStandardFungiblePostCondition(
    ownerStxAddress,
    FungibleConditionCode.LessEqual,
    new BigNum(amount),
    createAssetInfo(CONTRACT_ADDRESS, HODL_TOKEN_CONTRACT, 'spendable-token')
  ),
]
```

The relevant asset is created with the helper function `createAssetInfo`.

Note, that the condition for the contract uses the `makeContractFungiblePostCondition` instead of `makeStandardFungiblePostCondition`. This is because contracts have a different type in Clarity than user addresses.

### Non-fungible post-conditions

On the marketplace page, users can pay for their requested monsters. The contract call (`pay`) will transfer stacks tokens to the original owner of the monster and transfer the monster to the new owner. The following conditions would enfore that:

```
 makeContractNonFungiblePostCondition(
  CONTRACT_ADDRESS,
  'market',
  NonFungibleConditionCode.DoesNotOwn,
  createAssetInfo(tradableCV.address, tradableCV.name, 'nft-monsters'),
  tradableIdCV
),
makeStandardSTXPostCondition(
  bidOwnerCV.address,
  FungibleConditionCode.LessEqual,
  new BigNum(amount)
),
```

Note, that for non-fungible tokens only two condition codes exist: `Owns` and `DoesNotOwn`. Furthermore, the identifier of the NFT (asset name) has to be provided. In this case, it is the monster id.

However, the name of the asset `nft-monsters` is not known to the marketplace app. Currently, there is no way to discover the name other than reading the source code. Therefore, the post-condition mode is set to `allow` for this call. While this works, it is not desirable from the user perspective.

Hopefully, a standard that is currently in development will help to find a convenient way for apps to solve this problem. See [www.tofauti.net](https://www.tofauti.net/) and the [SIP repository](https://github.com/stacksgov/sips) for progress.
