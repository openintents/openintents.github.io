---
title: Crop an image
action: com.android.camera.action.CROP
constant: com.android.camera.crop.CropActivity.CROP_ACTION
uri: location of the image, can be empty
extras:
  - 
    name: outputX
    type: int
    var: outputX
    description: width of the output image
  -
    name: outputY
    type: int
    var: outputY
    description: height of the output image
  -
    name: scale
    type: boolean
    var: scale
    description: flag whether output image should be scaled
  - 
    name: scaleUpIfNeeded
    type: boolean
    var: scaleUpIfNeeded
    description: 
  -
    name: aspectX
    type: int
    var: aspectX
  -
    name: aspectY
    type: int
    var: aspectY
  - 
    name: spotlightX
    type: int
    var: spotlightX
  -
    name: spotlightY
    type: int
    var: spotlightY
  -
    name: return-data
    type: boolean
    var: returnData
  -
    name: output
    type: string
    constant: MediaStore.EXTRA_OUTPUT
    var: output
    description: uri of the location where to store the cropped image 
  - 
    name: set-as-wallpaper
    type: boolean
    var: setAsWallpaper
  -
    name: showWhenLocked
    type: boolean
    var: showWhenLocked
  -
    name: outputFormat
    type: String
    var: outputFormat
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

If the caller does not provide an image source as data then the activity should ask the user to pick an image using the Intent.ACTION_GET_CONTENT and mime-type image/*.

The caller may pass an extra EXTRA_OUTPUT to control where this image will be written.
If the EXTRA_OUTPUT is not present, then a small sized image is returned as a Bitmap
object in the extra field. This is useful for applications that only need a small image.
If the EXTRA_OUTPUT is present, then the full-sized image will be written to the Uri
value of EXTRA_OUTPUT.
