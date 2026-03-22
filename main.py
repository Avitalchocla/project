import os
import subprocess
import stat
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.utils import platform

def request_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([
            Permission.READ_MEDIA_VIDEO,
            Permission.READ_MEDIA_AUDIO,
            Permission.READ_MEDIA_IMAGES,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.MANAGE_EXTERNAL_STORAGE
        ])

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.status = Label(text="ELAZAR EDITOR PRO", size_hint_y=0.1)
        layout.add_widget(self.status)

        self.filechooser = FileChooserListView(
            path="/sdcard",
            filters=['*.mp4','*.mkv','*.avi','*.mp3','*.wav','*.srt']
        )
        layout.add_widget(self.filechooser)

        btns = BoxLayout(size_hint_y=0.3, spacing=5)

        self.video_btn = Button(text="VIDEO")
        self.audio_btn = Button(text="AUDIO")
        self.subtitle_btn = Button(text="SUBTITLE")
        self.preview_btn = Button(text="▶ PLAY")
        self.open_btn = Button(text="📂 OPEN")
        self.run_btn = Button(text="RUN", background_color=(0,0.7,0,1))

        self.video_btn.bind(on_release=self.set_video)
        self.audio_btn.bind(on_release=self.set_audio)
        self.subtitle_btn.bind(on_release=self.set_subtitle)
        self.preview_btn.bind(on_release=self.preview_audio)
        self.open_btn.bind(on_release=self.open_folder)
        self.run_btn.bind(on_release=self.run)

        for b in [self.video_btn,self.audio_btn,self.subtitle_btn,self.preview_btn,self.open_btn,self.run_btn]:
            btns.add_widget(b)

        layout.add_widget(btns)
        self.add_widget(layout)

        self.video = None
        self.audio = None
        self.subtitle = None
        self.sound = None

        self.ffmpeg = os.path.join(os.path.dirname(__file__), "ffmpeg")
        if os.path.exists(self.ffmpeg):
            os.chmod(self.ffmpeg, os.stat(self.ffmpeg).st_mode | stat.S_IEXEC)

    def set_video(self, _):
        if self.filechooser.selection:
            self.video = self.filechooser.selection[0]
            self.status.text = f"Video: {os.path.basename(self.video)}"

    def set_audio(self, _):
        if self.filechooser.selection:
            self.audio = self.filechooser.selection[0]
            self.status.text = f"Audio: {os.path.basename(self.audio)}"

    def set_subtitle(self, _):
        if self.filechooser.selection:
            self.subtitle = self.filechooser.selection[0]
            self.status.text = f"Subtitle: {os.path.basename(self.subtitle)}"

    def preview_audio(self, _):
        if self.audio:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(self.audio)
            if self.sound:
                self.sound.play()
                self.status.text = "Playing..."

    def open_folder(self, _):
        path = "/sdcard/Download/ELAZAR"
        if platform == 'android':
            from jnius import autoclass
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            File = autoclass('java.io.File')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')

            file = File(path)
            uri = Uri.fromFile(file)

            intent = Intent(Intent.ACTION_VIEW)
            intent.setDataAndType(uri, "*/*")
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)

            currentActivity = PythonActivity.mActivity
            currentActivity.startActivity(intent)

    def run(self, _):
        if not self.video:
            self.status.text = "Select video!"
            return

        out_dir = "/sdcard/Download/ELAZAR"
        os.makedirs(out_dir, exist_ok=True)
        output = os.path.join(out_dir, "final.mp4")

        cmd = [self.ffmpeg, "-y", "-i", self.video]

        if self.audio:
            cmd += ["-i", self.audio, "-map", "0:v:0", "-map", "1:a:0"]

        if self.subtitle:
            cmd += ["-vf", f"subtitles={self.subtitle}:force_style='Alignment=2'"]

        cmd += ["-c:v", "libx264", "-c:a", "aac", "-shortest", output]

        self.status.text = "Processing..."

        try:
            subprocess.run(cmd, check=True)
            self.status.text = "Done! Check Download/ELAZAR"
        except Exception as e:
            self.status.text = str(e)

class Splash(Screen):
    def on_enter(self):
        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'main'), 2)

class MyApp(App):
    def build(self):
        request_permissions()
        sm = ScreenManager()
        sm.add_widget(Splash(name="splash"))
        sm.add_widget(MainScreen(name="main"))
        return sm

MyApp().run()