---
title: View data
action: android.intent.action.VIEW
input:
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
