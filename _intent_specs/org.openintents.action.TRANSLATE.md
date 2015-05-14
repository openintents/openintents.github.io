---
title: Translate text
action: org.openintents.action.TRANSLATE
extras:
  -
    name: android.intent.extra.TEXT
    type: String
    description: 
  -
    name: org.openintents.extra.FROM_LANGUAGE
    type: String
  -
    name: org.openintents.extra.TO_LANGUAGE
    type: String
out: 
  extras:
    - 
      name: android.intent.extra.TEXT
      type: String
      description: translated text
---
Use some translation engine to translate a text and return the result.
