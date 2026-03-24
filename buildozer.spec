[app]

# 🏷️ App
title = ELAZAR Editor Pro
package.name = ezedit
package.domain = org.elazar

# 📁 Source
source.dir = .
source.include_exts = py,png,jpg,kv

# 🔢 Version
version = 3.5

# 📦 Dependencies
requirements = python3,kivy

# 📱 Screen
orientation = portrait
fullscreen = 0


# ================= ANDROID =================

# 🎯 API (חשוב מאוד)
android.api = 30
android.minapi = 21
android.sdk = 30

# 🧠 NDK (התיקון הכי חשוב)
android.ndk = 25b

# 🧱 Architecture
android.arch = arm64-v8a

# 🔐 Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 🖼 Splash
android.presplash.filename = presplash.png

# 🧩 Icon
android.icon = icon.png

# 🎬 FFmpeg בתוך האפליקציה
android.add_assets = assets/ffmpeg:ffmpeg


# ================= BUILD =================

[buildozer]

log_level = 2
warn_on_root = 1
