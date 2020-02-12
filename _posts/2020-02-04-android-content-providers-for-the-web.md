---
title: Android Content Providers for the Web
subheadline: Giving web users control of their calendar data
categories: blockstack
image:
  title: vinicius-amano-566532-unsplash.jpg
---

In this article, the term **web content providers** is defined and OI Calendar is used as an example.

[OI Calendar](https://cal.openintents.org) is a cloud calendar that stores the event data
in a private, encrypted manner on user-owned storage. The application does not create data silos, or so-called data honey pots because it stores users' data at a different location, at the users' storage provider. [Blockstack](https://blockstack.org) provides the tools to build such decentralized apps. OI Calendar is using Blockstack for authentication using [decentralized IDs](https://w3c-ccg.github.io/did-spec/) and for storage using the [Gaia protocol](https://github.com/blockstack/gaia)

[OI Calendar-Sync](https://github.com/openintents/calendar-sync) is a utility app on Android that synchronizes data between OI Calendar and the Android content provider for calendars. Content Providers on Android are parts of the Android system that store and give access to one particular type of data. Some types like contact data, calendar data or media data are predefined by the Android system (through contract definitions), other types like email data or shopping list data are defined by 3rd party apps. They are accessible through a unified API on Android such that all apps (with the right permissions) can make use of the user's data from a single source. The user is in control and manages the data at this one source.

On the web, the situation is different. Contact data, images, blog posts or comments are scattered around different apps, mostly data silos that make it hard for users to access their data across apps or that require to copy their data between apps. With [Blockstack's collections](https://github.com/blockstack/blockstack.js/issues/642), a solution similar to Android Content Providers is proposed that solves these problems for the web. Let's call these collections "Web Content Providers".

A **Web Content Provider** is a web service that allows 3rd party applications to access user data of a particular type in a unified way with the user's permission.

The difference to current services like Google APIs is that

- the type of data is defined outside the services that manage this data.
- only the user controls access to this data. There is no 3rd party involved if a service ask for permission to manage the data - thanks to cryptography.

The implementation of Blockstack is still ongoing but the end result will be that each data type has its own bucket, its own address in the user's gaia storage. Thereby, users can freely provide access to that bucket in the same way users control access to app specific data.

For OI Calendar, this means that calendar data is not controlled by this single app, that the user can choose their preferred web app for viewing calendar events in the same way Android user can choose from a big range of calendar apps like Etar, Business Calendar, Google Calendar or DigiCal. And furthermore, with OI Calendar Sync, this works across Android and the Web!

A short introduction to the concept was given as a lightning talk at FOSDOM 2020. Please find video with slides [here](https://fosdem.org/2020/schedule/event/dip_android/)

![calendar event](https://github.com/openintents/openintents.github.io/raw/master/images/calendar-web-android.png)
