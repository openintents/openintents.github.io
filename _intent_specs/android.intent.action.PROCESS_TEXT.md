---
title: Process text
action: android.intent.action.PROCESS_TEXT
constant: android.content.Intent.ACTION_PROCESS_TEXT
link: https://developer.android.com/reference/android/content/Intent.html#ACTION_PROCESS_TEXT
extras: 
  -
    name: android.intent.extra.PROCESS_TEXT
    type: String
    var: text
    description: text to be processed
  -
    name: android.intent.extra.PROCESS_TEXT_READONLY
    type: boolean
    var: readonly
    description: states if the resulting text will be read-only  
out:
  extras:
    -
      name: android.intent.extra.PROCESS_TEXT
      type: String
      var: processedText
      description: the processed text
---
Process a piece of text
