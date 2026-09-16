
[app]
title = Lamsty
package.name = lamsty
package.domain = org.lamsty.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.2.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.archs = armeabi-v7a
android.build_tools_version = 33.0.2
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.ant_path = /usr/bin/ant
