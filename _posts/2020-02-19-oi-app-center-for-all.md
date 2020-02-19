---
title: OI App Center for All
subheadline: Sharing reviews and other Blockstack app meta data
categories: blockstack
image:
  title: oi-app-center-for-all.png
---

OI App Center is a platform to collect reviews about Blockstack apps. In contrast to commonly known platforms like Amazon, Yelp, or AirBnB, the data is owned and controlled by the users, not the platform. OI App Center is just a (hopefully) convenient representation of that data, and its purpose is to help all users to create reviews and to find reviews of interesting apps.

Users store and manage their reviews in their gaia storage and then notify the data indexer of OI App Center about the new data. The indexer is hosted at https://app-center.herokuapp.com/ and it uses the radiks server implementation by Blockstack. This allows anyone to inspect the aggregated data of the indexer. For example, the following url returns all user comments for Envelop, it follows the `queryToMongo` syntax (see [Radiks' git repo](https://github.com/blockstack/radiks-server/blob/master/src/controllers/ModelsController.ts#L46) for details):

```
https://app-center.herokuapp.com/radiks/models/find?radiksType=UserComment&object=https://envelop.app
```

The model for a comment is very simple. It contains the comment, a rating (1-5) and a reference to the app (the object, in this case the authentication domain of the app). Furthermore, it contains the usual properties of a radiks model to verify the creator of the comment.

For convenience, the indexer provides an API to only return the latest comments by each user:

```
https://app-center.herokuapp.com/api/usercomments
```

These APIs are good for displaying comments in apps like [Dappity](https://dappity.app) or [Webby](https://heywebby.app/), or on landing pages of specific apps. However, they are not good for creating new comments across apps. Unfortunately, the current radiks server implementation only supports indexing data of one application. This is due to the way how signing keys are created and it probably won't change in the near future. However, with [collections](https://docs.blockstack.org/develop/collections.html) the user would sign with their collection keys and this is the same across all apps. As collections are in the preview state we are looking forward to bring this feature into the hands of users and app developers.

![user comments](https://github.com/openintents/openintents.github.io/raw/master/images/oi-app-center-for-all.png)
