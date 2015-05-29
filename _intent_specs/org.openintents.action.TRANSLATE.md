---
title: Translate text
action: org.openintents.action.TRANSLATE
extras:
  -
    name: android.intent.extra.TEXT
    type: String
    var: text
    description: 
  -
    name: org.openintents.extra.FROM_LANGUAGE
    type: String
    var: from
  -
    name: org.openintents.extra.TO_LANGUAGE
    type: String
    var: to
out: 
  extras:
    - 
      name: android.intent.extra.TEXT
      type: String
      var: translatedText
      description: translated text
---
Use some translation engine to translate a text and return the result.
