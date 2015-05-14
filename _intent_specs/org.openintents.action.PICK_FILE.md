---
title: Pick a file
action: org.openintents.action.PICK_FILE
input:
  uri: A file URI for suggested file name or starting directory. Can also be left empty.
extras:
  -
    name: org.openintents.extra.TITLE
    type: String
    description: title for the chooser activity
  -
   name: org.openintents.extra.BUTTON_TEXT
   type: String
   description: text for the default button of an activity.
output:
  uri: File URI of the selected file.
---
Pick a file through a file manager.

The picked file URI can be obtained in `onActivityResult()` through `getData()`.

Details can be found in the sample application [TestFileManager](https://github.com/openintents/filemanager/tree/master/FileManagerDemo) in the public repository.

You may want to use the [OI File Manager intent definition file](https://github.com/openintents/filemanager/blob/master/FileManagerDemo/src/org/openintents/intents/FileManagerIntents.java).
