---
title: "Testing Stacking Pool 2.1"
categories: blockstack
image:
---

Stacks 2.1 brings some changes to stacking, in particular it is possible to avoid cool down cycles and to increase stacking amount during locking periods. Here is a description of all the tests for these features when used with a stacking pool.

For the tests with use the 2.1 testnet maintained by Hiro Systems. Make sure to set the correct network in the explorer.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/4CFjUnkT9NaRf50ALrIbt/bZ8-h_GQ1QT6iq4-4GUjF-Screenshot from 2023-02-01 10-33-55.png)

The testing pool use the following settings:

- 

The pool stacking address is [ST21815DY1QZWV6NAPCDE54BMHE10WK8HB2QXBNDT](https://explorer.stacks.co/address/ST21815DY1QZWV6NAPCDE54BMHE10WK8HB2QXBNDT?chain=testnet&api=https://2-1-api.testnet.hiro.so).

- 

The pool rewards address is a native segwit address (supported since 2.1): [https://mempool.space/testnet/address/tb1qs2qft0sdllxe424nrt3fzaytsg8y6y2cplaylj](https://mempool.space/testnet/address/tb1qs2qft0sdllxe424nrt3fzaytsg8y6y2cplaylj)

- 

All stacks are locked for only 1 cycle at a time and re-stacked until pool membership is revoked.

From cycle 5, 820m STX were stacked so that PoX consensus is active. There are two pool members:

- 

Alice: [ST3GKDW24KN9KVY49DG20MJ39DQMH1Z4DJT7C7MFT](https://explorer.stacks.co/address/ST3GKDW24KN9KVY49DG20MJ39DQMH1Z4DJT7C7MFT?chain=testnet&api=https://2-1-api.testnet.hiro.so) (5.2m STX)

- 

Bob: [ST1BY17KAGWQYYZ3TST4CANW0AJFN80YY931DJTK2](https://explorer.stacks.co/address/ST1BY17KAGWQYYZ3TST4CANW0AJFN80YY931DJTK2?chain=testnet&api=https://2-1-api.testnet.hiro.so) (100+ STX)

## Actions by Users

During cycle 4, Alice and Bob delegated to the pool as usual before the start of cycle 5. Alice delegated 5.2m STX, Bob 100 STX in a first transaction. Later, Bob delegated 105 STX.

For cycle 6, Bob uses a helper function to [revoke and delegate in one transaction](https://2-1-api.testnet.hiro.so/extended/v1/tx/0x565efae37787f86db7c4e5d6cb837d6ea27fbb024b1d28c3eae78b54f41eccc3). **NOTE**, that Bob needs to call `allow-contract-caller` first to enable delegation through the helper contract.

## Step 1: Get Pool Members

To find pool members, we need to check calls to `delegate-stx` on contract `pox-2`. The delegation state can be looked up using the delegation map as in Stacks 2.0.

An improvement is under development that would result in specific events for when a user delegates stx using any contract call or even a specially crafted bitcoin transaction. During the tests, this feature was not yet available.

## Step 2: Stacking

### First time members

This works as in Stacks 2.0. Depending on the user’s balance and the minimum requirements, the appropriate stacking amount is locked using `delegate-stacks-stx`.

For cycle 5,

- 

we [locked 5.2m STX](https://2-1-api.testnet.hiro.so/extended/v1/tx/0xc7cbe51a3810d9b5db762fe6f125141702619a0bff556e7479dcc530f7c1851d) for Alice for 1 cycle.

- 

we [locked 100 STX](https://2-1-api.testnet.hiro.so/extended/v1/tx/0x3623325d11a77aee92dd3a9161ca7d60af758d65ed67ca87d1a0c990e94e1896) for Bob for 1 cycle. (Note, that this happened after a first stack-aggregation-commit call. See Step 3.)

For cycle 6, no new members were added.

### Member wants to add more — increase

After Bob’s STX were locked, he noticed that there are more liquid STX. He asked to lock more for cycle 5. In Stacks 2.1, it is now possible!

For cycle 5, we [increased the locked amount](https://2-1-api.testnet.hiro.so/extended/v1/tx/0xb6028b1ebfd65e3432252ca52530710ce13a079115d9e9b06d979ce8e41f0321) for Bob by 5 STX (`delegate-stack-increase`) after the delegated more STX.

For cycle 6, Bob has increased the delegation to 106 STX. We locked the amount during the extend call (see below).

### No more cool down cycles — extend

For cycle 6, we want to lock the same amount for Alice and Bob again. In Stacks 2.0, there would be a cool down cycle. In Stacks 2.1, we can extend the locking period during cycle 5.

For cycle 6,

- 

we [extended the locking period](https://2-1-api.testnet.hiro.so/extended/v1/tx/0x5b11c87f6364a0e07ec5a41bf3911d8c2e864140d05eeb98cfa24a91227cba05) for Alice by 1 cycle (`delegate-stack-extend`). The stacking amount is unchanged (5.2m STX).

- 

we [extended the locking period](https://2-1-api.testnet.hiro.so/extended/v1/tx/3fa93b194ac96697f418ec76343a3fbbef318369324bb3438165b3091cf8929c) by 1 cycle for Bob and increased the locking amount by 1 STX in **one** transaction using a [helper contract](https://explorer.stacks.co/address/ST21815DY1QZWV6NAPCDE54BMHE10WK8HB2QXBNDT.pox-2-pool-admin-helper?chain=testnet&api=https://2-1-api.testnet.hiro.so) `pox-2-pool-admin-helper-2` that combines the extend and increase calls.

**NOTE**: The helper contract makes **first** a calls to `delegate-stack-extend` and **then** to `delegate-stack-increase`. With the 1 cycle locking period, the increase call would fail with `err 2` due to the unlock height in the next cycle.

## Step 3: Finalize Cycle

With Stacks 2.1, we add members to the pool even after we have already finalized a first batch. There is now the function `stack-aggregation-commit-indexed` that returns an index of the pool slots. This index can be used for adding more STX to the pool for the next cycle.

For cycle 5,

- 

we [finalized the first batch](https://2-1-api.testnet.hiro.so/extended/v1/tx/0x39c5fe515ab9501bf9ba5732eb361b1cecb2320886ed3e10363952d102879c49) with Alice as we hit the minimum locked STX of 5.2m STX. We used the new function and received as result value the pool’s index `3`.

- 

we [finalized the next batch](https://2-1-api.testnet.hiro.so/extended/v1/tx/0x4f0bc2dee7fbb0a42c8d56fac2b346db4bb4ba94f2570f764571440a2aefa812) by increasing the locking amount by all the newly added STX from Bob for cycle 5 using function `stack-aggregation-increase` with the pool’s index `3`.

- 

the total amount stacked was 5,200,105.00 STX.

For cycle 6, we [finalized the cycle](https://2-1-api.testnet.hiro.so/extended/v1/tx/https://2-1-api.testnet.hiro.so/extended/v1/tx/0x236c42ecf98b1d8cb55ac7462cc3ea18d3bb1b7c51d85187e31838c614cde05b) as usual using function `stack-aggregation-commit`. Therefore, we were not able to add more STX to the cycle at a later time. The total of 5,200,106.00 STX were stacked for cycle 6.

## Step 4: Payout

During the tests, we didn’t distribute rewards. However, the bitcoin explore shows that we have received some tBTC for 1 slot as expected.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/4CFjUnkT9NaRf50ALrIbt/fj7PsSO4lBrJMQ14u0Xwa-Screenshot from 2023-02-01 11-09-24.png)

## Learnings

We managed to use the new scripts for two pool members. The scripts are not yet optimized for thousands of users.

Reasons why contract calls failed:

- 

the chain was not live, the single miner ran out of tBTC and stopped mining. This was not immediately noticed by us and we sent transactions that failed due to wrong block heights.

- 

helper contracts were not enabled through `allow-contract-caller`.

- 

`delegate-stack-increase` was called for users in their last locking cycle. With the 1-cycle model of most stacking pools, `delegate-stack-extend` needs to be called first for existing pool members.

- 

the call was made to `pox` instead of `pox-2`. The error is shown as `(err none)`.

(header image by [caroline voelker](https://unsplash.com/@carolinevoelker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/pool-urban?orientation=landscape&utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))
