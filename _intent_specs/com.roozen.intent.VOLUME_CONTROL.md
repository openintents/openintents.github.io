---
title: Open Volumne Settings
action: com.roozen.intent.VOLUME_CONTROL
extras:
  -
    name: TYPE
    type: int
    var: type
    description: Volume Stream (accepted values=AudioManager.STREAM_SYSTEM, AudioManager.STREAM_MUSIC, AudioManager.STREAM_RING, AudioManager.STREAM_VOICE_CALL, AudioManager.STREAM_ALARM, AudioManager.STREAM_NOTIFICATION)
---
Use this intent to pop up a dialog box in your activity to allow the user to manually change one of the six volume streams as listed under input.

This intent could be useful if an app is using several volume types (Alarms and Play Media, for example) and only provides the volume buttons to change volume for one type.

How it Works: Opens dialog box of the specified volume type. User slides a progress bar to choose volume. The volume for that stream changes when the user slides the bar. When finished, the Android GUI for a volume change pops up to display the selected value. User touches OK button to close the dialog.

If the volume type is System, Ringer, or Notification, a volume change will change the Ringmode to Normal (AudioManager.RING_MODE_NORMAL). This is because a change in volume will have no affect, as a user would expect it would, if the Ringmode is still Silent or Vibrate Only.

Explanation of Streams:

AudioManager.STREAM_MUSIC: For media, such as music and video.
AudioManager.STREAM_ALARM: For Alarms.
AudioManager.STREAM_VOICE_CALL: For In-Call Volume, that is, the volume of the other person's voice when in a call.
AudioManager.STREAM_RING: For the ringer volume. Notifications are also on this stream unless the user deselects that option by going to (from home menu) Menu > Settings > Sound & display > Ringer Volume and deselecting the checkbox.
AudioManager.STREAM_SYSTEM: For System volume, such as the sound of button presses, if that setting is turned on, or the camera shutter.
AudioManager.STREAM_NOTIFICATION: Changes the volume for notification alerts.

