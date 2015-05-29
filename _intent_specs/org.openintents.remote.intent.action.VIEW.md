---
title: View data on remote machine
action: org.openintents.remote.intent.action.VIEW
extras:
  - 
    name: org.openintents.remote.intent.extra.HOST
    type: String
    var: host
    description: Specifies the host on which to execute a remote intent.
author: mr.baldwin  
---
Simulates an android.intent.action.VIEW intent on a remote machine.

Although the remote machine may not be running Android, it may be controlled remotely by an Android application. 
For example, an Android application for controlling a media center may instruct the media center to open a file that is stored locally on the media center. 
The data URI would be interpreted relative to the remote machine. For example, a file:// URI would always refer to a file on the media center, not a file on the SD card of the device controlling the media center.
