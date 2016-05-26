---
title: Permissions across Android versions
subheadline: Encrypted notes went missing
categories: Coding
---

In March, [an issue](https://github.com/openintents/safe/issues/14) was raised that OI Safe and OI Notepad
can't be installed on Lollipop devices due to duplicate permission defintions.
Previously, they were included in both apps to make sure
that the user sees the permission strings when install one or the other app. To fix the issue the permission definition
was removed from the OI Notepad app.

Now, there is [a new issue](https://github.com/openintents/notepad/issues/13) that is much harder to understand: the
defined and given permission is not present in notepad. This only happens to on some devices. Maybe, it depends on the order
both apps are updated, maybe it is related to when the device was upgraded to lollipop. Uninstall (after backup)
and reinstalling OI Notepad does solve the issue.

## Update (2016-04-13)
There is a way to reproduce this behaviour as described in [the issue](https://github.com/openintents/notepad/issues/13#issuecomment-209428535)
by @dicer. Thank you for the investigations.
