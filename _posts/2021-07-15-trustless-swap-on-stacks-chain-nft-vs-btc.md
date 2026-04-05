---
title: "Trustless Swap on Stacks chain: NFT vs $BTC"
categories: blockstack
image:
  title: trustless-swap-on-stacks-chain-nft-vs-btc.jpg
---

When Boom launched Boomboxes, I [minted](https://explorer.stacks.co/txid/0x091ec2e15e7d14e89569d692dfaf05830b84b1a5975d9f15ea9a3fe744c8b7ff?chain=mainnet) number #82 of 1st Edition. Boombox NFTs come with an intrinsic value because these NFTs earn stacking rewards. (Read the details [in my previous post](https://app.sigle.io/friedger.id/q-UHdutKP7wxrQm72QtUy).) I participate in the consensus algorithm (PoX) of the Stacks chain by locking my Stacks. I locked 16,999 STX for around 3 weeks when I minted the NFT. On testnet, I exercised a trustless swap between stacks and bitcoins. Now, I would like to swap this NFT, Boombox b-12 #82 for Bitcoins on mainnet. The associated art work is the image of the post.

I am looking for offers! Deadline** **20th July 2021, 1am UTC. 

If interested read on and please ping me on Twitter @fmdroid or Discord @friedger.btc#0185 with your offer and your STX address or [.btc name](https://btc.us). Note, that 1) the swap must have happened before stacks block #24,000 and 2) BTC transfer fees are paid by the buyer.

**Update 23 July:** I am not looking for offers any more. 
   1. The swap rules were created with [this create-swap transaction](https://explorer.stacks.co/txid/0x70578fa63b28659b9fdcadc77d096b70d6789f0e4c92304d9e14325af5dcb0d8?chain=mainnet).
   2. BTC payment happened: [0x0cd84f2eff7ffb77fb45de32690d97b95dd3d8f3a24a3f448a37df3708f2f119](https://www.blockchain.com/btc/tx/0cd84f2eff7ffb77fb45de32690d97b95dd3d8f3a24a3f448a37df3708f2f119)
   3a. BTC payment was rejected on Stacks chain [with incorrect amount](https://explorer.stacks.co/txid/0x38e2f50a4c410e2835a3497d0a7f68c2e81150a3f95956333c31d7b68beb647b?chain=mainnet).
   3b. BTC payment was verified on Stacks chain [with correct amount](https://explorer.stacks.co/txid/0x5c275f52078374fb1ff68266034ce83e8cfe144cfb239f0d10c8f626b0b2e431?chain=mainnet).

  This type of swap shall be called catamaran swap because - unlike [submarine swap](https://wiki.ion.radar.tech/tech/research/submarine-swap) - the two parts happen on-chain, just two different chains.

### Evaluating NFT b-12 #82

Previous stacking rewards shown at [Stacking Club](https://stacking.club/cycles/11) suggests that we can expect around 0.016 BTC per reward slot. Looking at the current competition between miners, this amount could increase. However, the price of STX/BTC is not predictable for me, therefore, the reward amount could decrease. 

There were 96 Boomboxes, 1st Edition minted. The total locked value for these Boomboxes is 113k STX. I used a scripted that parsed the `delegate-stx` contract calls. This amount is just above the price for 1 stacking reward slot in cycle #12. Therefore, we can estimate that my 17k STX would get are around 15% of 1 reward slot.

### Trustless Swap

Swapping the NFT for Bitcoins works with a [Clarity](https://clarity-lang.org) smart contract on the Stacks chain that has knowledge about the Bitcoin blockchain. The contract contains the NFT id (#82), the buyers Stacks address, the agreed bitcoin price, my bitcoin address and a time limit.

Once the contract is deployed, I will transfer the NFT to the contract in escrow. Then the buyer transfers the agreed price (or more) to my bitcoin address. Everybody can watch the Bitcoin blockchain for such a transaction and submit it to the contract. The contract will verify it by recreating the transaction's merkel proof and its block header and by comparing the hashes retrieved directly from the bitcoin blockchain via `get-block-info?`. If the transaction was indeed minted on the Bitcoin blockchain and if it contains the transfer of the agreed amount to the specified address, the NFT is release and transferred to the buyers STX address provided in the contract. If no valid Bitcoin transaction was submitted within the time limit, here 100 blocks, I can claim the NFT back from the contract and I can try to find a new buyer.

The relevant contract code is [here on github](https://github.com/friedger/clarity-friedger-pool/blob/main/contracts/btc-nft-swap.clar).

### Risk assessment

There are some risks for the buyer and the seller. 

- User errors: 
We assume that there are no user errors like making a typo in an address or forgetting the deadline. 
- Bugs in smart contract:
If the contract code is buggy, the NFT could be locked in the contract forever and Friedger Pool would pay the rewards to the contract. In that case, we might be able to convince the admin of Friedger Pool (that is me) to payout to the right address nevertheless.
- Malicious pool admin:
The pool admin could payout the rewards incorrectly. While this is possible (the pool admin overpaid in cycle #11), we trust that this won't happen. A trustless pool admin smart contract is planned for Friedger Pool in the not too far future.
- Smart contract fails to verify Bitcoin transaction:
This can happen if the Bitcoin transaction is too large. There can be only 8 inputs and 8 outputs in the transaction. The buyer must make sure that this won't happen. The smart contract might also fail to verify the Bitcoin transaction if the transaction happened during a so-called flash block. That is a Bitcoin block without a corresponding Stacks block. There is a [relevant issue](https://github.com/blockstack/stacks-blockchain/issues/2663) on the stacks git repo that hopefully will be addressed for Stacks 2.1. In this case for now, the buyer has to trust that the seller will transfer the NFT to the buyer manually after the time limit of the swap.
- Stacked Stacks are lost:
This won't happen, because PoX ensures that stacked Stacks tokens never leave my wallet.

Please let me know if you see more potential issues with this trustless swap. I will update this article with more details until the swap was executed successfully.
