import random


def generate_avatar(user_seed: str = None):
    """
    :param user_seed: 用户唯一标识(姓名+生日)，传入后同一个用户固定形象；不传完全随机
    :return: 形象描述字符串
    """
    hair_list = ["银白色长发", "黑色短发", "淡蓝色中长发"]
    eye_list = ["金色竖瞳", "深黑色温柔眼眸", "浅紫眼眸"]
    style_list = ["科技透明质感", "柔和光影人形", "暗黑色简约人形"]

    if user_seed:
        random.seed(hash(user_seed))

    hair = random.choice(hair_list)
    eye = random.choice(eye_list)
    style = random.choice(style_list)
    avatar_desc = f"自主生成形象：{style}，{hair}，{eye}，整体适配手机黑色背景。"
    return avatar_desc
