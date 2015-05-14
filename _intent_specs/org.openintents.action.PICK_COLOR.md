---
title: Pick a Color
action: org.openintents.action.PICK_COLOR
extras:
  -
    name: org.openintents.extra.COLOR
    type: String
    description: default colour or previously selected color
output:
  extras:
    -
      name: org.openintents.extra.COLOR
      type: String
      description: default colour or previously selected color
---
Pick a color using a color picker dialog.

Applications should use `startActivityForResult()` to launch this color picker with a default color specified in the integer Intent extra `"org.openintents.extra.COLOR"`. The chosen color will be returned in an Intent the same way.

