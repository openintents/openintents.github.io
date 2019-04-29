---
title: OI Calendar Sync
subheadline: Bridging Web and Android
categories: apps
image:
  title: franck-v-512281-unsplash.jpg
---

[OI Calendar](https://cal.openintents.org) is a cloud calendar that stores the event data
in a private, encrypted manner on user-owned storage. The application does not create data silos, or so-called data honey pots because it stores users' data at a different location, at the users' storage provider. [Blockstack](https://blockstack.org) provides the tools to build such decentralized apps. OI Calendar is using Blockstack for authentication using [decentralized IDs](https://w3c-ccg.github.io/did-spec/) and for storage using the [Gaia protocol](https://github.com/blockstack/gaia)

On Android, calendar data is managed by a well defined content provider. In order to bring the events from OI Calendar onto the Android world, it is sufficent to build a `SyncAdapter`. This has now been released as [OI Calendar-Sync](https://github.com/openintents/calendar-sync). It is a utility app that synchronizes data between OI Calendar and the Android content provider for calendars. This means that Android users keep using their preferred calendar app and will also see their OI Calendar events.

The image below shows the same event in OI Calendar, Etar, Business Calendar, DigiCal.

![calendar event](https://github.com/openintents/openintents.github.io/raw/master/images/calendar-web-android.png)

The implementation is still in early stages, please provide feedback on [github](https://github.com/openintents/calendar-sync/issues).
