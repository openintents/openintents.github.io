---
title: "Requirements for a Stacking Pool UI"
categories: blockstack
image:
  title: requirements-for-a-stacking-pool-ui.jpg
---

Currently, the tools used to run Friedger Pool is a set of 4 scripts. It requires hand holding and manual processing. In the following description all the bold text is what needs to be done manually. A UI for pool admins should allow to enter these parameters or calculate/suggest it for the admin. The process is as follows:

The first step is to get the delegation state considering various methods how user can delegate (**pox contract, pool-script, boombox**). The script gathers information about users that have delegated to the pool's **addresses**. The information is stored in a json file. In the first locking batch for a cycle all txs from block 0 are considered. In the next batches txs are considered that happened **after the block** of first batch run.

The second step is to lock STX according to the delegation settings of the user. The **current block height**, the **cycle id** and the delegation values are used to determine the parameters for the locking call. The fees are set to **96000** uSTX. This script can be run *again and again* until all txs are confirmed if the **nonce** of the first tx is provided.

The third step is to finalize the locking for the **upcoming** cycle. Appropriate **fees** need to be set.

Now, STX are stacked. From time to time, transactions of the reward address(es) should be **consolidated**. BTC needs to be **converted** to STX. Note, Electrum fails for addresses that have received from than 10k transactions.

The fourth step happens after the reward cycle has ended. It is about the payout of rewards. The script inspect all the successful locking transactions and filters them by **current cycle id**. A second filter is applied to **boombox **transactions because their payout happens later. For each stacker, the payout amount is calculated based on the **received rewards** and the current **exchange rate**. Similar to step 2, the script can be run *again and again* with the same **nonces** but increasing **fees** until all txs are confirmed.

A web UI could connect just to the stacks node and hold the information locally, like the [pool-tool scripts on gitlab](https://gitlab.com/riot.ai/clarity-pool-tools). However, connecting to the postgres DB of a stacks api node might enable more features.
