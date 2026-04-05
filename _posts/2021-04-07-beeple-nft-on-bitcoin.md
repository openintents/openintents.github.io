---
title: "Beeple NFT on Bitcoin"
categories: blockstack
image:
  title: beeple-nft-on-bitcoin.png
---

Recently, the artist known as Beeple auctioned his work *EVERYDAYS: THE FIRST 5000 DAYS* as a non-fungible token (NFT) at Christie's. The NFT changed ownership for [$65 million USD](https://onlineonly.christies.com/s/beeple-first-5000-days/beeple-b-1981-1/112924). This started discussions about the value of NFTs.

NFTs are like certificates on paper but written to a blockchain. Like certificates, NFTs are created by an issuer. By creating a certificate, the issuer wants to make a certain statement that the certificate holder can show to others. The statement could be for example about citizenship. Those looking at the certificate want to verify that the certificate is valid and genuine. On paper, we use official seals, watermarks, etc. On the blockchain, we use cryptographic keys.

The most important property of an NFT is that the ownership of the NFT can change without asking the issuer for permission while the statement stored on the NFT cannot be changed at all. Looking at the Beeple NFT, Christie's transferred the NFT after payment while the content remains unchanged. The NFT will always reference the hash of the digital artwork. It is some kind of a unchangeable link to the image. The NFT states that there is the digital artwork and, furthermore, that only one NFT with this link exists that was created by the artist. 

It is not very difficult to create another NFT. See for example the Beeple NFT on the Stacks blockchain [here](https://explorer.stacks.co/txid/0x8f0393265a8a4102701ef6240b03022c567cf67f04e472e077709fe975424921?chain=mainnet). It contains a link to the same digital artwork. The only difference is that it was issued by somebody else. Therefore, the value of an NFT comes from the issuing party and it's recognition by those looking at the NFT. For the Beeple NFT on the Stacks blockchain, the issuer is not recognized as the artist. For the Beeple NFT auctioned by Christie's, the issuer is recognized as the actual artist and Christie's as an authority for auctioning arts increases the reputation. 

As seen, the value of the NFT does not comes from the statement stored in the NFT but from those using it. The next question is how to make the statement. Is a written statement on paper enough? If it should be globally accessible and the medium should not be controlled by a single entity, then blockchains are the only solution. There are specialized blockchains for NFTs like [Wax](https://on.wax.io/wax-io/) that do not care too much about security but more about fun and speed. For artwork worth millions of dollars this is inappropriate. It shouldn't be probably on less than the Bitcoin blockchain as the most battle tested and secure blockchain. With the addition of smart contracts to Bitcoins via [Proof of Transfer](https://docs.blockstack.org/understand-stacks/proof-of-transfer) on the Stacks blockchain, it is possible to secure your NFTs with Bitcoin. That means that malicious users have to attack the Bitcoin blockchain in order to steal NFTs on the Stacks blockchain.

If you are interested to mint your own NFT, you can use the [Boom app](https://boom.money). If you are interested in more technical details, a good starting point is the [Stacks documentation](https://docs.blockstack.org/write-smart-contracts/overview).
