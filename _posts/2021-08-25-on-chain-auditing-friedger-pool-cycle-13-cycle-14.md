---
title: "On-chain Auditing Friedger Pool (cycle #13, cycle #14)"
categories: blockstack
image:
  title: on-chain-auditing-friedger-pool-cycle-13-cycle-14.jpg
---

[Friedger Pool](https://pool.friedger.de) is one of the larger Stacking Pools creating Bitcoin yields for more than 10m stacked STX. Friedger Pool does the payout in STX instead of BTC to reduce costs and more importantly to take advantage of [Stack's smart contracts](https://docs.stacks.co/write-smart-contracts/overview).

For cycle #13, Friedger Pool received 1.82519341 BTC. This can be verified on any btc explorer in tedious work or on the great [stacking.club in aggregated format](https://stacking.club/reward-address/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq/13):

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/MA3mBt0f-fwK2GxxG4JWY/jlVEfNRw27WWXhPosWtlc-Screenshot from 2021-08-21 00-23-54.png)

These were converted into 56,756.504155 STX and [distributed to 1138 pool members.](https://sendstx.com/cycle/13)

For cycle #14, [1.86358615 BTC](https://stacking.club/reward-address/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq/14) has been received, converted to 59,216.310614 STX and distributed to 1263 pool members.

The conversion rate is defined by the pool admin of Friedger Pool. I want to get rid of this step and introduced an [on-chain auditing contract](https://github.com/friedger/clarity-friedger-pool/blob/main/contracts/friedger-pool-wrew.clar) that mints wrapped BTC rewards on the Stacks blockchain. 1 sat received by pool from miners means 1 wrapped reward minted on the Stacks chain. The Friedger Pool wrapped rewards (FPWR) are SIP-10 tokens and are minted into the depot contract that manages the payout. Thanks to the [clarity bitcoin library contract](https://explorer.stacks.co/txid/SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.clarity-bitcoin-lib-v1) that is also used for the catamaran swaps, the wrapped rewards are minted only if the BTC reward transaction could be verified on-chain. There are tokens FPWR-v03 for cycle #13, and FPWR-v04 for cycle #14.

In a community effort, we verified all 845 BTC reward transactions for cycle #13 and minted 1.68265349 FPWR. The difference of 0.14253992 FPWR is caused by 70 transactions that were sent during so-called flash blocks. These are Bitcoin blocks without a corresponding Stacks blocks. These transactions can't be verified in Stacks 2.0. The upgrade to Stacks 2.1 ([#2663](https://github.com/blockstack/stacks-blockchain/issues/2663)) will allow to verify them as well.

For cycle #14, the focus was on payout of wrapped rewards and therefore, the tokens were directly [minted by the pool admin](https://explorer.stacks.co/txid/0xb6f24de21508c1e96ac3b8f8845b23713ef910be6002e5b2584fb45aadb483a8).

The wrapped rewards for cycle #13 or #14 do not have any value because the stacking rewards have already paid out earlier in STX.  Nevertheless, the on-chain auditing contract queried a price oracle for each verified transaction and reported the corresponding value in Stacks. The total for #13 was 60,051.872915 STX. Unfortunately, the oracle wasn't updated during cycle #13 and all transactions were evaluated with the last known price of 2802 sats/STX. Similarily for cycle #14, [66,549.665239 STX](https://explorer.stacks.co/txid/0xb6f24de21508c1e96ac3b8f8845b23713ef910be6002e5b2584fb45aadb483a8) were reported by the oracle.

The minted wrapped rewards have been assigned proportionally to the pool members minus 5% fees (1.59852088 FPWR-v03, 1.75499675 FPWR-v04). The fees of cycle #13 (0.08413259 FPWR-v03) have been assigned to the users who have verified the transactions. The rewards from flash blocks were not assigned. For cycle #14, the fees remain in the depot contract.

The tokens were not sent to the users directly because they do not have any value. However, users are invited to claim their rewards at [https://pool.friedger.de/members](https://pool.friedger.de/members) if they want to hold Friedger Pool Wrapped Rewards tokens version 04 in the "Claim Stacking rewards" section:

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/MA3mBt0f-fwK2GxxG4JWY/gP4hX_-TGoK1QO4fVBnx9-Screenshot from 2021-08-25 06-57-00.png)

The on-chain auditing is one step towards automating stacking pools. We learned that

- the smart contract for bitcoin transactions worked as expected and the numbers add up correctly.
- the UI to submit Bitcoin transactions work only for a small number of transactions and scripts are better tools to handle 500+ transactions.
- flash blocks are indeed a problem in Stacks 2.0.
- the UI and the depot contract (#13) had a bug and *lnow* fixed it.
- bitcoin block heights can't be verified on-chain. An oracle could be a solution until Stacks 2.1. Until then, it is not possible to automate the payout of rewards because the BTC transactions can't be assigned to stacking cycles.
- the price oracle is not reliable enough for production.

I would like to thank *lnow*, *harini*, *werner3141*, *bogachev*, *dcdigit* and the Stacks foundation for their engagement, help and support!
