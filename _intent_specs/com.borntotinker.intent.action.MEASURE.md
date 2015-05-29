---
title: Environmental Measurement
action: com.borntotinker.intent.action.MEASURE
extras:
  -
    name: android.intent.extra.measurement.TYPE
    type: String
    var: type
    description: Specifies the physical characteristic being measured.
out:
  The result of the measurement collection will be returned. 
  Units and data types will vary depending on the physical information being measured.
---
An open ended intent to collect information from the android phone's surroundings.

This could be physical information such as spatial measurement, acoustic decibel levels, ambient light levels, vibration sprectrum data, etc.
