---
title: "How to run a Decentralized Stacking Pool?"
categories: blockstack
image:
---

### Update May 2023 

Stacks 2.4 has been published. The pox contract is now version 3 (pox-3) and the pox-pool-self-service has been updated to version 2 to fix an issue with extending more than 1 cycle.

### Note

This is an rewrite of the first article from July 2021 about running a Stacking pool in general. That article can be found here: [https://app.sigle.io/friedger.id.stx/UOvy85BCSD-bjlrv_6q74](https://app.sigle.io/friedger.id.stx/UOvy85BCSD-bjlrv_6q74) There is also a Pooled Stacking [glossary](https://app.sigle.io/friedger.id/MtU8D4thkohi5TVKBKIy_) and a [FAQ](https://app.sigle.io/friedger.id.stx/MeBQ49LDcr_ZD_afEwOwH).

## Decentralized Stacking Pools (nearly)

Running a stacking pool has become much easier. The experience with Boomboxes and the hardfork of Stacks 2.1 allowed us to install a smart contract that does most of the actions of a pool operator.

To join a decentralized pool, users have to delegate to a smart contract address, not to a standard address that is owned by a single entity or a small group of users (multisig). The smart contract is owned by all and nobody.

### Decentralized Pool Member management

Pool members do not rely on a single entity that approves joining a pool or locking their stacks or so. All this is handled in a decentralized way by the smart contract.

Users can either delegate STX to the smart contract via the normal PoX-2 contract or call the delegate-stx function of the smart contract. This function will do the delegation and all the steps that the pool operator usually does. These steps are locking your Stacks tokens and committing them, all in one function call. There is a second function that does only the pool operator steps. This function can be called by anyone for anyone with some security rules defined in the smart contract.

The smart contract has been published on this [git repo](https://github.com/friedger/clarity-stacking-pools) and the web app [lockstacks.com](http://lockstacks.com) has integrated the contract so that the contract can be easily used. The web app gives the user the option to leave the pool, to extend the pool membership without cool down cycle and increase the stacking. A more detailed description how this can be done is described [in this article](https://app.sigle.io/friedgerpool.btc/aDpIH4Ntbvt_D74GX1HjH).

### Reward admin

Stacking rewards are paid in Bitcoin to a reward address that is defined in the smart contract. This BTC reward address is owned and controlled by the so-called reward admin. The duty of the reward admin is to distribute the rewards. Each stacking pool can setup its own rules about fees, how the rewards are distributed, etc. The nice thing is that the payout is independent of the smart contract of the pool. That means that a new decentralized stacking pool can re-use the existing pool smart contract with minor adaptions.

## Instructions

To start your own decentralized stacking pool you can follow these steps

- 

Setup a website that clearly states the pool’s rules, most importantly decide and communicate your payout rules (see below).

- 

Use the favourite tool to edit code, the easiest is to import the git repo into Hiro Platform.

- 

In the editor, choose contracts/pox-pools-self-service.clar and

update the `pool-pox-address` to your own btc reward address.

- 

change the stx-buffer that determines how much stx is not locked if the delegation amount is higher than the actual balance

- 

Then deploy the contract and send a PR to have the pool included in [lockstacks.com](http://lockstacks.com)

- 

Teach your prospective pool members how they can manage their pool membership.

The smart contract for all pools should be the same or nearly the same for all pools so that users can verify the pools more easily.

Feel free to contact me if you need support.

### Payout Rules

- 

Reward admins can distribute the rewards manually in BTC or STX. For STX, some scripts have been published at [https://gitlab.com/riot.ai/clarity-pool-tools/-/tree/feat/2-1](https://gitlab.com/riot.ai/clarity-pool-tools/-/tree/feat/2-1)

- 

Reward admins can deposit future rewards in a wrapped BTC token or STX and let pool members claim their share of the rewards. The reward admin would receive their rewards as unwrapped BTC. This was proposed in grant [CB-23Q2-02.1 : Decentralized Staking Pool.](https://github.com/stacksgov/Stacks-Grant-Launchpad/discussions/844)

- 

Mini-sBTC is a payout rule where several reward admins provide liquidity for wrapped BTC and are incentivized to distribute stacking rewards. This is work in progress. See [https://github.com/Trust-Machines/core-eng/issues/278](https://github.com/Trust-Machines/core-eng/issues/278)

- 

Think of your own fair rules…!

Some payout rules can be implemented in a smart contract. The most difficult part is the bridging the BTC reward to the STX blockchain.

## Comments about Fast Pool v1

Fast Pool is the replacement of Friedger Pool. Friedger has now stepped down as pool operator and acts only as reward admin.

164 pool members joined for the first cylce #56, 355 pool members for cycle #57. 10 users have used the self-service function for other users to help them with their stacking in the pool.

The website [https://pool.friedger.de/cycles](https://pool.friedger.de/cycles), [https://pool.friedger.de/payouts](https://pool.friedger.de/payouts) and [https://app.sigle.io/fastpool.btc](https://app.sigle.io/fastpool.btc) give more details about activities and payouts.

### Improvements

The smart contract does not handle cases when users swim in two pools. A new version should keep track of the locks stx internally and it should have a getter so that a reward payout contract can calculate the share for each pool member.

The smart contract does not correctly protect users from locking for more than the next cycle.

The instructions how to setup a decentralized stacking pool are still long. The smart contract could be improved so that reward admins can call a function to initialize the contract.

More payout rules should be implemented and run by more reward admins.

Prospective pool members should be better educated what a decentralized stacking pool is, e.g. by integrating the glossary and FAQ into lockstacks.com
