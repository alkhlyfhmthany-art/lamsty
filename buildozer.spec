[app]
title = Lamsty
package.name = lamsty
package.domain = org.lamsty

source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1
