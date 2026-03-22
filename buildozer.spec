[app]

# (str) Title of your application
title = ELAZAR Editor Pro

# (str) Package name
package.name = ezedit

# (str) Package domain
package.domain = org.elazar

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv

# (str) Application version
version = 3.5

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# ================= ANDROID =================

# (int) Android API
android.api = 30

# (int) Minimum API
android.minapi = 21

# (int) Target SDK
android.sdk = 30

# (str) NDK version
android.ndk = 23b

# (str) Architecture
android.arch = arm64-v8a

# Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Splash screen
android.presplash.filename = presplash.png

# App icon
android.icon = icon.png

# Add FFmpeg as asset
android.add_assets = assets/ffmpeg:ffmpeg


# ================= BUILD =================

[buildozer]

# (int) Log level (0 = error only, 2 = info)
log_level = 2

# (bool) Warn on root
warn_on_root = 1
