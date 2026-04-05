---
title: "Instructions for Testing AFP"
categories: blockstack
image:
  title: instructions-for-testing-afp.jpg
---

### Introduction

The autonomous Friedger Pool (AFP) is a project that tries to automate the operation of [a Stacking Pool](https://docs.stacks.co/understand-stacks/stacking) as much as possible. The Proof of Transfer contract (pox) allows users to join a pool via simple smart contract calls. However, they have to trust pool operators that these manage the users' stacking rewards correctly.

Using smart contracts, the experience for pool members can be improved by

- providing transparency. Users should be able to see and verify how much rewards the pool admin has received and how much they paid out to users. AFP starts with transparency by applying verification of Bitcoin transactions on the Stacks blockchain. See [here](https://app.sigle.io/friedger.id/zwmiYGAH1TvqQnoiKGqSV) for details.
- creating a trustline. Pool admins should stake some value that users can distribute in case pool admins do not pay out the received rewards correctly. This requires clear rules about the reward distribution that users and pool admins have agreed on. It obviously requires transparency in the first place. AFP will provide a vault that the pool admin can fill, users can then evaluate their risk by inspecting this vault that is used for payouts.
- create a liquidity token for future rewards. Users could sell their future rewards while they keep their stacks. [Boomboxes](https://boom-wallet.medium.com/how-to-get-your-first-boombox-d97a9404e759) is one implementation using NFTs to provide liquidity on rewards.
- creating a liquidity token for locked Stacks. Users could sell their Stacks while they are locked. [DecentDelegate](https://github.com/hozzjss/cooperative-stacking) is an implementation of such a liquidity token.

For cycle #13, [Friedger Pool](https://pool.friedger.de) runs a test to help building better stacking pools.

### Testing Transparency

Goal of this test is to verify that a stacking pool has received a certain amount of bitcoin rewards for a given stacking cycle.

The btc address [33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq](https://mempool.space/address/33WSGLeVoEpuZDjB54HKZ1y5YsERELoVNq) is the reward address for Friedger Pool on mainnet. For cycle #13, we expect 135 reward slots. The should be more than 100 Bitcoin transactions for this address during cycle #13. These transactions should be reported to a smart contract that wraps these rewards into tokens on the Stacks chain. When the tokens are minted the current BTC/STX price retrieved from the oracle-v1 is also recorded.

### Task

Task submit the btc reward payments via the smart contract fprw-v02:

Each stacking rewards can be found in any bitcoin explorer. Copy the transaction id.

![](https://gaia.blockstack.org/hub/1Af6tr97gdEF24Ds2Mat3no6P6EkcGxUkL/photos/dAZao4q9C22DL76zHsF5-/Mg_VcfBRWtSyPRaQaKiql-Screenshot from 2021-07-29 22-51-40.png)

At [Friedger Pool's member area](https://pool.friedger.de/members), there is a section about submitting reward transactions. Paste the btc transaction id, click verify. 

Finally click submit and confirm the transaction using the Stacks Wallet browser extension.

Done. The rewards have been reported and the new "Friedger Pool Wrapped Rewards" ($FPWR-v02) have been minted and deposited into the FPWR depot. Later on, pool members can claim their rewards. 

BTW, these tokens do not have any value because the stacking rewards will be paid out as usual in Stacks.

### Testing Reward Claim

At the end of each cycle, pool admins determines how much rewards each pool member should receive. Ideally the amount is proportional to the member's stacked amount. Currently, it is not possible to

- retrieve this information within a smart contract. 
- determine in which cycle a reward was received.

Nevertheless, we can test the payout process, if the pool admin provides the missing information in a manual process at the end of the cycle. In the future, this step would be automated via the smart contract.

### Task

Only members that have stacked in cycle #13 can participate. Do this after cycle #13 has completed.

At [Friedger Pool's member area](https://pool.friedger.de/members), there is a section to claim your stacking rewards. Click the button and confirm the transaction of the Stacks Wallet extension.

Once the transaction was confirmed, you will see the received reward amount in your wallet as FPWR-v02 tokens.

### FAQ

1- Is everyone eligible for join the Friedger Pool automation testing? 
Yes.

2- How do I join the Friedger Pool automation testing?
Join the discord server (https://discord.gg/AFXMDjwA).

3- Should I install any tool for joining the testing
You need the Stacks Wallet for Web and you need to participate in Friedger Pool for cycle #13. You should have some unlocked stacks tokens (less than 1 STX required).

4- What steps should I follow for the test?
Follow the instructions above and provide feedback via [https://shrl.ink/v13i](https://shrl.ink/v13i)

5- What is the "Value for Friedger Pool" in reported Bitcoin transactions?
The reported bitcoin transactions contain the value of the rewards. The rewards are minted as wrapped reward tokens. Users can immediately see how much rewards have been received, at what Stacks price. Smart contracts can use these information to further automate the pool administration process.
