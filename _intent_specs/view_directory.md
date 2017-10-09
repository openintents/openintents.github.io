---
title: View file directory
name: file-directory
action: android.intent.action.VIEW
uri: uri of directory from FileProvider, DocumentProvider or uri with file scheme, can be empty.
type: vnd.android.documents/directory
typelink: https://developer.android.com/reference/android/provider/DocumentsContract.Document.html#MIME_TYPE_DIR
author: Friedger Müffke
submitted: 2017-10-08
permalink: /action/android-intent-action-view/file-directory
extras:
  -
    name: org.openintents.extra.ABSOLUTE_PATH
    type: String
    var: absolutePath
    description: absolute path of the directory
---
This intention is used to allow 3rd party apps to direct the user to a directory of the file system
or document tree.

The location of the directory is either provided in the extra or as data uri.

The content uri (if provided) of the received intent can be used by the (file manager) app to retrieve the display name of the folder via `OpenableColumns.DATA`. The file: scheme uri (if provided) can be used to determine the directory path if the extra was not provided.

It is the responsibility of the (file manager) app to decide whether it can display the directory
or not (due to missing permissions or unknown location).

Note, file: scheme uris should not be used in apps targeted Android 24+, otherwise a [`FileUriExposedException`](https://developer.android.com/reference/android/os/FileUriExposedException.html) is thrown.

Note, for picking a directory or file, use [OPEN_DOCUMENT](/action/android-intent-action-open-document),  
[OPEN_DOCUMENT_TREE](/action/android-intent-action-open-document-tree)
or [PICK_FILE](/action/org-openintents-action-pick-file).
