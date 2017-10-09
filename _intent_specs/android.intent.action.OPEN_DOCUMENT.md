---
title: Open Document
action: android.intent.action.OPEN_DOCUMENT
constant: android.content.Intent.ACTION_OPEN_DOCUMENT
link: https://developer.android.com/reference/android/content/Intent.html#ACTION_OPEN_DOCUMENT
extras:
  -
     name: android.provider.extra.INITIAL_URI
     type: android.net.Uri
     var: initialUri
     description: sets the desired initial location visible to user when file chooser is shown
out:
  -
     data: URI of the item that was picked if one document was picked.
     clipdata: URIs of the documents that have been picked if more than one was picked.
---
Allows the user to select and return one or more existing documents.

See also [PICK_FILE](/action/org-openintents-action-pick-file).
