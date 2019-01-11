---
title: Getting Rid of Passwords
subheadline: OI Chat launched today
categories: apps
image:
  title: amanda-jones-1277188-unsplash.jpg
---
Having contributed to the Android app of [Matrix.org](https://matrix.org) back in 2015 (adding [basic support for Android Auto](https://github.com/matrix-org/matrix-android-sdk/pull/20)) it feels great to get involved again. 

Today, we launched [OI Chat](https://chat.openintents.org), a Matrix service dedicated to Blockstack users. As explained in the post [Giving Internet Permission](https://www.openintents.org/blog/2018-12-09-giving-internet-permission.md), Blockstack is a platform for decentralized apps. It provides a decentralized identity that comes with user-owned storage. [OI ConvertCSV](https://convertcsv.openitnents.org) and [OI Timesheet](https://oi-timesheet.com) benefit from it already. However, when I talk about Blockstack I mention two parts that are still missing in the platform: 
1. Decentralized Communication
1. P2P Payment

I think that Matrix is to chat what Gaia is to storage, therefore, we invested in OI Chat to bring both parts together. The result is 
* a [matrix server](https://github.com/friedger/matrix-blockstack-password-provider) that does not rely on or store any passwords anymore, 
* a [matrix client](https://github.com/friedger/riot-web) that simplifies login for Blockstack users, and
* an [auth tool](https://github.com/friedger/matrix-blockstack-auth) to generate one-time logins for alternative matrix clients.

All Blockstack users have a reserved account on the matrix server that only they can control. The Blockstack identity address is used as the username on matrix, and the authentication flow requires the user to prove that they are in control of the corresponding keys. In particular, the user has to write a challenge received from the matrix server into the app bucket on the user's Gaia storage and then provide the location as kind of password during login. The matrix server looks up the user's profile on the Blockstack network, retrieves the challenge from the user's gaia storage and can verify that the user is indeed in control of the blockstack account.

The OI Chat matrix client does this automatically. The tool for the one-time login has implemented the same algorithm and thereby allows the user to choose alternative matrix clients. The user has to just enter their username and the generated one-time login e.g. on Android or iOS. Finally, the same algorithm can be used by any Blockstack app to integrated with matrix communication. Apps could e.g. send invitations to other users, exchange messages, or establish a protocol to collaborate on shared data. A Blockstack API was proposed on [the forum](https://forum.blockstack.org/t/proposal-chat-provider-for-inbox-notifications/6926) that has been partly implemented in the auth tool.

The innovation here is that authentication happens without dependency on password safes or federated authentication providers. It uses just one-time logins, cryptography and user-owned storage to prove the identity of a user. In order to support [more distributed identities](https://w3c-ccg.github.io/did-spec/) that not necessarily have user-owned storage attached a few change requests to the matrix specification has been made, in particular [MSC1762](https://github.com/matrix-org/matrix-doc/pull/1762), [MSC1768](https://github.com/matrix-org/matrix-doc/pull/1768), [MSC1780](https://github.com/matrix-org/matrix-doc/pull/1780), and [MSC1781](https://github.com/matrix-org/matrix-doc/pull/1781).

 