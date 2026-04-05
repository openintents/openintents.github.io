---
title: "Upcoming: NPM package for Clarity bitcoin lib"
categories: blockstack
image:
  title: upcoming-npm-package-for-clarity-bitcoin-lib.jpg
---

One of the most interesting properties of the [Stacks blockchain ](https://www.stacks.co/)is the view of their nodes into the state of the Bitcoin blockchain. The view is available in the smart contract language and it is possible to verify on-chain that a Bitcoin transaction was actually mined as described earlier in [this post](https://app.sigle.io/friedger.id/zwmiYGAH1TvqQnoiKGqSV).

The main part of the verification is implemented in a library contract ([clarity-bitcoin-lib-v1.clar](https://github.com/boomcrypto/clarity-deployed-contracts/blob/main/contracts/SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9/clarity-bitcoin-lib-v1.clar))

I reviewed an early state of a library that helps web developers to use the library. The git repo is here: [https://github.com/web3devs/stacks-bitcoin-api](https://github.com/web3devs/stacks-bitcoin-api)

It helps to build the parameters required to call a Clarity smart contract that uses the bitcoin library contract. Any Bitcoin transaction can be verified that has 4 or less input parameters and 4 or less output parameters.

There are a few open issues to finalized the library that hopefully will be resolved in Q3 2022.

The library is built with the support of [Stacks grant #426](https://grants.stacks.org/dashboard/grants/426).
