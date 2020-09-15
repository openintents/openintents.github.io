---
title: Introduction to Speed Spend
subheadline: Web app to learn Stacks development
categories: blockstack
image:
  title: start.jpg
---

The development of the [Stacks testnet](https://www.blockstack.org/testnet) is progressing and it is now in a state that first smart contracts have been published. It is still early and changes to syntax, tooling and functions are still expected. Therefore, this post is updated as the testnet evolves.

There is already good [documentation](https://docs.blockstack.org/smart-contracts/overview) how to publish smart contracts on testnet. Following that descriptions provides you with a setup to develop your own contracts or experiment with existing ones. Alternatively, you can use the [Clarity Web IDE](https://friedger.github.io/clarity-web-ide/). You find a selection of Clarity smart contracts on [github](https://github.com/friedger/clarity-smart-contracts).

We build a web application called [Speed Spend](https://speed-spend.netlify.app) that explores different use cases for smart contracts in web apps. It is an educational app with focus on functionality, not design. Please send pull requests to beautify the app!

## Stacks Accounts

In order to interact with smart contracts, the user needs to have a private key to sign transactions. Each private key maps to a Stacks account on the Stacks blockchain and can hold STX tokens. A Stacks account is represented using the [Crockford base-32 encoding with checksum](https://github.com/blockstack/c32check). They look like something like `ST12EY99GS4YKP0CP2CFW6SEPWQ2CGVRWK5GHKDRV`, this is an account for the testnet. In Speed Spend you find your accounts (and a button to fill them with STX from the faucet) on the ][profile page](https://speed-spend.netlify.app/me).

Through the Blockstack authentication process, a user has two different stacks accounts:

- the owner stacks account that is derived from the private key and is only available in the authenticator app (Connect)
- the app stacks account that is derived from the app private key

The difference between the two is that the owner stacks account is read-only for the app, while the app stacks account is under full control of the app. The owner stacks account can only be used by the user via the Connect app. The stacks account is returned after authentication to the app in `userData.profile.stacksAddress`. Therefore, the app has read-only access to that account. All other interactions with that account needs to be delegated to Connect. The [connect library](https://www.npmjs.com/package/@blockstack/connect) provides the necessary methods for that.

The apps stacks account can be used without any explicit consent by the user. Transactions can be signed and submitted directly.

## Speed Spend and Hodl

In Speed Spend, the use of both accounts is shown on the [Speed Spend](https://speed-spend.netlify.app/speed-spend) and [Hodl](https://speed-spend.netlify.app/hodl) pages. It is all about transferring STX between accounts.

The Speed Spend page let you sent STX to other users (that have signed into the app once and published their public key). The public key is found through the Blockstack username and then used to derive the app stacks account of the other user. See [accounts.js](https://github.com/friedger/speed-spend/blob/ef56eb67afe420aa9b7e6a521210f247afba6fe8/src/lib/account.js)):

```
addressFromPublicKeys(
    AddressVersion.TestnetSingleSig,
    AddressHashMode.SerializeP2PKH,
    1,
    [publicKey]
  );
```

The [stacks-transaction library](https://www.npmjs.com/package/@blockstack/stacks-transactions) provides the method `addressFromPublicKeys`. Here, we just use a single signature account on the testnet.

The Hodl page let you transfer STX between your two Stacks accounts. The transfer from the user owned stacks accounts requires a confirmation from the user through Connect using `doSTXTransfer` from the `connect` library. See [OwnerAddressSpendField.js](https://github.com/friedger/speed-spend/blob/master/src/components/OwnerAddressSpendField.js).

![Hodl with Connect](https://github.com/openintents/openintents.github.io/raw/master/images/hodl-connect.png)

The app stacks account can send the transaction directly through `makeSTXTokenTransfer` and `broadcastTransaction` of the `stacks-transaction` library. See [SpendField.js](https://github.com/friedger/speed-spend/blob/master/src/components/SpendField.js).

## Profile

As mentioned initially, the [profile](https://speed-spend.netlify.app/me) page lists the account balances. They are retrieved using the `AccountsApi` object provided by the [stacks blockchain api client library](https://www.npmjs.com/package/@stacks/blockchain-api-client). See [accounts.js](https://github.com/friedger/speed-spend/blob/master/src/lib/account.js).

## Transaction Status

While we have now explored accounts, balances and transferring stacks, the last thing to do is to verify whether a transaction has completed sucessfully. It is the same procedure for all interactions with the stacks blockchain. A transaction id is created and you need to query the chain about details for the corresponding transaction.

The stacks blockchain api client library provides the tools for it. There is a `TransactionsApi` object that allows to retrieve transaction data, in particular `getTransactionById({ txId })` returns all the details if the transaction is known by the network. If not, the library provides a subscription method via websockets that recieves notifications if the transaction arrives at the network and if it was processed sucessfully or unsucessfully. The method is called `connectWebSocketClient`. The whole process is combined in the `TxStatus` component for Speed Spend and used on all pages. See [transactions.js](https://github.com/friedger/speed-spend/blob/master/src/lib/transactions.js).

## Flip Coin and Monsters

The interaction with smart contracts is explored on the "Hodl Token", "Flip Coin" and "Monster" pages. The details about fungible and non-fungible token, smart contract calls and Proof of Hodl login will be covered in an other post.
