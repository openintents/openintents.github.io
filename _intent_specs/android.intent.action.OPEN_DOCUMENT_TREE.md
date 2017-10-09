---
title: Open Directory
action: android.intent.action.OPEN_DOCUMENT_TREE
constant: android.content.Intent.ACTION_OPEN_DOCUMENT_TREE
link: https://developer.android.com/reference/android/content/Intent.html#ACTION_OPEN_DOCUMENT_TREE
extras:
  -
     name: android.provider.extra.INITIAL_URI
     type: android.net.Uri
     var: initialUri
     description: sets the desired initial location visible to user when file chooser is shown
out:
  -
     data: URI of the item that was picked
---
Allows the user to select and return a document directory.
