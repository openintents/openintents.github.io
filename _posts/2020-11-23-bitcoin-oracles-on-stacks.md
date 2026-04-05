---
title: "Bitcoin Oracles on Stacks"
categories: blockstack
image:
  title: bitcoin-oracles-on-stacks.jpg
---

### Introduction

In September, it was announced that [Chainlink](https://chain.link) will come to the Stacks ecosystem. Chainlink is described as decentralized oracle network that provides reliable, tamper-proof inputs and outputs for smart contracts on any blockchain. From the view point of a smart contract developer this is just an interface (aka trait in Clarity) for a black box that can be asked a question and it will return an answer. This introduces a level of trust that lies outside of the blockchain. 

The on-chain trust of a blockchain is built by the consensus algorithm. It gives trust in the state of the blockchain because the majority of the nodes verifies all state changes based on data that is stored on chain. Chainlink tries to build a trust system by self-certification and data duplication. There is an incentive for oracles to provide correct data through rewards (in LINK tokens). However, there is no explicit stake at risk for oracles if they provide incorrect data.

![](/images/bitcoin-oracles-on-stacks-I9gyPQhFu6H1_7cam1w13-8c35025-Request__Receive_Data.png)

### Proof-of-Stake Mixin

The Stacks blockchain has a reliable link to the Bitcoin blockchain through Proof of Transfer. This link can be used for oracles for the bitcoin blockchain. Bitcoin oracles can answer questions like how many confirmations has a Bitcoin transaction or what is the current balance of a bitcoin address. Looking at the stacks node, these questions could be answered easily by all stacks nodes because they have already access to the Bitcoin blockchain. 

A stacks node could watch out for transactions of a Bitcoin oracle question, then check the Bitcoin blockchain and send a transaction with the answer. What is more, miner nodes could do the same and include only transactions if they found the same answer. Probably, it would be the other way around: Miner nodes would send the answering transaction themselves to get the reward and all stack nodes could verify it. If they find out that the miner added a transaction with a wrong answer they could deny the miner's block reward. The blockchain would then continue with a fork containing the "correct" transaction. This means that the block reward acts as the stake for the Bitcoin oracles.

![](/images/bitcoin-oracles-on-stacks-FhPRhRqbx75Aq80Ds_cRL-bitcoinoracles.png)

### Wrapped Bitcoin

With Bitcoin oracles it is easier to build wrapped Bitcoins. Wrapped Bitcoins are fungible tokens on the Stacks blockchain that correspond to Bitcoins on the Bitcoin blockchain. There is one Wrapped Bitcoins contract that creates new tokens whenever its corresponding Bitcoin address received Bitcoins. The tokens are sent to the corresponding Stacks address of the Bitcoin sender. Bitcoin oracles can be asked to confirm that the Wrapped Bitcoins are indeed backed by real Bitcoins. 

![](/images/bitcoin-oracles-on-stacks-aJXhlBiAY3SHyI2itediE-Wrapped Bitcoin.png)

### Conclusion

With the trust in Bitcoin oracles that are secured by additional Proof-of-Stake, a new class of smart contracts can be built: Smart contracts could payout Stacks loans based on Bitcoin collaterals, Bitcoin transactions could be counted as votes on the Stacks blockchain and so on.
