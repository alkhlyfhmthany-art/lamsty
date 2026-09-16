[app]
title = Lamsty
package.name = lamsty
package.domain = com.lamsty.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
