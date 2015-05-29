---
title: Pick Bluetooth Device
action: PICK_BLUETOOTH_DEVICE
out: 
  extras:
    - 
      name: ADDR
      type: String
      var: macAddress
      description: the MAC address
    -
      name: FRIENDLYNAME
      type: String
      var: name
      description: the Name of the Device

author: ligi
submitted: 2011-04-24
---
Let the user pick a Bluetooth Device. Returns MAC Address and Name.
