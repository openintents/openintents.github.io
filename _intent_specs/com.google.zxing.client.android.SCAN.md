---
title: Scan
action: com.google.zxing.client.android.SCAN
input:
  -
    name: SCAN_MODE
    type: String
    description: >END_
Provide optional scan mode.

By default, sending Scan.ACTION will decode all barcodes that we understand. However it may be useful to limit scanning to certain formats. Use Intent.putExtra(MODE, value) with one of the values below (optional).

"PRODUCT_MODE": Decode only UPC and EAN barcodes. This is the right choice for shopping apps which get prices, reviews, etc. for products.

"ONE_D_MODE": Decode only 1D barcodes (currently UPC, EAN, Code 39, and Code 128).

"QR_CODE_MODE": Decode only QR codes.
END_
    sample: "QR_CODE_MODE"
  -
    name: SCAN_RESULT
author: dswitkin
submitted: 2008-09-26
    
---
Scan a barcode.
