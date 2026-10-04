[app]
package.name = fulllifeai
package.domain = org.fulllife.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# 删掉pyttsx3、face‑recognition、bluetooth
requirements = python3,kivy,cryptography

# 安卓权限
android.permissions = CAMERA,RECORD_AUDIO,BLUETOOTH,ACCESS_WIFI_STATE,INTERNET,USE_BIOMETRIC

android.api = 33
android.ndk = 25b
android.sdk = 24
# 指定APK内置中文字体
android.add_assets = fonts/SourceHanSansCN‑Regular.ttf