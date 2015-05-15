---
title: Count Pages of PDF Document
action: com.acadoid.pdfview.action.COUNT_PAGES
uri: PDF file Uri
out:
  extras:
    -
      name: PAGES
      type: int
      var: pages
      description: number of pages (and PDF file Uri for convenience)
---
counts the number of pages in a given PDF file

Input:
- Uri of PDF file via Intent.putDataAndType() (should point to a file located on the SD card)

Output:
- number of pages via Intent.getExtras().getInt("PAGES") (the number is zero if a problem occurred)
- Uri of PDF file via Intent.putDataAndType() (Uri of PDF file, mirrored for convenience)
