[app]
title = FullLifeAI
package.name = fulllifeai
package.domain = org.afei.cn
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

android.api = 33
android.minapi = 24
android.ndk = 25b

requirements = python3,kivy,charset-normalizer==3.5.2

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.debug = True
android.enable_androidx = True
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
