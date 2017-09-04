---
title: Start a Web App
action: com.google.android.apps.chrome.webapps.WebappManager.ACTION_START_WEBAPP
extras:
  -
    name: org.chromium.chrome.browser.webapp_url
    type: String
    var: startUrl
    description: Specifies the start url of the web app
  -
    name: org.chromium.chrome.browser.webapp_source
    type: int
    var: sourceFlag
    description: Specifies where the web app comes from. Only 0 and 1 are valid values    
  -
    name: org.chromium.chrome.browser.webapk_package_name
    type: String
    var: packageName
    description: Specifies the package name of the web app on Android    

---
An intent to start a web app that has been installed on the device as WebApk. This intent is usually only called from
within the web apk only.
