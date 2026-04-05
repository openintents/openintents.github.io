---
title: "Customized Boombox Admin Protocol"
categories: blockstack
image:
  title: customized-boombox-admin-protocol.jpg
---

Boom has recently deployed a [smart contract](http://SP1QK1AZ24R132C0D84EEQ8Y2JDHARDR58R72E1ZW.boombox-admin-v3) that makes it really easy to create stacking pools. If you are new to stacking pools read for example [the docs about stacking](https://docs.stacks.co/understand-stacks/stacking) or the article about the [old way of running a pool](https://app.sigle.io/friedger.id/UOvy85BCSD-bjlrv_6q74). 

The new way is to deploy a simple NFT contract and then register it with the smart contract that was deployed by Boom. The contract is called `boombox-admin-v3` and the register function is called `add-boombox`. The function call contains all information about the pool: how many cycles the STX tokens are stacked for, when the stacking starts, what the Bitcoin reward address is and the minimum required delegation amount. Each registration of an NFT contract receives a unique Boombox id.

### Delegation

With this Boombox id, users select their preferred stacking pool. When calling the `delegate-stx` function of the Boombox admin contract, their STX tokens are immediately locked for the specified period. This is the same for all Boomboxes. 

Delegation is possible until 100 blocks before the start of the cycle. After that, one user has to finalize the cycle and send a `stacks-aggregation-commit` transaction. Currently, this has to be done via a script. In the future, this will be done in boom.money directly or the explorer's sandbox. The pool operator for all Boomboxes is the admin contract itself. The BTC rewards address of the pool is the key that distinguishes the pools.

### The First Pools

### Charity Cracker NFT

The Charity Cracker NFT is a Customized Boombox created by Boom. The rewards were directly sent to the [Bitcoin address](https://mempool.space/address/3MxgufNKFWeeMcsHHnotyjcwqRbsNu3bGv) of the Surfer Kids charity. Its Boombox id is 2. The first registration call was incorrect, therefore, Boombox id 1 did never participate in Proof of Transfer consensus.

The contract is deployed at [this address](https://explorer.stacks.co/txid/SP1QK1AZ24R132C0D84EEQ8Y2JDHARDR58R72E1ZW.charity-core-surf?chain=mainnet). 111 BTC reward yielding NFTs have been created. The pool was finalized for cycle #24 with [this transaction](https://explorer.stacks.co/txid/0xb1a45288ef385af0eafcb62df64f3b7196b71c25dc075d14631f8fdafbd76314?chain=mainnet).

### Grand Prize Winner Cycle #24

The NFT is the STX yielding Boombox distributed as Grand Prize of the 12 Day Holiday giveaway by the Stacks Foundation. The NFT joined Friedger Pool by using the same [Bitcoin reward address](https://mempool.space/address/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq). That means that Friedger Pool is responsible for the distribution of the rewards.

The contract is deployed at [this address](https://explorer.stacks.co/txid/SP3REDX8A1RFHSK0P0VE83HQ64TNTBQZ4V855KGPN.gp-bb-24?chain=mainnet). 1 NFT was created. The pool was finalized for cycle #24 with [this transaction](https://explorer.stacks.co/txid/0x3f796668c252422769ad05efee263c90a6c0935a97a44612f9d3784fec03fa35?chain=mainnet).

### Creating Your Own Pool

As pool creator, you should take care that the minimum amount of locked STX is reached. Otherwise, STX are locked but won't receive any rewards. The contract has a function `halt-boombox` that allows the creator of the Boombox to prevent more locking in case of an emergency.

As an pool creator, you only have to implement a small trait with the following four functions:

`(define-trait boombox-trait (
    (mint (uint principal uint {hashbytes: (buff 20), version: (buff 1)} uint) (response uint uint))
    (get-owner (uint) (response (optional principal) uint))
    (get-owner-at-block (uint uint) (response (optional principal) uint))
    (set-boombox-id (uint) (response bool uint))
  ))`

The function `get-owner` is the usual SIP-009 function for NFTs and useful during distribution of rewards. The same for `get-owner-at-block`. The implementation can be the same for all pools:

`(define-read-only (get-owner (id uint))
    (ok (nft-get-owner? charity-cracker id)))`

`(define-read-only (get-owner-at-block (id uint) (stacks-tip uint))
    (match (get-block-info? id-header-hash stacks-tip)
      ihh (ok (at-block ihh (nft-get-owner? charity-cracker id)))
      err-invalid-stacks-tip))`

The function `set-boombox-id` is called by the Boombox admin contract to inform the NFT contract about its id. The NFT contract should then verify the id during the `mint` call.

The `mint` call contains the following parameters: Boombox id, the stacker/pool member, the locked amount in micro-STX, the pool's Bitcoin reward address and the locking period. All this information can be used to personalize the NFT. The stacker is usually the recipient of the minted NFT. Note, that the protocol does not require to a real NFT, only the returned id of the `mint` call needs to be unique.

### Using the Boombox Admin Contract

The admin contract has utility functions like `nft-details-at-block` that provides information of the locked amount and about the owner at a given block. Even though it is a public function, the function can be called as read-only function:

`const result = await callReadOnlyFunction({
    contractAddress: "SP1QK1AZ24R132C0D84EEQ8Y2JDHARDR58R72E1ZW",
    contractName: "boombox-admin-v3",
    functionName: "nft-details-at-block",
    functionArgs: [
      uintCV(2),
      contractPrincipalCV(
        "SP1QK1AZ24R132C0D84EEQ8Y2JDHARDR58R72E1ZW",
        "charity-core-surf"
      ),
      uintCV(27),
      uintCV(42450),
    ],
    senderAddress: "SP1QK1AZ24R132C0D84EEQ8Y2JDHARDR58R72E1ZW",
  });`

The function call returns the owner of NFT 27 before it was transferred from `SP129E8GA4CTSZMQFTVY5V4HBY4K2T6A67PHSHRYN` to `SP343SNH3E14GAHSGGF2PH9PNN64DP5HFY9HT56AE` at block 42452. It also returns the locked amount of 50 STX.
