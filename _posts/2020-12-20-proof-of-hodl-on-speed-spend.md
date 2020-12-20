---
title: Proof of Hodl on Speed Spend
subheadline: Authenticate and Authorize with Hodl token
categories: blockstack
image:
  title: proof-of-transfer.jpg
---

The Stacks authentication flow in apps is a solution to move away from using rented accounts owned by big tech companies. It allows applications to handle user data distinctively and securely while keeping the identity of the user private.

This works well for applications that handle user data in the name of the user. However, there are applications and use cases where the anonymous authentication is not sufficient. For example, applications that have different roles or that handle service subscriptions, they require some known user identifier that can be sent to the service providers for verification. This identifier is often an email address, an identifier for communication. Email addresses are not designed to be used for subscription verification. How should an identifier look like and what properties should it have?

The Stacks authentication provides a cryptographic key that can help here. The application receives a proof of ownership of the key, then the application can verify whether certain actions have been done with this key without requesting further personal details.

In Speed Spend, such a verification was added to the flip coin game. It is required that the user has locked at least 1000 microStacks or the user is hodling 10 tokens before playing the game. The locking is a simple Stacks transfer and was described in the [introductory article](2020-09-15-introduction-to-speed-spend). For hodling tokens, a contract call needs to be performed. This was explained in the [article about contract calls](2020-12-11-contract-calls-on-speed-spend).

The verification for the locked tokens is just a check for the balance of the app user address, that is the address that belongs to the app private key.

The function below `getStacksAccount` calculates the Stacks address from a private key. Then the `AccountsApi` is used to retrieve the Stacks balance for this address.

```

function getStacksAccount(appPrivateKey) {
  const privateKey = createStacksPrivateKey(appPrivateKey);
  const publicKey = getPublicKey(privateKey);
  const address = addressFromPublicKeys(
    AddressVersion.TestnetSingleSig,
    AddressHashMode.SerializeP2PKH,
    1,
    [publicKey]
  );
  return { privateKey, address };
}

...

const balance = await accountsApi
    .getAccountBalance(
      { principal: getStacksAccount(userData.appPrivateKey).address })
if (balance) {
  const stxBalance = balance.stx;
  const balanceAsNumber = parseInt(stxBalance.balance, 16);
}

```

The code above is part of the `BetButton` component of Speed Spend. It also contains the check for the hodl token balance. This value can be retrieved directly from a read-only function of the hodl token contract:

```
(define-read-only (hodl-balance-of (owner principal))
  (ft-get-balance hodl-token owner)
)
```

In the app, the call to the read-only function is done using `callReadOnlyFunction` with the stx address of the user, not the app stx address.

```
const hodlBalanceCV = callReadOnlyFunction({
    contractAddress: CONTRACT_ADDRESS,
    contractName: HODL_TOKEN_CONTRACT,
    functionName: 'hodl-balance-of',
    functionArgs: [cvToHex(standardPrincipalCV(stxAddress))],
  })
```

If this value is greater or equal to 10 then the player has hodled enough token and can play the game. For Speed Spend, the verification unlocks part of the user interface of Speed Spend. It provides a business model for the UI part of the app. Users that don't want to invest in Speed Spend can still use the smart contract of Flip Coin and participate in the game. However, it is possible to include similar verifications in smart contracts itself or also on aggregation servers for the best players or so.

The nice things of these proof of hodl verifications is that the user is in control of investment or subscription. If the user decides to transfer the hodl tokens to a different user it does not change anything for the app developer. There is no need to update accounts or credit card details.
