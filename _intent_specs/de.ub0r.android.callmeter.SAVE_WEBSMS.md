---
title: Save WebSMS
action: de.ub0r.android.callmeter.SAVE_WEBSMS
extras:
  -
    name: uri
    type: String
    var: msgUri
    description: uri of a sent text message
  -
    name: connector
    type: String
    var: connectorName
    description: name of a WebConnector
component: broadcast
---
Send the URI of a sent text message as broadcast to notify Call Meter 3G that the message was sent with the given WebSMS Connector.
