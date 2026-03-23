[app]

title = ELAZAR Editor Pro
package.name = ezedit
package.domain = org.elazar

source.dir = .
source.include_exts = py,png,jpg,kv

version = 3.5

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# ===== ANDROID =====

android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b

android.arch = arm64-v8a

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.presplash.filename = presplash.png
android.icon = icon.png

# FFmpeg
android.add_assets = assets/ffmpeg:ffmpeg

# ===== BUILD =====

[buildozer]
log_level = 2
warn_on_root = 1
