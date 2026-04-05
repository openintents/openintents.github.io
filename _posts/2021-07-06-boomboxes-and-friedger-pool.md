---
title: "Boomboxes and Friedger Pool"
categories: blockstack
image:
  title: boomboxes-and-friedger-pool.jpg
---

TDLR : Boombox pool rules are

- Delegation through contract SP497E7RX3233ATBS2AB9G4WTHB63X5PBSP5VGAQ.boomboxes-cycle-12
- Immediate locking when delegating
- Locking period: 1 cycle
- Bitcoin reward address: Friedger Pool's address
- NFT ownerships at block height #24,000 determines reward receivers

### Introduction

The Stacks blockchain allows users to contribute to the network by stacking their Stacks tokens. Some users use a Stacking Pool like [Friedger Pool](https://pool.friedger.de), [Xverse](https://www.secretkeylabs.com/) or [PlanBetter](https://planbetter.org/) to stack with a group of users. These pools usually pay out rewards at the end of each cycle. In order to provide liquidity for these rewards, the [Boom wallet](https://boom.money) allows users to create Boomboxes. These are non-fungible tokens (NFT) that represent the rewards of a user's stacked Stacks. The user can trade these freely before the rewards are paid out. Whoever owns the NFT at the end of the cycle will receive the payout. This gives the NFTs an intrinsic value until the cycle ends. A detailed description about how to create a Boombox was published a while ago on [Boom's blog](https://boom-wallet.medium.com/how-to-get-your-first-boombox-d97a9404e759).

The first Boomboxes can be created for the current [cycle #12](http://stacking.club/cycles/12). The [Clarity contract](https://explorer.stacks.co/txid/SP497E7RX3233ATBS2AB9G4WTHB63X5PBSP5VGAQ.boomboxes-cycle-12?chain=mainnet) defines the (SIP-9 compatible) NFT and acts as the pool administrator of Friedger Pool. 

### Delegation

Users interact with the contract through the `delegate-stacks` function. This function does three things: 1) The NFT is minted for the user. 2) The user's Stacks tokens are delegated to Friedger Pool using the Boombox contract as pool address. 3) These delegated stacks are locked by the Boombox contract. For cycle #12, the **locking period is 1 cycle**.

All three actions happen in one transaction. Usually, step 2) is done by the user using the Stacks Wallet for Desktop. Step 3) is done by the pool admin shortly before the begin of the next cycle. Here, the locking happens immediately when the Stacks tokens are delegated to the pool. Users don't have to trust the pool admin to correctly lock their Stacks.

The delegated stacking protocol requires a final step to enable rewards for the next cycle: All locked Stacks have to be aggregated and committed before the start of the cycle. The aggregated amount has to be at least a little bit more than 57,000 Stacks according to the protocol. One user has to call the `stack-aggregation-commit` function of the Boombox contract. This can only happen 200 blocks before the start of the cycle, that is after Bitcoin block 690950. This block is also the deadline for Boomboxes. After that block, they can't be created any more.

### Payout

The Boombox contract uses the **bitcoin address of Friedger Pool** ([33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq](https://mempool.space/address/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq) corresponds to the hash `0x13effebe0ea4bb45e35694f5a15bb5b96e851afb` and version `0x01`). That means that Boombox users trust Friedger Pool to correctly convert the Bitcoin rewards to Stacks and distribute them proportionally. For Boomboxes, the rewards will be paid out by Friedger Pool to the owners of the NFT around the end of cycle #12. The block is fixed to **Stacks block #24000** - after the reward phase ended at bitcoin block 693250.

Cycle #12 is a first iteration of Boomboxes. Every second cycle, a new Boombox will be released that users can sell, use as in-app payments or for other use cases.
