---
title: Giving Internet Permission
subheadline: OI apps embrace user-owned storage
categories: apps
image:
  title: nick-fewings-642033-unsplash.jpg
---
OpenIntents is a community effort to promote and discuss the use of Android intents and similar concept of modern mobile platforms.
Until now, there were little reasons for OpenIntents to allow apps to access the internet. The applications are mainly
productivity apps for Android that handle user data on the user's device. OpenIntents does not want to deal with user data or track any users. 
Therefore, `android.permission.INTERNET` was not added to the manifests even when Google made this permission not dangereous anymore.
(Read more for example at [Android Police from 2015](https://www.androidpolice.com/2015/06/06/android-m-will-never-ask-users-for-permission-to-use-the-internet-and-thats-probably-okay/))

This changed today. 10 years after version 1.0.0 of OI ConvertCSV was released (on 9th Dec 2008), [OI ConvertCSV](https://convertcsv.openintents.org) is the first (of many) application 
that received the internet permission. OpenIntents 
still does not want to deal with user data or track users but the user should have the possibility to 
backup their data at **the location they want** (and import from wherever they want). With the development in 
blockchain technology this is possible. [Blockstack](https://blockstack.org) has build a storage system (gaia) 
that belongs to the user in the real sense: 
* Users create their own decentralized identity that truely belongs to the user (by means of the private key). 
* User names are registered on the blockchain backed by a large (bitcoin) community, not a single for-profit company. 
* Users can configure were application data should be storage by editing their public profile.
* The app only provides a domain name to identify the app data. (For OI ConvertCSV, this is **convertcsv.openintents.org**.)

OpenIntents is not involved in these user activities. We only provide the code to enable the user and
we had the chance to contribute to the (open source) Android SDK for Blockstack. OI ConvertCSV was ideal for the 
first conversion to an app that is backed by user-own storage. As the purpose of the app is to backup and transfer shopping lists 
and notes, it was a question of adding a custom document provider for the Android storage access framework (SAF) and an 
account activity. Through the SAF, the user can now choose a location on their own gaia storage to backup 
their data or to transfer it to another device. 

If you want to read more about Blockstack, there is a nice tutorial for developers to get into the topic of user-owned storage 
at [docs.blockstack.org](https://docs.blockstack.org/develop/zero_to_dapp_1.html).
