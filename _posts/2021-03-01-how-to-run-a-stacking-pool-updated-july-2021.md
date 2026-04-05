---
title: "How to run a Stacking Pool? (updated July 2021)"
categories: blockstack
image:
  title: how-to-run-a-stacking-pool-updated-july-2021.jpg
---

### What is a Stacking Pool?

The Stacks blockchain uses the proof of transfer (PoX) consensus algorithm. It requires that Stack miners send Bitcoins to two randomly selected Bitcoin addresses each Bitcoin block. The more a miner sends, the higher the probability to win the Stacks block reward. The receiving Bitcoin addresses are picked from the list of Stackers. Stackers are users who hold a lot of Stacks and who are prepared to freeze their tokens for some time. The Bitcoin payouts are limited to 4000. These are called reward slots. Therefore, one stacker needs to provide 1/4000 of all frozen Stacks. If one stacker provides 2/4000 of all frozen Stacks, the user receives two payouts and so on. If users don't want to freeze the minimum amount, they can collaborate with other users and join a Stacking pool. One user, the pool admin, would receive the Bitcoins rewards for their collective stacking and distribute the rewards to the users. This happens according to the rules specific to each pool. 

Note: "Joining a pool" is the same as "delegating Stacks."

### Get started

As a pool admin, you have to go through the following procedure. The first three steps are done only once. The rest is repeated for each cycle.

- Make yourself familiar with the protocol.
- Make yourself familiar with the tools.
- Create a dedicated Secret Key for the pool, define your pool rules.
- Educate users about your offer, invite them to use your delegatee address in Stacks Wallet.
- Near the start of the cycle, collect the delegated stacks and lock their STX.
- Before the start of the cycle, finalize the delegation process with a commit transaction.
- During the cycle, observe your rewards and start at step 4 for the next cycle.
- At the end or after the cycle, do the payout.

### The Protocol

The protocol is described in the SIP-007 ([https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md](https://github.com/stacksgov/sips/blob/main/sips/sip-007/sip-007-stacking-consensus.md))

A few things to note that are relevant for pool admins:

- The required minimum of frozen Stacks is dynamic and can increase last minute. It only increases in steps of 10k STX.
- It is possible that your pool receives 0 Bitcoins because miners do not send any Bitcoins when it was your slot's turn, or your pool did not meet the required minimum of frozen Stacks.
- The more slots your pool has taken, the closer your payouts will be to the average payout.
- The pooling part of the protocol was added because Bitcoin transactions are expensive. Therefore, pools should find ways to optimize payouts, e.g. by bundling transactions over time or by using alternative payout methods.

The site Stacking Club ([https://stacking.club](https://stacking.club)) gives you a good insight into what happens during each cycle.

### The Tools

The PoX smart contract is the main tool. It provides the functions to stack the Stacks of your pool members. It is deployed at SP000000000000000000002Q6VF78.pox. The documentation is available at [https://docs.blockstack.org/references/stacking-contract](https://docs.blockstack.org/references/stacking-contract).

There are scripts to help you to deal with the tasks of stacking and committing Stacks:

[https://gitlab.com/riot.ai/clarity-pool-tools](https://gitlab.com/riot.ai/clarity-pool-tools)

### The Pool Rules

As the pool admin, you define the rules. They define who is allowed in your pool and how the payout happens. You can define a minimum or maximum amount of Stacks that users need to contribute, a minimum or maximum duration of cycles your pool members must stay in the pool and the way how stacking rewards are paid out. Make sure that users can find this information easily. Ideally, register your pool with the Pool Registry (still under development).

Your stacks address is referred to as "delegatee address".

### The Pool Members

Users just have to enter your delegatee address when following the delegation flow in the Stacks Wallet. That is all! You can't verify that they understood your Pool Rules.

### Stacking Their Stacks

Stacking your pool members' Stacks consists of

- collecting their details from the Stacks chain (maximum amount, duration, payout details)
- locking their Stacks by calling `delegate-stack-stx` for each of your members
- finalizing the pool stacking by calling `stack-aggregation-commit`

You can do step 2 and step 3 more than once as long as the total of the frozen Stacks is a minimum of around 50k STX (1/20,000 of the liquid supply).

The finalizing tx has to happen before the prepare phase of the next cycle starts.

You have to call the function `stack-aggregation-commit` for each cycle.

### The Rewards

You can find out how many slots your pool has taken once the reward phase of the cycle starts. The contract map "reward-cycle-pox-address-list" provides you with the total frozen stacks. Your total frozen Stacks divided by the minimum is the number of your slots. The minimum for the cycle is the total frozen Stacks divided by 4,000 rounded to the lower 10,000.

The rewards will arrive in your Bitcoin wallet at random blocks, the latest at the end of the reward cycle.

### The Payout

With the retrieved information during stacking, you can also do the payout. As this follows your pool rules, there are many variations. The simplest is to not payout at all if your pool is, for example, a charity pool. The tools above also contain helper functions for payout.

### Using a Smart Contract

By default, it is not possible to call functions of the pox contract from a contract. Users have to explicitly allow a contract to manage their stacking activities via `allow-contract-caller`. Users can withdraw their permission via `revoke-contract-caller`. [Boom](https://boom.money) and [Xverse](https://xverse.app) have implemented this. However, it introduces a step for Stackers that is not available in the Stacks Wallet for desktop.

### Pool Registry (added July 2021)

A [pool registry](https://stacks-pool-registry.pages.dev/) has been created that contains a registry of public pools as well as a basic UI to join pools using the Stacks Wallet for Web. Two types of pools are supported: 

- Pools using a simple `delegate-stacks` function call. These are all pools that use a standard address as pool address where users join these pools using the usual `pox` contract. The function is defined in the `pool-trait` trait of the pool registry.
- Pools using an extended `delegate-stacks` function call that additionally expects a payout address (as hash) and the user's preferred locking period. Examples are Boomboxes and Xverse.

### Improvements (updated July 2021)

By now, the Stacks Wallet for Desktop allows users to set the maximum number of cycles they want to participate in a pool. The Stacks Wallet for Desktop does not allow to set the address where the pool admin should send the partial rewards to. However, Friedger Pool uses the [contract `friedgerpool-payout-hints`](https://explorer.stacks.co/txid/SP2PABAF9FTAJYNFZH93XENAJ8FVY99RRM50D2JG9.friedgerpool-payout-hints?chain=mainnet) that contains a mapping between pool members and reward receiver addresses. 

The stacks node emits now events that allow the stacks node api to observe the rewards. For example, the following endpoint gives you all previous rewards slot for a give address: https://stacks-node-api.mainnet.stacks.co/extended/v1/burnchain/reward_slot_holders/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq

### Improvements II (update July 2021)

From the previous suggestion of improvements back in May, only 1 suggestion remains. It would be nice if the pox contract could provide functions to get the list of delegators and amount to stack. 

The Stacks foundation and infStones announced that they will invest more resource to improve the work of pool admins. Read more at https://stacks.org/infstones-supports-stacking
