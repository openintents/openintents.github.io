---
title: Monsters on Speed Spend
subheadline: Marketplace for NFTs on Stacks Blockchain
categories: blockstack
image:
  title: marketplace.jpg
---

Non-fungible tokens (NFTs) are digital assets that live on the blockchain as data entries of a smart contract. They are globally unique and represent some kind of ownership. It could be ownership of a digital collectible, a gaming item, artwork or a representation of a real-world asset like a diamond or a theater ticket. Like a real-world asset, an NFT can be transferred from one user to another.

We have received a grant from the [Stacks Foundation](https://stacks.org/grants) to build a user-friendly marketplace for NFTs. The web app [Speed Spend](https://speed-spend.netlify.app) is a first milestone towards this goal. We created one "monster" NFT contract and a second pseudo NFT contract. Monsters are like pets and need to be fed once a day. You can do that for example on Speed Spend's [monster page](https://speed-spend.netlify.app/monsters) or on the testnet explorer sandbox. In contrast, the pesudo NFT is just an dumb asset that will always belong to the pseudo NFT contract, they can't even be transferred.

## Marketplace for NFTs

With the latest upgrade of Clarity on the Krypton testnet, it is now possible to build a marketplace where users can offer and buy NFTs as long as the NFT smart contract used `uint` keys to identify an NFT and as it implements a basic interface for trading. We defined this interface as a `trait` in Clarity with two functions that are required for a trade:

```
(define-trait tradables-trait
  (
    (owner-of? (uint) (response principal uint))
    (transfer (uint principal) (response bool uint))
  )
)
```

The marketplace contract assumes that all NFTs are always available for sale. There is one function to place a bid for an compatible NFT, one function to accept a bid, one function to pay for the bid and in case the payment does not happen timely one function to cancle the deal. After the owner of an NFT accepted a bid the marketplace smart contract owns the NFT until the bid is paid for or the deal was cancelled. The contract's address is `ST12EY99GS4YKP0CP2CFW6SEPWQ2CGVRWK5GHKDRV.market`. It's source code is available on chain and on [github](https://github.com/friedger/clarity-marketplace).

On Speed Spend, a basic UI was added that allows users to interact with all four market place functions and the two NFTs. On the testnet explorer sandbox, it is currently not possible to use these functions because the UI does not except contracts as parameters. See [issue #244](https://github.com/blockstack/explorer/issues/244) for details.

## Monsters on Speed Spend

The monster page shows the recent transactions on the marketplace contract. Each transaction has appropriate action buttons for the users, e.g. the owner can accept bids after a `bid` transaction, bidders can pay after an `accept` transaction. The video below shows a typical flow using the monster NFT.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gKOeUbI8F9o" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The video was created using a local setup for faster transaction confirmation. It requires

- to open speed spend with search parameter `?mocknet=local`,
- to run mocknet locally using the docker image of the stacks blockchain api node

  ```
  docker run -p 3999:3999 blockstack/stacks-blockchain-api-standalone mocknet
  ```

  and deploy the contracts with the mocknet flag on

  ```
  clarity-smart-contracts $ ts-node scripts/flip-coin-deploy-all.ts
  clarity-marketplace $ ts-node scripts/market.ts
  ```

- to run a local authenticator using my fork (see [issue #618](https://github.com/blockstack/ux/issues/618) - once the corresponding PR is merged this is not necessary anymore).

There is also a UI to bid for a pseudo NFT: users can bid for NFTs with an arbitary id, however, there is no user to accept the bid and the flow stays in the bidding state forever. It is just to show that the marketplace can handle more than one type of NFTs.

## NFTs session

In parallel to the development of the marketplace feature for Speed Spend, we hold two sessions about NFTs to bring creators and developers of NFTs together. The first session was a general introduction, explaining that NFTs are globally unique and can be transferred. The second session was about additional properties that an NFT can have, like tradable or composable. The next session will be about trading and marketplaces for NFTs. All slides are available on the site for NFTs: [tofauti.net](https://tofauti.net).
