---
title: View a file directory
name: view-directory
action: android.intent.action.VIEW
uri: content uri of directory from FileProvider or DocumentProvider, can be empty.
type: vnd.android.documents/directory
author: Friedger Müffke
submitted: 2017-10-08
permalink: /action/android-intent-action-view/file-directory
extras:
  -
    name: org.openintents.extra.ABSOLUTE_PATH
    type: String
    var: absolutePath
    description: absolute path of the directory
    
implementations: 
  -    
    name: OI File Manager 
    url: https://play.google.com/store/apps/details?id=org.openintents.filemanager
---
This intention is used to allow 3rd party apps to direct the user to a files directory.

The uri can be used by the (file manager) app to retrieve the display name of the folder.
It is the responsibility of the (file manager) app to decide whether it can display the directory 
or not (due to missing permissions or unknown location).
