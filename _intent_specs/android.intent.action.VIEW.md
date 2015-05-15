---
title: View data
action: android.intent.action.VIEW
uri: Uri of the data to be displayed
link: https://developer.android.com/reference/android/content/Intent.html#ACTION_VIEW
author: android
---
Display the specified data to the user.

An activity implementing this action will display to the user the
given data. It is not intended for the user to edit it, though an
implementation can allow that to be done as a secondary part of its UI
if desired (as it can provide any other optional features in its UI
for the user).

This is the most common action performed on data -- it is the generic action you can use on a piece of data to get the most reasonable thing to occur. For example, when used on a contacts entry it will view the entry; when used on a mailto: URI it will bring up a compose window filled with the information supplied by the URI; when used with a tel: URI it will invoke the dialer.
