from cryptography.fernet import Fernet
import os

MEMORY_FILE = "memory.enc"


def save_learn_memory(content: str, user_type: str):
    from core_secure import load_key
    fernet = Fernet(load_key())
    entry = f"【{user_type}】{content}"
    enc = fernet.encrypt(entry.encode("utf‑8"))
    with open(MEMORY_FILE, "ab") as f:
        f.write(enc + b"\n")


def load_all_memory():
    if not os.path.exists(MEMORY_FILE):
        return "暂无学习记忆"
    from core_secure import load_key
    fernet = Fernet(load_key())
    full_text = ""
    with open(MEMORY_FILE, "rb") as f:
        for line in f.readlines():
            try:
                dec = fernet.decrypt(line.strip()).decode("utf‑8")
                full_text += dec + "\n"
            except Exception:
                pass
    return full_text


def self_learn_summary(new_info: str):
    memory = load_all_memory()
    learn_result = f"学习到新信息：{new_info}，历史知识库：{memory[:1000]}"
    save_learn_memory(new_info, "self_learn")
    return learn_result
