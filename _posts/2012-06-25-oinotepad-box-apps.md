---
title: OI Notepad and Box OneCloud apps
subheadline: Collaboration started  
categories: Apps
---

OI Notepad is one of the first apps that integrates the new collaboration feature of the Box app. Box provides a secure content sharing platform and since today allows other Android apps to hook into the Box app. While the Box app focuses on managing the secure online storage, other Android applications take the responsibility for displaying and editing the file content. Thus, the end users can choose their preferred viewer and editing apps. It also takes the burden of Box to provide a one-for-all solution. OpenIntents is happy to see this excellent use of the Android intent system.

OI Notepad declares an intent filter for plain text files (mime-type text/plain) and thereby indicates that OI Notepad can handle these file types for displaying and editing. In the Box app the end user can choose from the installed apps as well as new apps from Google Play that have been registered as partner apps:

[img Edit text file] [img Create new text file]

Once, the user has chosen OI Notepad a data object is passed to OI Notepad that contains a binder to the Box OneCloud service. This provides access to an input and output stream for reading and uploading the file content.

From a developer point of view, the integration was straight forward as Box provides an SDK with a library project at github.com/box. The existing UI of OI Notepad was only changed slightly to indicate the possibility for uploading.

From a security point of view, the integration is save as the data (i.e. notes) is provided by the Box app, OI Notepad only acts as the viewer and editor. No need for OI Notepad to ask for INTERNET permission. No content from OI Notepad itself is passed outside of the app.
