---
title: Crop an image
action: com.android.camera.action.CROP
constant: com.android.camera.crop.CropActivity.CROP_ACTION
uri: location of the image, can be empty
extras:
  - 
    name: outputX
    type: int
    description: width of the output image
  -
    name: outputY
    type: int
    description: height of the output image
  -
    name: scale
    type: boolean
    description: flag whether output image should be scaled
  - 
    name: scaleUpIfNeeded
    type: boolean
    description: 
  -
    name: aspectX
    type: int
  -
    name: aspectY
    type: int
  - 
    name: spotlightX
    type: int
  -
    name: spotlightY
    type: int
  -
    name: return-data
    type: boolean
  -
    name: 
    constant: MediaStore.EXTRA_OUTPUT
  - 
    name: set-as-wallpaper
    type: boolean
  -
    name: showWhenLocked
    type: boolean
  -
    name: outputFormat
    type: String
out:
  - 
    name: cropped-rect
    type: boolean
    description: rectangle of the cropped image
  - 
    name: data
    type: android.graphics.Bitmap
author: Friedger Müffke    
submitted: 2016-01-22
---
Take an image and crop it according to the user's requirements. The output can be a URI or a (possibly) downsampled bitmap 
with the cropped image.
