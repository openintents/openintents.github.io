---
title: "An Application of Clarity Bitcoin Library"
categories: blockstack
image:
  title: an-application-of-clarity-bitcoin-library.jpg
---

The [Clarity Bitcoin Library](https://github.com/friedger/clarity-friedger-pool/blob/main/contracts/clarity-bitcoin.clar) initially created by Jude Nelson is a Clarity contract that allows to handle information from the Bitcoin blockchain. In particular, it allows to verify whether a transaction was actually mined on the Bitcoin blockchain. This is possible because the hash values of Bitcoin block headers are available in Clarity contracts via `get-block-info?`. Then, it remains to just verify hashes of merkle trees, transactions and block headers.

### Auditing a Stacking pool

The Clarity Bitcoin Library can be used to audit a Stacking Pool that pays out Stacking rewards in Stacks tokens, i.e. the pool receives Bitcoin rewards that are later converted to Stacks and, finally, distributed to the pool members. Pool members could report the reward Bitcoin transactions via a Clarity contract. The contract could then be queried about the expected payouts. The beauty of the contract is that all users can participate in the auditing. In a later step, the payout could be even automated based on the reported Bitcoin transactions.

In order to make this happen, the library was tested and improved. It turned out that it is currently not possible to destructure a Bitcoin transaction on-chain due to resource limitations for transactions. It makes more sense to parse the Bitcoin transaction off-chain and provide the parts as function arguments. In the verification function, the transaction can be reconstructed to create the transaction hash and verify it.

### User Interface

[Speed Spend](https://speed-spend.org/pool-audit) has been extended to include a simple UI for auditing a pool on testnet.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/zwmiYGAH1TvqQnoiKGqSV/WvwnZv7jPqp9KRPc4ss6--Screenshot from 2021-05-27 21-21-03.png)

As a user, you have to provide just the bitcoin transaction id (i.e. the hash of the transaction). All other details are retrieved from the bitcoin or stacks apis.

You should verify the provided transaction before submitting the transaction. All verification results are shown in the console.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/zwmiYGAH1TvqQnoiKGqSV/VQXwp9BFEENXb3J6l-shS-Screenshot from 2021-05-27 14-20-26.png)

The most important information is that the transaction could be verified as "mined" and how much Sats the pool received by the transaction. Both values are shown in the UI. All reported bitcoin transactions are listed as well.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/zwmiYGAH1TvqQnoiKGqSV/HvahBQB0UEHmoizeqoQ5k-Screenshot from 2021-05-27 14-22-16.png)

### Next Steps

With Stacks 2.1, there will be probably improvements for Clarity that makes handling Bitcoin more efficient. 

For the Pool auditing, the received sats will be converted via a price oracle and registered in the contract. Then, each user should be able to query to contract for their expected rewards for each cycle.

Known issues

- transactions with two reward transfers are not correctly handled. 
- transactions contained in a bitcoin block that was not used as anchor for a Stacks block can't be verified (flash blocks, [issue #2663](https://github.com/blockstack/stacks-blockchain/issues/2663))
