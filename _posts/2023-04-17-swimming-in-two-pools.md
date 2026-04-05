---
title: "Swimming in two pools"
categories: blockstack
image:
  title: swimming-in-two-pools.jpg
---

Upgrade of the Stacks blockchain to version 2.1, brought new stacking features. One of them is to increase the stacking amount while your STX are locked. This works for direct stacking and pooled stacking.

The implementation for pooled stacking allows to switch the pool while the stacked amount is increased. Look at the following transactions that can happen in one block or more:

- 

You delegate 100 STX to pool A.

- 

Pool A locks 100 STX for you.

- 

You delegate 300 STX to pool B.

- 

Pool B sees that you have already 100 STX locked and increases the locked amount by 200 STX

That means that for the upcoming cycle, you earn rewards for 100 STX with pool A and rewards for 200 STX with pool B.

That is fun!

However, it makes live harder for pool operators, in particular handling the payout. It is currently not possible to determine how much you are contributing to a pool through a contract call. The stacking info of pox-2 contract (`pox-2.get-stacker-info`) only provides that details about the last pool and the account info (`stx-account`) tells only about the total amount of locked stacked and locking period. That means there can’t be a stacking pool that distributes rewards automatically through a contract based on the locked amounts of all pool members.

If a pool wants to do automatic reward distribution, the pool needs to keep track of the locked amount for each pool member in its own stacking pool contract.
