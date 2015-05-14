---
title: Show about dialog
action: org.openintents.action.SHOW_ABOUT_DIALOG
output: none, but required to recognise the calling app.
---
Show an about dialog to display information about your application.

By default the information is retrieved from the Manifest of your application (both from the manifest tag as from metadata tags). Metadata keys are specified in (as constants) in `org.openintents.metadata.AboutMetaData`. 
Optionally send along extras with information to display (overriding the metadata). Intent extra keys are specified (as constants) in `org.openintents.intents.AboutIntents`.

From your "about" menu option you start an activity with this specific intent action:
```java
Intent intent = new Intent("org.openintents.action.SHOW_ABOUT_DIALOG");
startActivityForResult(intent, 0);
```
The activity needs to be launched "forResult" with requestCode>=0 so that the package name is passed properly. Optionally, one can set the intent extra
`org.openintents.extra.PACKAGE_NAME`.

Original use is with OI About: See [OI About]({{site.url}}/aboutapp) for usage information for this intent.
An OI TestAboutApp demonstrating this is also available.
