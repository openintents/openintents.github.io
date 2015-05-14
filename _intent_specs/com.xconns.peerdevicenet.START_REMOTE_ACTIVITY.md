---
title: Remote Intents
action: com.xconns.peerdevicenet.START_REMOTE_ACTIVITY
extras:
  -
    name: REMOTE_INTENT
    description: the intent to be sent to peer 
  - 
    name: PEER_NAME
  - 
    name: PEER_ADDR
  - 
    name: PEER_PORT 
    description: peer device info
---

PeerDeviceNet exposes a group of intents for sending intents to remote devices:

com.xconns.peerdevicenet.START_REMOTE_ACTIVITY
com.xconns.peerdevicenet.START_REMOTE_ACTIVITY_FOR_RESULT
com.xconns.peerdevicenet.START_REMOTE_SERVICE
com.xconns.peerdevicenet.SEND_REMOTE_BROADCAST

for more details, please refer to
http://www.peerdevicenet.net/rmt_intent.html
