---
title: Add a Tag to the Given Data
action: org.openintents.action.TAG
uri: uri of the tag
extras:
  -
    name: tag
    type: String
    description: the tag for the contents as a string
  -
    name: uri
    type: String
    description: uri string describing the data to be tagged
    sample: contentItemUri.toString()
---

Activity implementing this intent provide means to add the given tag or newly entered tag to the given data.

The data is specified by its content URI.
