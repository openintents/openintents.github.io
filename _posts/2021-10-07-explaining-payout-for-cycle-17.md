---
title: "Explaining Payout for Cycle #17"
categories: blockstack
image:
  title: explaining-payout-for-cycle-17.jpg
---

### What happened?

During cycle #17, we decided to make a first payout of 1 BTC. The rate was 2758 sats/stx, resulting in  36,258.158085 STX as rewards (=1/0.00002758). As usual, we ran our payout script. However, we missed a manual update of a new part of the script. The result was that some stackers of cycle #18 received a payout already in cycle #17.

More precisely, we included all new stackers of cycle #18 who we locked during block #31859 and block #31905. That were 164 stackers with 2,075,821.824168 STX locked. The 164 received 4,651.902147 STX from the rewards of cycle #17. A run of the payout script in dry run mode returned that number. And the following calculation confirms the amount (minus rounding):

total rewards × cycle #18 stacker locked stx / total paid locked stx = cycle #18 stackers rewards
36,258.158085 × 2,075,821.824168 ÷ 16,179,505.406138 = 4,651.902142

That means we paid only 31,606.255938 STX to the stackers of cycle #17. That were 0.87170053 BTC.

We apologize for this error! We introduced better logging and will continue to work on a better automated pool.

By now, cycle #17 is completed and we received a total of 1.80116109 BTC. (You can verify by checking the rewards address as described for example on [reddit](https://www.reddit.com/r/Bitcoin/comments/bjgqkm/historical_balance_lookup/) or at [stacking.club](https://stacking.club/cycles/17)). The second payout is therefore 0.80116109 BTC plus the missing 4,651.902142 STX. At the current rate of 2534 sats/stx, the BTC convert to 31,616.459747 STX. The total of the second payout is therefore 36,268.361889 STX.

### Background

The Stacks blockchain miner software received an update during cycle #15 that changed the way how transactions were processed. Before the update, transactions were processed mainly in chronological order. We could send our stacking transactions in batches using the pool-tool smart contract and eventually the transactions were processed. With the update, a fee market was created. Transactions are now processed with optimization for getting transactions fees in relation to transaction size. This moved our big batch transactions to the end of the queue. During processing stackers for cycle #16, we decided to switch to individual processing of the stackers using the PoX contract, making the transactions smaller and more likely to be processed.

Unfortunately, the  PoX contract does not provide the start cycle for the locking period. We decided to manually add this information in our scripts. While we did that for cycle #16 and #17, we missed to add the cycle information for #18 ([gitlab issue](https://gitlab.com/riot.ai/clarity-pool-tools/-/issues/1)) resulting in the problem described above.
