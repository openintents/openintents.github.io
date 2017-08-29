---
title: What we know about WebApks
subheadline: Installing PWAs
categories: opinion
image:
  title: willie-fineberg-57667.jpg
---
The new HTML5 is called Progressive Web Apps (PWAs). They are web applications that also work on mobile,
also when offline and also when one old browsers. If they are used often, the browser can suggest to
add them to the home screen, to (kind of) install the apps.

The easiest solution for installing a PWA is by creating a bookmark of the start url of the PWA. 
However, there are some problems with that [as described by Henrik Joreteg](https://joreteg.com/blog/installing-web-apps-for-real#the-time-has-come). 

He also describes that [Paul Kinlan announced](https://youtu.be/YJwrBbze_Ec?t=21m33s) at the Chrome Dev Summit 2016 
that there will be soon WebApks on Android. WebApks are PWAs wrapped into native Android apps. (Similar to

Since 28 August 2017, Chrome on Android (version 59, stable) contains the feature to install PWAs as normal Android apps ("improved A2HS"). 
After the user was asked to add the PWA on to the decive, Chrome does some magic 
([as hinted by Paul Kinlan](https://twitter.com/Paul_Kinlan/status/9021861366464143369) and [here](https://twitter.com/Paul_Kinlan/status/900798601663795201)) by querying Google Play Services 
to download and install the corresponding WebApk in the background. 
The user does not see any differences between installed PWAs and other apps as technically there aren't any. This 
solves a few usability issues that the installation of PWAs had before.

Looking into such a WebApk created by Chrome reveals that there is a runtime host defined in the meta data of the apk
(org.chromium.webapk.shell_apk.runtimeHost) that launches the PWA. For Chrome's WebApks, the runtime host is Chrome. 
If the runtime host is not available then the VIEW intent with the start url of the PWA is fired. 
(There are more checks and fallbacks, but nothing essential). The package name of the WebApk is something like 
"org.chromium.webapk.ace0b15a6ce931426". Hence, in a WebApk, there is nothing particular specific 
to the Chrome browser, one need "just" to replace the runtime host in the WebApk's manifest.

However, for now, there is no documentation of how other browsers can create such a WebApk, [as stated 
by Paul Kinlian](https://twitter.com/Paul_Kinlan/status/901849918884773888).
As Google Play Services have a backdoor for Google's apps to install other apps (like Drive can install Docs), for Chrome it is 
easy to use Google Play Services to query the installation of a WebApk, for other browsers this is hard (requires build infrastructure, 
side-loading permission, ..).

Since Android 8, these other browsers have an even harder existance in regards to PWAs. 
[Maximilano Firtman points out](https://medium.com/@firt/android-oreo-takes-a-bite-out-of-progressive-web-apps-30b7e854648f) 
that Google has made the old way of "installing" PWAs (via bookmarks) less usable. The other browsers can't do much in this area
now, have to wait for a WebApk API of Google Play Services. And even when this becomes available, 
what should the other browsers do if they want support Android devices without Google experience? It looks like 
the browsing experience of modern web apps has been moved by Google from the Android operating system into their Play services.
