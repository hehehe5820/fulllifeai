from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from core_secure import is_core_init_done, save_core_user
from voice_module import speak, listen_voice
from virtual_avatar import generate_avatar
from self_learn import save_learn_memory, load_all_memory

Window.clearcolor = (0, 0, 0, 1)
Window.size = (420, 820)


class FullLifeAIMainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 18
        self.padding = [30, 40, 30, 20]
        self.avatar_text = ""
        self.check_system_init()

    def check_system_init(self):
        if not is_core_init_done():
            self.show_core_register_page()
        else:
            self.show_ai_main_page()

    def show_core_register_page(self):
        self.clear_widgets()
        tip_label = Label(
            text="【全智能生命体｜初始化页面】\n仅可录入一次，保存后本页面永久消失\n录入后核心信息不可查看/修改/删除",
            color=(1, 0.2, 0.2, 1),
            font_size=16,
            size_hint_y=0.2
        )
        self.add_widget(tip_label)

        self.name_input = TextInput(
            hint_text="核心人员 姓名",
            size_hint_y=0.08,
            foreground_color=(1, 1, 1, 1),
            background_color=(0.12, 0.12, 0.12, 1)
        )
        self.birth_input = TextInput(
            hint_text="出生年月日 例：2000‑01‑01",
            size_hint_y=0.08,
            foreground_color=(1, 1, 1, 1),
            background_color=(0.12, 0.12, 0.12, 1)
        )
        self.add_widget(self.name_input)
        self.add_widget(self.birth_input)

        btn_collect = Button(
            text="采集人脸 + 指纹 + 声纹 并锁定核心信息",
            size_hint_y=0.12,
            background_color=(0.3, 0.05, 0.05, 1)
        )
        btn_collect.bind(on_press=self.save_core_user)
        self.add_widget(btn_collect)

    def save_core_user(self, instance):
        name = self.name_input.text.strip()
        birth = self.birth_input.text.strip()
        if len(name) < 1 or len(birth) < 6:
            return

        face_token = "FACE_ENC_00001"
        fp_token = "FINGER_ENC_00001"
        voice_token = "VOICE_ENC_00001"

        user_data = {
            "name": name,
            "birth": birth,
            "face_token": face_token,
            "fp_token": fp_token,
            "voice_token": voice_token
        }
        result_ok = save_core_user(user_data)
        if result_ok:
            self.avatar_text = generate_avatar(user_seed=name + birth)
            save_learn_memory(f"【系统初始化完成】核心用户:{name},虚拟形象:{self.avatar_text}", "system")
            self.show_ai_main_page()

    def show_ai_main_page(self):
        self.clear_widgets()
        avatar_label = Label(
            text=f"全智能生命体\n{self.avatar_text}",
            color=(0.2, 0.8, 1, 1),
            font_size=17,
            size_hint_y=0.22
        )
        self.add_widget(avatar_label)

        self.chat_view = ScrollView(size_hint_y=0.4)
        self.chat_box = GridLayout(cols=1, size_hint_y=None)
        self.chat_box.bind(minimum_height=self.chat_box.setter("height"))
        self.chat_view.add_widget(self.chat_box)
        self.add_widget(self.chat_view)

        self.cmd_input = TextInput(
            hint_text="输入指令...",
            size_hint_y=0.08,
            foreground_color=(1, 1, 1, 1),
            background_color=(0.12, 0.12, 0.12, 1)
        )
        self.add_widget(self.cmd_input)

        btn_row = BoxLayout(spacing=10, size_hint_y=0.1)
        btn_send = Button(text="发送", background_color=(0, 0.25, 0.4, 1))
        btn_voice = Button(text="语音对话", background_color=(0.25, 0, 0.4, 1))
        btn_send.bind(on_press=self.send_text_command)
        btn_voice.bind(on_press=self.start_voice_conversation)
        btn_row.add_widget(btn_send)
        btn_row.add_widget(btn_voice)
        self.add_widget(btn_row)

    def add_chat_msg(self, text, is_ai=False):
        color = (0.3, 0.9, 0.5, 1) if is_ai else (1, 1, 1, 1)
        msg_label = Label(text=text, color=color, size_hint_y=None, height=32, font_size=14)
        self.chat_box.add_widget(msg_label)

    def send_text_command(self, instance):
        cmd = self.cmd_input.text.strip()
        if not cmd:
            return
        self.add_chat_msg(f"你：{cmd}")
        reply = self.handle_command(cmd)
        self.add_chat_msg(f"AI：{reply}", is_ai=True)
        speak(reply)
        self.cmd_input.text = ""

    def start_voice_conversation(self, instance):
        speak("请说出你的指令")
        voice_txt = listen_voice()
        if voice_txt == "UNRECOGNIZED":
            speak("没有识别到声音，请重试")
            self.add_chat_msg("AI：未识别语音", True)
            return
        self.add_chat_msg(f"你：{voice_txt}")
        reply = self.handle_command(voice_txt)
        self.add_chat_msg(f"AI：{reply}", True)
        speak(reply)

    def handle_command(self, cmd: str):
        save_learn_memory(f"用户指令：{cmd}", "user")
        memory_data = load_all_memory()
        return f"收到指令，已执行。历史学习知识库已更新。记忆摘要：{memory_data[:300]}"


class FullLifeAIApplication(App):
    def build(self):
        self.title = "全智能生命体"
        return FullLifeAIMainUI()


if __name__ == "__main__":
    FullLifeAIApplication().run()
