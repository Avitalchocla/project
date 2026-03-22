[app]
title = ELAZAR EDITOR PRO
package.name = ezedit
package.domain = org.elazar
source.dir = .
source.include_exts = py,png,jpg,ffmpeg

version = 3.5

requirements = python3,kivy==2.3.0

orientation = portrait

icon.filename = icon.png
presplash.filename = presplash.png

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,READ_MEDIA_IMAGES

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

android.accept_sdk_license = True
android.enable_androidx = True

android.release_artifact = apk

[buildozer]
log_level = 2