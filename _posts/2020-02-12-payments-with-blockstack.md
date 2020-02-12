---
title: Payments with Blockstack
subheadline: Blockstack Legends to support app developement
categories: blockstack
image:
  title: dan-meyers-MQ8-4HYTgOc-unsplash.jpg
---

The development of OI apps are only supported by [donations](https://openintents.org/contribute). With the adoption of Blockstack technologies, new possibilities came up to accept payments in a privacy-preserving manner and in particular without the need to maintain a database of user data. (Obviously, you will need to do what is needed for your book keeping.)

To separete the concerns of payments and the actual apps, a new app `Blockstack Legends` was build that is only dealing with accepting credit cards, cash or payments from other providers. Once, the payment is processed the app will issue a membership card of the Blockstack Legends Club.

## Creating Membership Cards

This membership card is a signed JSON web token (JWT). It contains the user name, i.e. the club member, an expiry date and a attribute stating that the user is indeed member of the club. Finally, the token is sigend with the keys of the club. Luckily, the functionality is already provided by `blockstack.js` through `signProfileToken`. For the purpose of the the membership card this method can be used in the same way as the blockstack browser is using the method to certify certain properties of a blockstack user during authentication.

The code looks like this:

```
const membershipCard = await blockstack.signProfileToken(
        { member: true, group: `Blockstack Legends` },
        clubPrivateKey,
        {
          username,
          publicKey,
        },
        undefined,
        'ES256K',
        new Date(),
        exp
      );
```

The first parameter describes the attributes this token certifies, the private key is used signing. The third parameter describes the club member or in general the subject of the token. Usually, it is only a public key, however, for the membership card, the username is included. This simplifies the verification later on. The next parameter defines the issuer, it can be leaft undefined so that the private key is used to derive the issuing public key. Finally, the signing algorithm is given, the issuing date and the expiry data. The expiry date depends on the amount the user paid and the monthly club fees.

This signed token can now be transferred to the user. There is no need for the app to keep it. Ideally, it is stored encrypted in the user's collection of certificates on gaia.

## Using Membership Cards

Now, other apps can ask the user for the location of the membership card and if validated provide premium features or other benefits for club members. Blockstack provides the method `verifyProfileToken` that is used during the authentication flow. The same method can be used to verify the membership card:

```
fetch(membershipCardUrl)
    .then(response => response.text())
    .then(cardContent => {
      if (cardContent) {
        const card = verifyProfileToken(cardContent, clubPublicKey);
        if (validBlockstackLegendsCard(card, username)) {
          return card;
        }
      }
      return Promise.reject('no card');
    });
```

It is not enough to verify the signature and dates of the token, this is already done by the `verifyProfileToken` method. Other properties of the card need to be verified as well. In particular, whether the subject is the current user and whether the subject is member of the correct group. The method `validBlockstackLegendsCard` would looks something like this

```
function validBlockstackLegendsCard(card, username) {
  if (!card.claim) return false;
  const isMember = card.claim.member && card.claim.group === `Blockstack Legends`;
  const isSubjectCurrentUser = card.subject.username === username;
  return isMember && isSubjectCurrentUser;
}
```

If all is valid the app can show premium features and provide other benefits to the users. A simple app based on REBL stack can be found [here](https://github.com/friedger/starter-app/tree/feature/premium).

## Payment Providers

In the current Blockstack Legends apps two payment possiblities are included:

1. cash payment
1. credit card payments via Stripe

### Cash Payment

For cash payments, administrators of the Blockstack Legends club generate payment receipts in the same way as membership cards are create: as JWTs signed with the personal key of the administrator. The user can then request a membership card with the payment receipt.

### Credit Card Payments vai Stripe

For credit card payments, the app is communicating with the stripe backend using the [payment intents API](https://stripe.com/docs/payments/payment-intents). On successful payment, a webhook is called that is hosted on netlify using netlify functions. The function ([webhooks.js](https://github.com/openintents/members/blob/master/lambda-src/webhooks.js))has access to the private key of the club and can generate a membership card. It is stored on the club's gaia storage until the user has moved it her own storage.

## Conclusions

Using existing functions in `blockstack.js` for JWTs are used to create proofs of payment and membership cards as JWTs. These JWTs can be used and validated by other apps without requesting any servers holding a user database or so. The validity is provided by the token itself through cryptography.

The next steps are to provide premium features for Blockstack Legends in OI apps and improve the handling of membership cards for the user through Blockstack collections.
