import speech_recognition as sr
from gtts import gTTS
import os
from pygame import mixer

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        mixer.init()  # Inicializamos el mezclador de pygame

    def listen(self):
        with self.microphone as source:
            print("Escuchando... (di 'Rory' para activarme)")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
        try:
            comando = self.recognizer.recognize_google(audio, language="es-ES").lower()
            print(f"Escuché: {comando}")
            return comando
        except sr.UnknownValueError:
            self.speak("No entendí lo que dijiste.")
            return ""
        except sr.RequestError:
            self.speak("Error al conectar con el servicio de voz.")
            return ""

    def speak(self, text):
        tts = gTTS(text=text, lang='es')
        audio_file = "temp_audio.mp3"
        tts.save(audio_file)
        mixer.music.load(audio_file)
        mixer.music.play()
        while mixer.music.get_busy():  # Esperamos a que termine de reproducir
            pass
        os.remove(audio_file)  # Borramos el archivo temporal