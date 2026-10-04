from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"
USER_DATA_FILE = "user.enc"


def init_key():
    """生成密钥，仅首次运行调用"""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)


def load_key():
    """二进制读取密钥"""
    if not os.path.exists(KEY_FILE):
        init_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()


def is_core_init_done():
    """判断是否已经录入核心用户"""
    return os.path.exists(USER_DATA_FILE)


def save_core_user(user_dict: dict) -> bool:
    """加密保存核心用户信息，二进制wb写入"""
    try:
        init_key()
        fernet = Fernet(load_key())
        import json
        raw = json.dumps(user_dict, ensure_ascii=False).encode("utf‑8")
        enc_data = fernet.encrypt(raw)
        with open(USER_DATA_FILE, "wb") as f:
            f.write(enc_data)
        return True
    except Exception:
        return False


def load_core_user() -> dict or None:
    """读取解密核心用户"""
    if not is_core_init_done():
        return None
    try:
        fernet = Fernet(load_key())
        with open(USER_DATA_FILE, "rb") as f:
            enc = f.read()
        raw = fernet.decrypt(enc).decode("utf‑8")
        import json
        return json.loads(raw)
    except Exception:
        return None
