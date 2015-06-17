---
title: Mirror Text Horizontally
action: org.openintents.action.UPSIDE_DOWN
extras:
  -
    name: org.openintents.extra.TEXT
    type: String
    var: selection
    description: text that should be processed.
  - 
    name: org.openintents.extra.TEXT_BEFORE_SELECTION
    type: String
    var: beforeSelection
  -
    name: org.openintents.extra.TEXT_AFTER_SELECTION
    type: String
    var: afterSelection
out: 
  extras:
    -
      name: org.openintents.extra.TEXT
---
Process a given text and return it upside down.

The text is usually a selection, if the selection is empty, 
the whole text, i.e. before and after the caret is processed.

This action is usually launched with mime type `text/plain` and the following category:
```
org.openintents.category.TEXT_SELECTION_ALTERNATIVE
```
