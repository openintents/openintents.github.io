---
title: Encode
action: com.google.zxing.client.android.ENCODE
extras:
  -
    name: ENCODE_DATA
    type: String
    description: The data to encode
    sample: My link address
  -
    name: ENCODE_TYPE
    type: String
    description: type of data (TEXT_TYPE, EMAIL_TYPE, PHONE_TYPE, SMS_TYPE, CONTACT_TYPE, LOCATION_TYPE)
    sample: TEXT_TYPE
    optional: true

author: dswitkin
submitted: 2008-09-26
---

Encode to barcode and display on screen.

Extra ENCODE_TYPE can be one of the following and defines more extras:

"TEXT_TYPE": Plain text. Use Intent.putExtra(DATA, string). This can be used for URLs too, but string must include "http://" or "https://".

"EMAIL_TYPE": An email type. Use Intent.putExtra(DATA, string) where string is the email address.

"PHONE_TYPE": Use Intent.putExtra(DATA, string) where string is the phone number to call.

"SMS_TYPE": An SMS type. Use Intent.putExtra(DATA, string) where string is the number to SMS.

"CONTACT_TYPE": A contact. Send a request to encode it as follows:
```java
import android.provider.Contacts;

Intent intent = new Intent(Intents.Encode.ACTION);
intent.putExtra(Intents.Encode.TYPE, CONTACT);
Bundle bundle = new Bundle();
bundle.putString(Contacts.Intents.Insert.NAME, "Jenny");
bundle.putString(Contacts.Intents.Insert.PHONE, "8675309");
bundle.putString(Contacts.Intents.Insert.EMAIL, "jenny@the80s.com");
intent.putExtra(Intents.Encode.DATA, bundle);
```
"LOCATION_TYPE": A geographic location. Use as follows:
```java
Bundle bundle = new Bundle();
bundle.putFloat("LAT", latitude);
bundle.putFloat("LONG", longitude);
intent.putExtra(Intents.Encode.DATA, bundle);
```
See [XZing on github](https://github.com/zxing/zxing)
