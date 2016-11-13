---
title: Google and the Open Android Ecosystem
subheadline: Examples
categories: opinion
---
At the local Google I/O extended event we had a discussion about policies for
mobile developers and the [formal investigations](http://ec.europa.eu/competition/elojade/isef/case_details.cfm?proc_code=1_40099)
of the EU commission against Google and Alphabet with regards to Android. The
commission mentioned three areas: anti-fragmentation, revenue sharing and
app bundling. There are no details where Google allegedly misuses its
market dominance. See also the discussion at [reddit](https://www.reddit.com/r/Android/comments/4fml1a/european_commission_antitrust_commission_sends/).

Here we would like to share a few examples mainly from the app bundling area
where the Google team could serve the open Android ecosystem better.

## Android Wear and Google app
Android Wear can't be used without the Google app.
If the Google app is not installed or disabled the Android Wear app forces the
user to enable the Google app before continuing.

![Android Wear requires Google]({{site.url}}/assets/img/posts/WearAppWithoutGoogle.png)

## Drive and Play Store
The Play Store app has an interface for lightweight installation of apps. The user doesn't
has to go through the usual process of Google Play Store. Drive is using this interface
to install Docs if the user wants to edit a document. However, this interface can
only be used by privileged apps, i.e. by apps from Google. See [question at stackoverflow](http://stackoverflow.com/questions/23695170/how-to-install-applications-programatically-without-opening-play-store-as-googl).

![Drive installs Docs]({{site.url}}/assets/img/posts/DriveDocsInstall.png)

## Google Search drops support for Quick Box Search
The Android framework supports system-wide search through the so-called
[Quick Search Box](https://developer.android.com/guide/topics/search/adding-custom-suggestions.html#QSB).
However, Google search, which is on many devices the default search engine does not implement the
quick search box mechanism anymore and therefore, encourages developers and product managers
to create silo apps and to use the Google App Indexing. Most user won't find apps like
[Quick Search](https://play.google.com/store/apps/details?id=com.startapp.quicksearchbox)
to make use of the Android global search feature.

## Search for Apps
Of course, we would like to see the possibility to search the Play Store by intent filters. Gmail is trying
to mimic the search for apps by using file extensions if there is no app install that can open a particular attachment.
Google, you can do better!

![Search by file extension 1]({{site.url}}/assets/img/posts/FileExtensionSearch1.png)
![Search by file extension 2]({{site.url}}/assets/img/posts/FileExtensionSearch2.png)
