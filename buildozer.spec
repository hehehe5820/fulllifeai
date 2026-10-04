[app]
# 全智能生命体
title = FullLifeAI
# QZNSMT
package.name = fulllifeai
# org.AFEI.cn
package.domain = org.fulllifeai
# 1.0.0
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# Android 14
android.api = 33
android.minapi = 24
android.sdk = 24
android.ndk = 25b
# INTERNET   ACCESS_NETWORK_STATE   READ_EXTERNAL_STORAG   WRITE_EXTERNAL_STORAGE   AMERA   ECORD_AUDIO   ACCESS_FINE_LOCATION    ACCESS_COARSE_LOCATION
android.permissions = INTERNET,ACCESS_NETWORK_STATE
requirements = python3,kivy
android.debug = True
android.enable_androidx = True
android.accept_sdk_license = True
[buildozer]
log_level = 2
warn_on_root = 1
