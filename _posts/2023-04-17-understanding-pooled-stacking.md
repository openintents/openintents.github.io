---
title: "Understanding Pooled Stacking"
categories: blockstack
image:
---

## Amounts

### DedeDelegated Amount (aka Pooled Amount)

The delegated amount is the maximum amount of STX that the pool operator can lock for the user. It is the first amount set by the user. I can be higher than the current balance. Eventually, the pool operator can never lock more than the minimum of the delegated amount and the user’s balance.

### Locked Amount

The locked amount is the actual amount of STX that the pool operator locked for the user for a certain locking period. During the locking operation by the pool operator the locked amount is never higher than the locked amount. However, the user can change the delegated amount afterwards by revoking and re-delegating. Furthermore, the pool operator can increase the locked amount for the remaining locking period. Therefore, the locked amount can be higher or lower than the delegated amount.

### Stacked Amount (aka Earning Amount)

After locking the users’ STX, the pool operator has to commit the total amount, only then the locked STX will earn rewards for the upcoming cycles. The pool operator has to do the commit for each cycle. With the commit transaction, the locked amount becomes the stacking amount for a reward cycle and earns rewards during that cycle.

Users can have locked STX that are not yet earning e.g. before the first cycle in the pool. When the pool operator increases the locked amount, then the user can have both an earning amount from previously locked amount and a non-earning amount that will start earning rewards for the next cycle(s) only. Therefore, the stacked amount can be smaller than the locked amount.

## Actions

### Delegate STX (user)

The user gives permission to a pool operator to handle the stacking rewards. The user can only delegate to one pool at a time. However, it is possible for the user to change the delegation while their STX is locked.

### Lock STX (pool operator)

The pool operator locks the user’s STX for a given locking period. The STX will unlock and become liquid again automatically after the locking period unless the locking period is extended by the pool operator.

### Commit STX (pool operator)

The pool operator aggregates the individual locked amounts of the pool members and commits these for stacking

### Earn rewards

This happens automatically. Rewards are paid in BTC to the pools BTC reward address.

### Payout (pool operator)

 The pool operator determines the shares each pool member receives and send their share of the rewards to their accounts

### Extend locking (pool operator)

The pool operator can extend the locking period of a pool member up to a maximum locking period of 12 cycles. If the user’s STX is locked for another 5 cycles, then the pool operator can extend for 7 cycles.

### Increase locking (pool operator)

The pool operator can increase the locked amount up to the minimum of the delegated amount and the user’s balance. The new locked amount will be applied from the next cycle onwards.

### Revoke (user)

The user revokes the permission for the pool operator to handle stacking rewards in the future. The current stacking is not affected.
