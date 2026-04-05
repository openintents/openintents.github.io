---
title: "FAQ: Pooled stacking"
categories: blockstack
image:
---

## Common FAQ

### Is there a way to confirm that stacking for delegates went correctly?

If your stx is loocked it is a good sign. Check also that your delegate-stx transaction was successful and that your pool admin locked your stx. You can see your status at https://lockstack.com/pooled-stacking-info

### How can I increase the locked amount. It says that I need to stop pooling if I want to increae the amount, will this mean I will miss 1 cycle?

When you are already a pool member, you can increase the locked amount for the next cycle by stop pooling and then delegate a higher amount. Then the pool operator can lock more for the upcoming cycles until the end of the current locking period.

While you stop pooling, your currently locked STX will continue to earn rewards for the current cycle.

### How can I change the stacking pool?

Just revoke delegation and join the new pool. Delegate a little higher amount, then the new pool operator can make you join the pool with the difference for the next cycle and with the full amount after the locking period with the existing pool.

### What is the difference between stacking stx and committing stx?

Stacking st is used by direct stackers. We can also say that pooled stacker are stacking stx as part of a pool.

Committing stx is an action by the pool operator. The pool operator locks stx for their pool members, these are registered as partially stacked stx. Only if the pool operator commits these partially stacked stx will then these stx will start to earn rewards.

## Fast Pool FAQ

### With Fast pool, will my STX not be automatically stacked for the following cycle?

No, there is no automatism. However, anybody can do it for you. Therefore, it is easy to install a script or ask friend and family to extend stacking for you. User, let’s call them Pool Helpers, can do it for you.

For other pools, pool operators extend your stacking.

### How can I compound stacking rewards?

Make sure that you delegate a higher amount than your current balance. After you received your reward extend for 1 cycle. Fast Pool will automatically use the new balance for the next cycle.

## Whale FAQ

### How can I do stacking from my cold wallet?

You can create your own pool and use a hot wallet to operator the pool. The stacker is the cold wallet. Thereby, only 1 transaction (pox-3.delegate-stx) is needed from cold wallet.

- 

Delegate from cold wallet to a hot wallet (pox-3.delegate-stx).

- 

Sign in first with your hot wallet on https://lockstacks.com, then visit [https://lockstacks.com/pool-admin/delegate-stack-stx](https://lockstacks.com/pool-admin/delegate-stack-stx) and lock stx tokens for all cold wallets

- 

[Use the hot wallet to finalized each cycle https://lockstacks.com/pool-admin/stack-aggregation-commit ](https://lockstacks.com/pool-admin/stack-aggregation-commit)for each reward cycle.

- 

And to continue stacking (given new feature in 2.1) you can just extend the locking from hot wallet for more cycles on [https://lockstacks.com/pool-admin/delegate-stack-extend](https://lockstacks.com/pool-admin/delegate-stack-stx).

###
