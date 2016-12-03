---
title: Send an app crash report 
action: android.intent.action.ACTION_APP_ERROR
constant: android.content.Intent.ACTION_APP_ERROR
link: https://developer.android.com/reference/android/content/Intent.html#ACTION_APP_ERROR
extras: 
  - 
    name: android.intent.extra.BUG_REPORT
    type: android.app.ApplicationErrorReport
    var: errorReport
    sample: new AppErrorReport()
---
The user pressed the "Report" button in the crash/ANR dialog.
This intent is delivered to the package which installed the application, usually Google Play. 
