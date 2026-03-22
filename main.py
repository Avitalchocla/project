import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader

class MainApp(App):
    def build(self):
        self.sound = None

        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        self.label = Label(text="🎧 בחר קובץ אודיו", size_hint=(1, 0.1))
        layout.add_widget(self.label)

        self.filechooser = FileChooserListView(
            filters=["*.mp3", "*.wav"],
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.filechooser)

        btn_play = Button(text="🎵 נגן", size_hint=(1, 0.1))
        btn_play.bind(on_press=self.play_audio)
        layout.add_widget(btn_play)

        btn_stop = Button(text="⏹ עצור", size_hint=(1, 0.1))
        btn_stop.bind(on_press=self.stop_audio)
        layout.add_widget(btn_stop)

        btn_folder = Button(text="📂 פתח Download", size_hint=(1, 0.1))
        btn_folder.bind(on_press=self.open_downloads)
        layout.add_widget(btn_folder)

        return layout

    def play_audio(self, instance):
        selection = self.filechooser.selection
        if selection:
            path = selection[0]
            self.label.text = f"נבחר: {os.path.basename(path)}"

            if self.sound:
                self.sound.stop()

            self.sound = SoundLoader.load(path)
            if self.sound:
                self.sound.play()

    def stop_audio(self, instance):
        if self.sound:
            self.sound.stop()

    def open_downloads(self, instance):
        os.system('xdg-open /storage/emulated/0/Download')

if __name__ == "__main__":
    MainApp().run()
