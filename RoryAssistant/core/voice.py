import speech_recognition as sr
import pyttsx3

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.speaker = pyttsx3.init()
        # Ajustes para que suene menos robótico
        self.speaker.setProperty('rate', 140)  # Velocidad natural (140 palabras por minuto)
        self.speaker.setProperty('volume', 0.7)  # Volumen medio (0.0 a 1.0)
        # Intentamos elegir una voz en español
        voices = self.speaker.getProperty('voices')
        for voice in voices:
            if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
                self.speaker.setProperty('voice', voice.id)
                break

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
        self.speaker.say(text)
        self.speaker.runAndWait()